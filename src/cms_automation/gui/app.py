"""Interface gráfica (Tkinter) para a automação CMS.

Reaproveita inteiramente o núcleo já testado (config, data_source,
workflow) — a GUI é só mais um "adaptador" de entrada, ao lado do CLI.
A automação corre numa thread de fundo (`threading.Thread`), para a
janela nunca travar durante o processamento — ao contrário da v2.0
original, que corria tudo na thread principal do Tkinter.
"""
from __future__ import annotations

import logging
import threading
import tkinter as tk
from datetime import datetime, timedelta
from pathlib import Path
from tkinter import filedialog, messagebox, scrolledtext, ttk

from ..config import AppConfig, ConfigError, load_config
from ..data_source import open_data_source
from ..input.fake_controller import FakeInputController
from ..input.real_controller import RealInputController
from ..vision.fake_backend import FakeVisionBackend
from ..vision.ocr_backend import TesseractVisionBackend
from ..workflow.processor import process_batch
from .log_bridge import QueueLogHandler
from .log_filter import filter_log_entries, parse_date

logger = logging.getLogger(__name__)

CATEGORIES = ["Geral", "Automação", "Captura", "Edição"]


class CmsAutomationApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Automação CMS")
        self.root.geometry("880x640")

        self.appsettings_path = tk.StringVar(value="config/appsettings.yaml")
        self.data_path = tk.StringVar(value="")
        self.dry_run = tk.BooleanVar(value=True)

        self.log_handler = QueueLogHandler()
        self.log_handler.setLevel(logging.INFO)
        logging.getLogger().addHandler(self.log_handler)
        logging.getLogger().setLevel(logging.INFO)

        self.all_log_entries: list = []
        self.category_vars = {cat: tk.BooleanVar(value=True) for cat in CATEGORIES}

        self.cancel_event: threading.Event | None = None
        self.worker_thread: threading.Thread | None = None

        self._build_layout()
        self.root.after(200, self._poll_log_queue)

    # ------------------------------------------------------------------ UI

    def _build_layout(self) -> None:
        top = ttk.Frame(self.root, padding=10)
        top.pack(fill="x")

        ttk.Label(top, text="appsettings.yaml:").grid(row=0, column=0, sticky="w")
        ttk.Entry(top, textvariable=self.appsettings_path, width=60).grid(row=0, column=1, padx=5)
        ttk.Button(top, text="Procurar...", command=self._browse_appsettings).grid(row=0, column=2)

        ttk.Label(top, text="Dados (CSV/Excel):").grid(row=1, column=0, sticky="w", pady=(6, 0))
        ttk.Entry(top, textvariable=self.data_path, width=60).grid(row=1, column=1, padx=5, pady=(6, 0))
        ttk.Button(top, text="Procurar...", command=self._browse_data).grid(row=1, column=2, pady=(6, 0))

        ttk.Checkbutton(top, text="Modo simulação (--dry-run)", variable=self.dry_run).grid(
            row=2, column=1, sticky="w", pady=(6, 0)
        )

        actions = ttk.Frame(self.root, padding=(10, 0))
        actions.pack(fill="x")
        self.start_button = ttk.Button(actions, text="Iniciar", command=self._start)
        self.start_button.pack(side="left")
        self.cancel_button = ttk.Button(actions, text="Cancelar", command=self._cancel, state="disabled")
        self.cancel_button.pack(side="left", padx=5)
        ttk.Button(actions, text="Calibrar coordenadas...", command=self._open_calibration_window).pack(
            side="left", padx=5
        )

        self.progress = ttk.Progressbar(self.root, mode="indeterminate")
        self.progress.pack(fill="x", padx=10, pady=8)

        self.stats_label = ttk.Label(self.root, text="")
        self.stats_label.pack(fill="x", padx=10)

        # Filtros de log
        filter_frame = ttk.LabelFrame(self.root, text="Filtro de logs", padding=8)
        filter_frame.pack(fill="x", padx=10, pady=8)

        self.start_date_var = tk.StringVar(value=(datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d"))
        self.end_date_var = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))
        ttk.Label(filter_frame, text="De:").pack(side="left")
        ttk.Entry(filter_frame, textvariable=self.start_date_var, width=12).pack(side="left", padx=4)
        ttk.Label(filter_frame, text="Até:").pack(side="left")
        ttk.Entry(filter_frame, textvariable=self.end_date_var, width=12).pack(side="left", padx=4)
        for cat in CATEGORIES:
            ttk.Checkbutton(
                filter_frame, text=cat, variable=self.category_vars[cat], command=self._redraw_log
            ).pack(side="left", padx=4)
        ttk.Button(filter_frame, text="Aplicar", command=self._redraw_log).pack(side="left", padx=8)

        self.log_text = scrolledtext.ScrolledText(self.root, state="disabled")
        self.log_text.pack(fill="both", expand=True, padx=10, pady=(0, 10))

    def _browse_appsettings(self) -> None:
        path = filedialog.askopenfilename(filetypes=[("YAML", "*.yaml *.yml")])
        if path:
            self.appsettings_path.set(path)

    def _browse_data(self) -> None:
        path = filedialog.askopenfilename(filetypes=[("CSV/Excel", "*.csv *.xlsx *.xlsm")])
        if path:
            self.data_path.set(path)

    # ------------------------------------------------------------ execução

    def _start(self) -> None:
        appsettings_path = self.appsettings_path.get().strip()
        data_path = self.data_path.get().strip()

        try:
            config = load_config(appsettings_path)
        except ConfigError as exc:
            messagebox.showerror("Configuração inválida", str(exc))
            return

        try:
            data_source = open_data_source(data_path)
        except (FileNotFoundError, ValueError) as exc:
            messagebox.showerror("Dados inválidos", str(exc))
            return

        self.cancel_event = threading.Event()
        self.start_button.config(state="disabled")
        self.cancel_button.config(state="normal")
        self.progress.start(10)
        logger.info("Início do processamento a partir da interface gráfica.", extra={"categoria": "Automação"})

        # Lê as variáveis do Tkinter aqui, na thread principal — nunca
        # dentro da thread de trabalho (o Tkinter não é thread-safe).
        dry_run_value = self.dry_run.get()

        self.worker_thread = threading.Thread(
            target=self._run_worker, args=(config, data_source, dry_run_value), daemon=True
        )
        self.worker_thread.start()
        self.root.after(200, self._poll_worker)

    def _run_worker(self, config: AppConfig, data_source, dry_run_value: bool) -> None:
        if dry_run_value:
            input_ctrl = FakeInputController()
            vision = FakeVisionBackend()
        else:
            input_ctrl = RealInputController()
            vision = TesseractVisionBackend(config.tesseract_cmd)

        self._last_stats = process_batch(
            data_source, config, input_ctrl, vision, cancel_event=self.cancel_event
        )

    def _poll_worker(self) -> None:
        if self.worker_thread and self.worker_thread.is_alive():
            self.root.after(200, self._poll_worker)
            return

        self.progress.stop()
        self.start_button.config(state="normal")
        self.cancel_button.config(state="disabled")
        stats = getattr(self, "_last_stats", None)
        if stats is not None:
            self.stats_label.config(text=stats.summary_text().replace("\n", "  |  "))
        logger.info("Processamento terminado.", extra={"categoria": "Automação"})

    def _cancel(self) -> None:
        if self.cancel_event is not None:
            self.cancel_event.set()
            logger.info("Cancelamento solicitado pelo utilizador.", extra={"categoria": "Automação"})

    # ----------------------------------------------------------------- log

    def _poll_log_queue(self) -> None:
        new_entries = self.log_handler.drain()
        if new_entries:
            self.all_log_entries.extend(new_entries)
            self._redraw_log()
        self.root.after(200, self._poll_log_queue)

    def _redraw_log(self) -> None:
        try:
            start_date = parse_date(self.start_date_var.get())
            end_date = parse_date(self.end_date_var.get())
        except ValueError:
            return  # ainda a escrever a data; não redesenha com erro

        categories = {cat for cat, var in self.category_vars.items() if var.get()}
        filtered = filter_log_entries(self.all_log_entries, start_date, end_date, categories)

        self.log_text.config(state="normal")
        self.log_text.delete("1.0", "end")
        for entry in filtered:
            self.log_text.insert("end", entry.format_line() + "\n")
        self.log_text.see("end")
        self.log_text.config(state="disabled")

    # --------------------------------------------------------- calibração

    def _open_calibration_window(self) -> None:
        from .. import appsettings_editor as ed

        appsettings_path = Path(self.appsettings_path.get().strip())
        try:
            yaml, data = ed.load_editable(appsettings_path)
        except ed.AppsettingsEditError as exc:
            messagebox.showerror("Erro", str(exc))
            return

        window = tk.Toplevel(self.root)
        window.title("Calibrar coordenadas")
        window.geometry("480x520")

        canvas_frame = ttk.Frame(window)
        canvas_frame.pack(fill="both", expand=True, padx=10, pady=10)

        captured: dict[str, tuple[int, int]] = {}
        rows: dict[str, ttk.Label] = {}

        names = ed.list_coordinate_names(data)

        def capture_one(name: str) -> None:
            import pyautogui

            messagebox.showinfo(
                "Capturar", f"Posicione o rato sobre '{name}' e clique OK."
            )
            x, y = pyautogui.position()
            captured[name] = (x, y)
            rows[name].config(text=f"{name}: capturado em ({x}, {y})")

        for name in names:
            old_x, old_y = ed.get_coordinate(data, name)
            row = ttk.Frame(canvas_frame)
            row.pack(fill="x", pady=2)
            label = ttk.Label(row, text=f"{name}: atual ({old_x}, {old_y})", width=45)
            label.pack(side="left")
            rows[name] = label
            ttk.Button(row, text="Capturar", command=lambda n=name: capture_one(n)).pack(side="left")

        def confirm_and_save() -> None:
            if not captured:
                window.destroy()
                return
            if not messagebox.askyesno(
                "Confirmar", f"Gravar {len(captured)} coordenada(s) em {appsettings_path}?"
            ):
                return
            for name, (x, y) in captured.items():
                ed.update_coordinate(data, name, x, y)
            ed.save_editable(yaml, data, appsettings_path)
            logger.info(
                f"{len(captured)} coordenada(s) recalibrada(s) e gravada(s).",
                extra={"categoria": "Edição"},
            )
            messagebox.showinfo("Guardado", "Coordenadas gravadas com sucesso.")
            window.destroy()

        ttk.Button(window, text="Gravar e fechar", command=confirm_and_save).pack(pady=10)


def main() -> int:
    root = tk.Tk()
    CmsAutomationApp(root)
    root.mainloop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

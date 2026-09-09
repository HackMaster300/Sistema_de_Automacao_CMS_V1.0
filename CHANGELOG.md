# Changelog

Este projeto segue [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [2.3.0] — 2026-09

### Adicionado
- **Bundle completo por SO**, pronto a usar assim que descompactado —
  não é só o executável solto. Cada `.zip` de release
  (`cms-automation-windows.zip`, `-linux.zip`, `-macos.zip`) já traz:
  - os dois executáveis (automação + calibração), sem precisar de
    Python;
  - `appsettings.yaml` já copiado do exemplo (pronto para calibrar,
    não precisa de copiar/renomear nada à mão);
  - `dados/identificadores.csv` de exemplo;
  - pastas `assets/error_templates/` e `logs/` já criadas;
  - `COMO_COMECAR.txt` com os passos de arranque.
- `tools/calibrate_coordinates.py` ganhou o seu próprio executável
  (`calibrate-coordinates-<so>`), gerado via `packaging/calibrate.spec`.
- Deteção automática do Tesseract OCR (`ocr.tesseract_cmd: auto` no
  appsettings): procura primeiro uma cópia embutida ao lado do
  executável, depois no PATH do sistema, depois em localizações
  típicas — só falha com uma mensagem clara se não encontrar nada.
- No bundle do **Windows**, o workflow de release tenta instalar o
  Tesseract via Chocolatey e embuti-lo dentro do próprio bundle
  (melhor esforço — se falhar, o bundle segue sem ele e o utilizador
  instala à parte, como nas versões anteriores).
- `packaging/assemble_bundle.py` — script que monta o bundle a partir
  dos executáveis e dos ficheiros do repositório.

### Nota sobre Linux/macOS
- Por agora, o Tesseract **não** é embutido automaticamente no bundle
  do Linux/macOS (a portabilidade de binários com dependências
  dinâmicas nesses SOs exigiria testes que não foi possível validar de
  forma fiável). Continua a ser uma instalação de sistema de uma linha
  (`apt`/`brew`).

## [2.2.0] — 2026-09

### Adicionado
- Executáveis standalone (Windows/Linux/macOS) gerados via PyInstaller
  (`packaging/cms_automation.spec`) — quem só quer usar a ferramenta
  não precisa de instalar Python nem dependências.
- Workflow de release agora tem 4 jobs: `test` → `build-python-package`
  + `build-executable` (matrix nos 3 SOs, em paralelo) →
  `publish-release`, que junta tudo (wheel, sdist, 3 executáveis) numa
  única GitHub Release.

### Nota
- O executável standalone continua a exigir o Tesseract OCR instalado
  no sistema — o PyInstaller empacota as bibliotecas Python, não
  binários de sistema como o Tesseract.

## [2.1.0] — 2026-09

### Adicionado
- Checkpoint de processamento: os dados (CSV ou Excel) ganham colunas
  `estado` e `processado_em`. Uma execução interrompida pode ser
  retomada sem reprocessar identificadores já concluídos.
- Suporte a Excel (`.xlsx`) como alternativa ao CSV para a lista de
  identificadores, via `open_data_source()`.
- `config.yaml` renomeado para `appsettings.yaml` — separa claramente
  configuração de aplicação (coordenadas, OCR, tempos) dos dados a
  processar.
- `tools/calibrate_coordinates.py capture`: captura a posição do rato
  para cada coordenada e grava diretamente no `appsettings.yaml` após
  confirmação, preservando comentários (via `ruamel.yaml`).
- `tools/calibrate_coordinates.py list`: lista as coordenadas
  atualmente configuradas.
- Workflow de CI (GitHub Actions) rodando os testes em Python 3.10–3.12
  a cada push/PR.
- Workflow de release: gera e publica o pacote (`sdist` + `wheel`) como
  artefacto de uma GitHub Release a cada tag `v*`.

### Alterado
- `process_batch()` agora recebe uma `CheckpointDataSource` em vez de
  uma lista simples de identificadores.
- CLI: `--config` continua a funcionar como alias de `--appsettings`.

## [2.0.0] — 2026-09

### Adicionado
- Reescrita completa do v1.0 (script único de ~2.850 linhas) numa
  arquitetura modular: `config`, `parsing`, `vision`, `input`,
  `workflow`.
- Configuração externa (`config.yaml`) — nenhuma coordenada, caminho ou
  dado hardcoded no código.
- Interfaces plugáveis `VisionBackend` e `InputController`, cada uma
  com implementação real e uma falsa para testes/`--dry-run`.
- 13 testes unitários sobre a lógica de negócio, sem depender de ecrã
  real.
- Logging estruturado (consola + ficheiro) em vez de `print`.
- Comportamento seguro por omissão para registos sinalizados como
  "suspeita de fraude": ficam retidos para revisão manual em vez de
  processados automaticamente.
- Modo `--dry-run`.

### Removido
- Dados de identificação de exemplo e caminho de sistema pessoal que
  existiam hardcoded no v1.0.

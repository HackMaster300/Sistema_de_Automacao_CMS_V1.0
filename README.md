# Sistema de Automação CMS — v2.3

![Testes](https://github.com/HackMaster300/Sistema_de_Automacao_CMS_V1.0/actions/workflows/tests.yml/badge.svg)
![Release](https://img.shields.io/github/v/release/HackMaster300/Sistema_de_Automacao_CMS_V1.0)

Automação RPA (Robotic Process Automation) para inserção e processamento
de registos num sistema CMS legado sem API — reconhecimento de estado
via OCR, tratamento de erros de interface, preenchimento condicional de
formulários e checkpoint para retomar lotes interrompidos.

Reescrita completa de um projeto pessoal originalmente escrito como um
único script de ~2.850 linhas (v1.0). Ver `CHANGELOG.md` para o
histórico de versões.

## Porquê reescrever

A v1.0 funcionava, mas tinha os problemas típicos do primeiro projeto
de RPA de alguém: tudo num único ficheiro, coordenadas e caminhos de
sistema hardcoded, a mesma sequência de ~120 cliques/teclas copiada e
colada quatro vezes, e zero testes. Se o processo fosse interrompido a
meio de um lote de 500 registos, não havia como saber onde parar sem
reler os logs à mão.

| | v1.0 | v2.3 |
|---|---|---|
| Estrutura | 1 ficheiro, 2.850 linhas | Pacote Python instalável (`pip install`) |
| Coordenadas/OCR/tempos | Hardcoded no código | `appsettings.yaml` externo, git-ignored |
| Coordenadas — como calibrar | Copiar/colar números à mão | `tools/calibrate_coordinates.py capture` grava direto no appsettings, após confirmação |
| Dados a processar | Lista Python hardcoded | CSV **ou** Excel, fora do repositório |
| Execução interrompida | Recomeça do zero | **Checkpoint**: retoma automaticamente os registos ainda pendentes |
| Sequência de preenchimento | Duplicada 4×, ~500 linhas de teclas soltas | 1 receita de dados, executada por um motor genérico |
| Visão/Input | Chamadas diretas espalhadas | Interfaces plugáveis, com implementação falsa para testes/`--dry-run` |
| "Suspeita de fraude" | Processado automaticamente | Retido para revisão manual por omissão |
| Logs | `print()` | `logging` estruturado (consola + ficheiro) |
| Testes | Nenhum | 20 testes unitários, sem depender de ecrã |
| Versionamento | Nenhum | Tags semânticas + Release automática no GitHub |
| Instalação para quem só usa | Copiar o script, instalar libs à mão | Descompactar o bundle e correr — zero Python, appsettings já incluído |

Ver `legacy/estilo_original_exemplo.py` para uma amostra (anonimizada)
do estilo original.

## Arquitetura

```
src/cms_automation/
├── config.py            # carrega e valida appsettings.yaml (dataclasses)
├── parsing.py            # texto OCR bruto -> registos estruturados
├── stats.py               # contadores e relatório final
├── data_source.py        # CSV/Excel com checkpoint (estado/processado_em)
├── logging_setup.py      # logging para consola + ficheiro
├── cli.py                 # ponto de entrada (argparse) / comando `cms-automation`
├── vision/                # VisionBackend: interface + real (pyautogui/pytesseract) + falsa
├── input/                 # InputController: interface + real (pyautogui/keyboard) + falsa
└── workflow/
    ├── states.py           # enum RecordState + ParsedRecord
    ├── steps.py             # Step + StepRunner (motor genérico de execução)
    ├── actions.py           # receitas de preenchimento por estado
    └── processor.py         # orquestração do lote, com checkpoint
```

## Instalação

### Opção 1 — Bundle completo, pronto a usar (recomendado para quem não é programador)

Cada [release](../../releases) inclui um `.zip` por sistema operativo —
`cms-automation-windows.zip`, `cms-automation-linux.zip`,
`cms-automation-macos.zip`. Basta descarregar o do seu SO e
descompactar. Já vem tudo dentro, pronto a usar:

```
cms-automation-windows/
├── cms-automation-windows.exe        # executável principal
├── calibrate-coordinates-windows.exe # ferramenta de calibração
├── appsettings.yaml                  # já copiado, pronto para calibrar
├── dados/identificadores.csv         # dados de exemplo
├── assets/error_templates/           # pasta pronta para as suas imagens de erro
├── logs/                             # pasta pronta para os logs
├── tesseract/                        # (Windows) Tesseract embutido, se o build o conseguiu incluir
└── COMO_COMECAR.txt                  # guia rápido de arranque
```

Não precisa de instalar Python, nem copiar `appsettings.example.yaml`
para `appsettings.yaml` à mão — já vem feito. Siga o `COMO_COMECAR.txt`
de dentro do bundle.

> **Tesseract OCR:** no bundle do Windows, o processo de release tenta
> embutir o Tesseract automaticamente (pasta `tesseract/` já incluída,
> nada a instalar). No Linux/macOS isso ainda não é feito de forma
> fiável — é preciso um único comando (`sudo apt install tesseract-ocr`
> ou `brew install tesseract`) antes da primeira execução. O
> `appsettings.yaml` já vem com `tesseract_cmd: auto`, que deteta
> sozinho onde o Tesseract está (embutido, ou instalado no sistema).

### Opção 2 — Como pacote Python (`pip`)

```bash
pip install .
# fica disponível o comando:
cms-automation --appsettings config/appsettings.yaml
```

### Em modo desenvolvimento

```bash
pip install -e ".[dev]"          # + pytest e build, para contribuir
pip install -e ".[calibration]"  # + ruamel.yaml, só para usar tools/calibrate_coordinates.py capture
pip install -e ".[packaging]"    # + pyinstaller, só para gerar os executáveis localmente
```

### Gerar o bundle localmente

```bash
pip install -e ".[calibration,packaging]"
cd packaging
pyinstaller cms_automation.spec --distpath ../dist --workpath ../build
pyinstaller calibrate.spec --distpath ../dist --workpath ../build
cd ..
python packaging/assemble_bundle.py \
    --os linux \
    --exe-path dist/cms-automation \
    --calibrate-exe-path dist/calibrate-coordinates \
    --output-dir bundle
```

## Releases

Cada versão publicada gera automaticamente um pacote instalável
(`.whl` + `.tar.gz`) anexado a uma GitHub Release, via
`.github/workflows/release.yml`. Para publicar uma nova versão:

```bash
# 1. Atualize a versão em pyproject.toml e descreva as mudanças em CHANGELOG.md
# 2. Crie e envie a tag
git tag v2.3.0
git push origin v2.3.0
```

O workflow corre os testes, constrói o pacote e publica a release
automaticamente — sem precisar de gerar o `.whl` manualmente.

## Configuração — appsettings.yaml

```bash
cp config/appsettings.example.yaml config/appsettings.yaml
```

O `appsettings.yaml` contém apenas configuração de **aplicação**:
coordenadas de UI, região de OCR, imagens de deteção de erro, tempos de
espera. Nunca deve ser commitado — está no `.gitignore` porque
coordenadas e caminhos variam por máquina/resolução.

### Calibrar as coordenadas

Se estiver a usar o bundle (sem Python instalado):

```bash
./calibrate-coordinates-linux list --appsettings appsettings.yaml
./calibrate-coordinates-linux capture --appsettings appsettings.yaml
```

Se estiver a correr a partir do código-fonte:

```bash
# Lista as coordenadas atuais
python tools/calibrate_coordinates.py list --appsettings config/appsettings.yaml

# Recalibra todas: para cada uma, posicione o rato e pressione Enter
python tools/calibrate_coordinates.py capture --appsettings config/appsettings.yaml

# Ou recalibra só algumas
python tools/calibrate_coordinates.py capture --appsettings config/appsettings.yaml \
    --only botao_ok_erro,botao_anterior
```

No fim de um `capture`, é mostrado um resumo (coordenada antiga vs.
nova) e só é gravado no ficheiro se você confirmar com `s`. A gravação
preserva todos os comentários e a estrutura do `appsettings.yaml`.

## Dados e checkpoint

Os identificadores a processar vivem num **CSV ou Excel** — nunca no
código, nunca no `appsettings.yaml`. Formato (ver
`data/sample_identifiers.csv`):

| identificador | estado | processado_em |
|---|---|---|
| 00000000001 | pendente | |
| 00000000002 | concluido | 2026-09-01T10:15:00 |
| 00000000003 | erro | 2026-09-01T10:16:30 |

- `estado` pode ser `pendente`, `concluido` ou `erro`. Se a coluna não
  existir, todas as linhas são tratadas como `pendente`.
- A cada identificador processado, o ficheiro é **atualizado
  imediatamente** (checkpoint) — não só no fim do lote.
- Ao correr novamente com o mesmo ficheiro, apenas as linhas ainda
  `pendente` são processadas. Um lote interrompido a meio retoma
  sozinho de onde parou, sem reprocessar o que já foi feito.
- Para reprocessar algo marcado `erro`, edite a célula/coluna `estado`
  de volta para `pendente` (ou apague o valor).

Excel funciona da mesma forma — basta apontar `--data caminho.xlsx`; as
colunas `estado`/`processado_em` são criadas automaticamente na
primeira execução, se ainda não existirem.

> **Importante:** nem o ficheiro de dados nem o `appsettings.yaml` são
> criados automaticamente por nada neste projeto — ambos têm de já
> existir antes de correr a automação ou a calibração. Isto é
> intencional: evita rodar um lote silenciosamente contra um ficheiro
> vazio criado por engano, ou sobrescrever coordenadas que nunca foram
> calibradas. Se o ficheiro não existir, cada ponto de entrada
> (`load_config`, `open_data_source`, `calibrate_coordinates.py`)
> falha com uma mensagem clara em vez de criar algo do zero.

## Uso

```bash
# Simula a execução sem mexer no rato/teclado nem ler o ecrã
cms-automation --appsettings config/appsettings.yaml --dry-run

# Execução real, com um ficheiro de dados específico
cms-automation --appsettings config/appsettings.yaml --data data/lote_2026_01.xlsx

# --config continua a funcionar como alias de --appsettings
cms-automation --config config/appsettings.yaml
```

## Testes

```bash
pytest tests/ -v
```

Os 20 testes correm sobre `FakeInputController`, `FakeVisionBackend` e
ficheiros temporários de checkpoint — nenhum precisa de ecrã real,
Tesseract instalado, ou um CMS de verdade.

## Segurança e revisão de casos sinalizados

Por omissão (`require_confirmation_for_fraud_flag: true`), qualquer
registo cujo texto OCR contenha "suspeita de fraude" **não** é
processado automaticamente — fica contabilizado e registado em log
para revisão manual. Casos sinalizados para revisão humana devem passar
por confirmação de um analista antes de qualquer preenchimento
automático, mesmo quando o sistema legado permitiria fazê-lo sem
intervenção.

## Limitações conhecidas

- Continua a depender de coordenadas de ecrã fixas e de uma
  resolução/layout estável do CMS — é a natureza de RPA baseado em UI.
- `form_defaults` (em `appsettings.yaml`) ainda usa valores fixos para
  alguns campos técnicos do formulário. No sistema legado, esses campos
  só precisam de estar preenchidos com algum valor para o registo poder
  ser submetido — o próprio sistema depois recalcula/corrige a partir
  dos dados reais do contador já existentes na base de dados. Os
  valores fixos cumprem esse requisito; não substituem os dados reais.
- Sensível a mudanças de layout do sistema legado.

## Autor

Zerdone Rocha — [LinkedIn](#) · [GitHub](https://github.com/HackMaster300)

## Licença

MIT — ver `LICENSE`.

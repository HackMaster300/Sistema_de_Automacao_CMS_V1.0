# 🤖 Sistema de Automação CMS V1.0

> Sistema sofisticado de automação para processamento de dados em sistemas de gestão de clientes (CMS)

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![Automation](https://img.shields.io/badge/Automation-Desktop%20GUI-orange.svg)
![Status](https://img.shields.io/badge/version-1.0-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey.svg)

## 📖 Sobre o Projeto

Sistema de automação desenvolvido em Python para processar grandes volumes de registros em plataformas CMS (Customer Management Systems). A ferramenta automatiza tarefas repetitivas de inserção de dados com detecção inteligente de erros e processamento automatizado de fluxos de trabalho complexos.

### ✨ Funcionalidades Principais

- ✅ **Processamento em Lote** - Automação de múltiplos registros sequenciais
- ✅ **OCR Inteligente** - Reconhecimento de texto em interfaces gráficas
- ✅ **Detecção de Erros** - Identificação automática de falhas no sistema
- ✅ **Navegação Automática** - Interação inteligente com elementos da interface
- ✅ **Processamento Condicional** - Lógica adaptativa baseada no estado dos registros
- ✅ **Logs Detalhados** - Monitoramento completo do processo de automação

## 🛠️ Tecnologias Utilizadas

### Linguagem Principal
- **Python 3.6+** - Lógica principal de automação

### Bibliotecas de Automação
- **PyAutoGUI** - Controle de mouse e teclado
- **Keyboard** - Detecção de eventos de teclado
- **Pyperclip** - Manipulação da área de transferência

### Processamento de Imagens & OCR
- **Pytesseract** - Reconhecimento óptico de caracteres (OCR)
- **PIL (Pillow)** - Processamento de imagens e capturas de tela

### Utilitários
- **Time** - Controle de delays e sincronização
- **Re** - Processamento de expressões regulares
- **Sys** - Controle de execução do programa

## 📦 Instalação

### Pré-requisitos
```bash
# Instalar Tesseract OCR
# Windows: https://github.com/UB-Mannheim/tesseract/wiki
# Linux: sudo apt install tesseract-ocr

# Instalar dependências Python
pip install pyautogui pyperclip keyboard pillow pytesseract
Configuração do Tesseract
python
# Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Linux
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
🎯 Como Usar
Execução Básica
bash
git clone https://github.com/HackMaster300/Sistema_de_Automacao_CMS_V1.0.git
cd Sistema_de_Automacao_CMS_V1.0
python cms.py
or
python cms_before.py

Preparação do Ambiente
Posicione a janela do CMS na área de trabalho

Configure as coordenadas no script conforme sua resolução

Prepare a lista de dados a serem processados

Execute o script e monitore o processo

Fluxo de Trabalho
text
1. Inserção de dados → 2. Verificação de erros → 3. Processamento OCR
4. Análise de estado → 5. Ação condicional → 6. Próximo registro
🔧 Funcionalidades Detalhadas
🔍 Processamento de Dados
Entrada Automática: Inserção sequencial de números de identificação

Validação em Tempo Real: Detecção imediata de erros no sistema

Fallback Inteligente: Mecanismos de recuperação para falhas

📊 Sistema OCR Avançado
python
# Captura e análise de texto da interface
screenshot = pyautogui.screenshot(region=area)
texto_extraido = pytesseract.image_to_string(screenshot)
🎮 Navegação Automatizada
Cliques Precisos: Interação com elementos específicos da interface

Preenchimento de Formulários: Automação completa de campos

Navegação entre Telas: Fluxo automatizado entre diferentes seções

⚡ Estados de Processamento
O sistema detecta e age conforme o estado de cada registro:

"Registado": Processamento completo

"Em processamento": Ações específicas para pendências

"Introduzido": Fluxo padrão de inserção

📁 Estrutura do Código
python
cms.py
├── Variáveis de Configuração
│   ├── Coordenadas de interface
│   ├── Caminhos de imagens de erro
│   └── Lista de dados para processamento
├── Processamento Principal
│   ├── Inserção de dados
│   ├── Detecção de erros
│   ├── Captura OCR
│   └── Análise de estado
└── Fluxos Condicionais
    ├── Registrado
    ├── Em processamento
    └── Introduzido
⚙️ Configuração
Coordenadas da Interface
python
# Exemplo de configuração de coordenadas
x_pf, y_pf = 53, 250                    # Campo PF
x_contador_btn, y_contador_btn = 366, 251 # Botão Contador
x_ok_btn, y_ok_btn = 846, 475           # Botão OK de erro
area = (41, 526, 905, 145)              # Área de captura OCR
Imagens de Detecção de Erro
python
# Configurar caminhos das imagens de referência
erro_img_path = "caminho/para/erro.png"
erro_img_path1 = "caminho/para/erro1.png" 
erro_img_path2 = "caminho/para/erro2.png"
Dados de Processamento
python
# Lista de números para processamento
dados = ['01317788162', '54280992519', '45135422488', ...]
📊 Estatísticas e Monitoramento
O sistema fornece relatórios completos:

Tempo de execução total e por registro

Contadores por estado de processamento

Taxa de sucesso e detecção de erros

Logs detalhados para auditoria

python
print(f"Total processado: {total_processados}")
print(f"Introduzidos: {contador_introduzido}")
print(f"Em processamento: {contador_em_processamento}")
print(f"Registados: {contador_registados}")
print(f"Erros: {numeros_errados}")
🚨 Gestão de Erros
Detecção de Falhas
Timeouts de interface

Imagens não encontradas

Erros de OCR

Estados inesperados

Mecanismos de Recuperação

Fallbacks para diferentes cenários

Logs para debugging

Interrupção segura com Ctrl+C

🔄 Fluxo de Processamento
1. Fase de Inserção
text
Clique PF → Clique Contador → Colar Dado → Enter → Verificar Erro
2. Fase de Análise
text
Captura Tela → OCR → Processar Texto → Identificar Estado
3. Fase de Ação
text
Estado "Registado" → Fluxo Completo
Estado "Processamento" → Fluxo Simplificado  
Estado "Introduzido" → Fluxo Padrão
⚠️ Considerações Importantes
Requisitos de Sistema
Resolução consistente da tela

Acesso administrativo para automação

Ambiente estável sem interferências

Backup dos dados antes do processamento

Limitações Conhecidas
Dependente da estabilidade da interface gráfica

Requer calibração inicial das coordenadas

Sensível a mudanças no layout do CMS

🛡️ Boas Práticas
Antes da Execução
bash
1. Faça backup dos dados
2. Teste em ambiente controlado
3. Verifique coordenadas e configurações
4. Prepare plano de rollback
Durante a Execução
bash
1. Monitore os logs constantemente
2. Mantenha o sistema estável
3. Evite interferências manuais
4. Tenha Ctrl+C preparado para emergências
🤝 Contribuindo
Para contribuir com o projeto:

Reporte bugs através de Issues

Sugira melhorias no sistema de automação

Compartilhe configurações para diferentes ambientes

Documente casos de uso específicos

Áreas de Melhoria
Interface de configuração gráfica

Suporte a múltiplos layouts de CMS

Sistema de templates para diferentes fluxos

Relatórios em PDF automáticos

📄 Licença
Distribuído sob licença MIT. Veja LICENSE para mais informações.

👤 Autor
Zerdone Rocha

💼 LinkedIn: Zerdone Rocha

🐙 GitHub: HackMaster300

📈 Resultados e Benefícios
⏱️ Eficiência
Redução de 90% no tempo de processamento

Processamento contínuo sem intervenção manual

Escalabilidade para grandes volumes de dados

🎯 Precisão
Eliminação de erros humanos

Validação automática de dados

Consistência nos processos

📊 Controle
Logs detalhados para auditoria

Métricas de performance

Detecção proativa de problemas

<div align="center">
⚡ Automatize processos repetitivos e foque no que realmente importa!

https://img.shields.io/github/stars/HackMaster300/Sistema_de_Automacao_CMS_V1.0?style=social


</div> ```

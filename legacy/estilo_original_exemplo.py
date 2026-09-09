"""Exemplo ilustrativo do estilo do V1.0 (NÃO é o código original —
apenas uma amostra reconstruída para fins de comparação no README).

O V1.0 real tinha ~2.850 linhas com este padrão repetido quatro vezes
(uma por cada variação de contagem de linhas do OCR) e três estados
cada, além de dados de identificação e um caminho de sistema pessoal
hardcoded no topo do ficheiro — removidos aqui de propósito.
"""

# Coordenadas fixas, só válidas na máquina/resolução do autor original
x_pf, y_pf = 53, 250
x_contador_btn, y_contador_btn = 366, 251

pyautogui.click(x_pf, y_pf, button='left', clicks=2, interval=0.25)
time.sleep(0.9)
pyautogui.click(x_contador_btn, y_contador_btn, button='left', clicks=1, interval=0.25)
time.sleep(0.1)

# ... e mais ~120 linhas de cliques/teclas por estado, repetidas
# quase identicamente quatro vezes ao longo do ficheiro.

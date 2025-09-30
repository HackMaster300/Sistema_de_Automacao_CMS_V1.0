import pyautogui
import time
import keyboard




# print("Posicione o cursor sobre o ponto desejado. As coordenadas serão exibidas a cada 2 segundos. Pressione Ctrl+C para interromper.")

# try:
#     while True:
#         x, y = pyautogui.position()
#         print(f"Coordenadas atuais: ({x}, {y})")
#         time.sleep(2)
# except KeyboardInterrupt:
#     print("\nCaptura de coordenadas interrompida.") 
    


# import pyautogui
# import time

# Função para capturar a área da tela selecionada pelo usuário
def capturar_area():
   
    x1= 33
    y1= 519
    x2= 951
    y2= 680
    # Calcula a largura e altura da área
    largura = x2 - x1
    altura = y2 - y1

    print(f"A área selecionada é: (x1: {x1}, y1: {y1}, largura: {largura}, altura: {altura})")
    
    # Retorna as coordenadas e as dimensões da área
    return (x1, y1, largura, altura)

# Captura a área
area_selecionada = capturar_area()

# Exibe as coordenadas e dimensões da área selecionada
print(f"Área capturada com sucesso: {area_selecionada}")

# Agora você pode usar essa área para capturar a tela posteriormente




























# import pyautogui
# import time

# # Defina a área para captura e clique
# area = (33, 493, 917, 159)  # Área para verificar rolagem
# click_position = (935, 614)  # Coordenada onde o clique será realizado antes da rolagem
# time.sleep(2)

# def verificar_rolagem():
#     """Verifica se há mais conteúdo para ser rolado na tela."""

#     # Clique na área especificada antes de verificar a rolagem
#     pyautogui.click(click_position)
#     time.sleep(0.5)  # Aguarde um pequeno intervalo após o clique

#     # Captura a imagem da parte inferior da área visível
#     inicio = pyautogui.screenshot(region=(area[0], area[1] + area[3] - 50, area[2], 50))
#     pyautogui.scroll(-300)  # Role para baixo
#     time.sleep(1)  # Aguarde a rolagem ser concluída

#     # Captura a imagem novamente após a rolagem
#     fim = pyautogui.screenshot(region=(area[0], area[1] + area[3] - 50, area[2], 50))
#     return inicio != fim  # Retorna True se as imagens forem diferentes (há mais conteúdo)

# # Verificar se há rolagem
# if verificar_rolagem():
#     print("Existe rolagem.")
# else:
#     print("Sem rolagem.")

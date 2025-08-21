import pyautogui
import pyperclip
import keyboard
import time
import pytesseract
from PIL import Image
import re
import sys  # Para sair do programa

# Caminho do executável do Tesseract (ajuste conforme seu sistema)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Para Windows


pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"  # Caminho no Linux



# Lista de dados a serem colados
dados    = ['01317788162', '54280992519', '45135422488', '07140230819', '07140230777', '14478289367', '22121009181', '54737358579', '14478544761', '07140230785', '54739932249', '54204478322', '04285033579', '01345668451', '04258222472', '14478194104', '45128758405', '54180164706', '14478188676', '22114396702', '14320541759', '14478136307', '04258222449', '04258225160', '04258222506', '04258222480', '54739838370', '30280150795', '14316689299', '04258237173', '04262330550', '45129656042', '01343903504', '54734257428', '01621017175', '01351257736', '01348073220', '22117896112', '01349462463', '22121001220', '01348783059', '22129127662', '07048424084', '54205345835', '54227693501', '14316158410', '01621020658', '04284835198', '01348267582']

# def introduzir():
#     print      54217292082

# def colocar_em_processamento():
#     print

# def resolver():
#     print

# Variáveis para marcar a hora de início e fim
hora_inicio = time.time() + 2 * 3600
num_dados = len(dados)

# Coordenadas fixas
area = (41, 526, 905, 145)  # Ajuste conforme necessário

# Coordenadas fixas
x_pf, y_pf = 53, 250
x_contador_btn, y_contador_btn = 366, 251
x_ok_btn, y_ok_btn = 846, 475  # Coordenadas do botão "OK" no erro
x_clique_esquerdo, y_clique_esquero = 490, 404
x_seguinte, y_seguinte = 512, 735
x_processamento,y_processamento = 351, 356
x_processamento_seguinte, y_processamento_seguinte = 507, 667
x_imprimir, y_imprimir = 563, 191
x_processamento_sim, y_processamento_sim = 507, 667
x_registado, y_registado = 542, 360
x_registado_seguinte, y_registado_seguinte = 507, 667
x_registado_cmp1, y_registado_cmp1 = 471, 180                       
x_registado_cmp_potencia, y_registado_cmp1_potencia = 807, 283
x_propriedade, y_propriedade = 791, 308
x_gis_x, y_gis_x = 777, 332
x_gis_y, y_gis_y = 777, 355
x_estado_instalacao, y_estado_instalacao = 479, 393
x_num_luz, y_num_luz = 775, 393
x_quartos, y_quartos = 775, 412
x_registro, y_registro = 507, 667
x_registado_sim, y_registado_sim = 507, 667
x_anterior, y_anterior = 385, 734
area2 = (442, 248, 87, 16)
click_position = (935, 660) 
# Caminho absoluto para a imagem do erro
# para windows
# erro_img_path = 'C:\\Users\\Zerdo\\Desktop\\cms\\erro.png'  
# erro_img_path2 = 'C:\\Users\\Zerdo\\Desktop\\cms\\erro2.png'
# erro_img_path1 = 'C:\\Users\\Zerdo\\Desktop\\cms\\erro1.png' 

# para linux
erro_img_path = "/home/zebito/Downloads/drive/cms/linux/erro.png" 
erro_img_path2 = "/home/zebito/Downloads/drive/cms/linux/erro2.png"
erro_img_path1 = "/home/zebito/Downloads/drive/cms/linux/erro1.png"# Ajuste conforme necessário


# Definir a área da tela para capturar (x, y, largura, altura)




total_processados = 0
contador_em_processamento = 0
contador_registados = 0
contador_introduzido = 0
numeros_errados = 0  

# Monitorar a combinação Ctrl + Q para interrupção
# Encerra o programa de maneira segura
try:
    time.sleep(2)
    for item in dados:
        # Verificar interrupção antes de cada operação
    

        # Clica automaticamente em 'PF.:' 
        pyautogui.click(x_pf, y_pf, button='left', clicks=2, interval=0.25)
        time.sleep(0.9)

        # Clica no botão 'Contador'
        pyautogui.click(x_contador_btn, y_contador_btn, button='left', clicks=1, interval=0.25)
        time.sleep(0.1)

        # Copiar o item
        pyperclip.copy(item)

        # Colar o item
        pyautogui.hotkey("ctrl", "v")
        print(item)
        time.sleep(0.5)



        # Pressionar Enter
        keyboard.press_and_release("enter")
        time.sleep(0.5)
        keyboard.press_and_release("enter")
        time.sleep(0.5)
        total_processados += 1



        # Verifica se o erro apareceu
        try:
            erro_na_tela = pyautogui.locateOnScreen(erro_img_path, confidence=0.7)
            erro_na_tela1 = pyautogui.locateOnScreen(erro_img_path1, confidence=0.5)  # Aumentar a confiança

            if erro_na_tela:
                numeros_errados += 1
                # print("Erro detectado, clicando em OK...")
                # Clica no botão "OK"
                pyautogui.click(x_ok_btn, y_ok_btn, button='left', clicks=1, interval=0.25)
                # keyboard.press_and_release("space")
                # Aguarda mais tempo para a interface responder

            continue
                
    
        except pyautogui.ImageNotFoundException:
            # print("Erro não encontrado.")
            # Clica com o botão direito na coordenada especificada
            pyautogui.click(x_clique_esquerdo, y_clique_esquero, button='left', clicks=2, interval=0.25)
            time.sleep(1)

            # Verifica novamente se o erro apareceu após o clique direito
            try:
                erro_na_tela2 = pyautogui.locateOnScreen(erro_img_path2, confidence=0.7)
                if erro_na_tela2:
                    # print("Erro detectado após clique direito, clicando em OK...")
                    # Clica no botão "OK"
                    pyautogui.click(x_ok_btn, y_ok_btn, button='left', clicks=1, interval=0.25)
                    time.sleep(2)

                    # Pressiona Enter novamente
                    keyboard.press_and_release("enter")
                    time.sleep(2)
                    break
                else:
                    print("Erro não detectado após clique direito.")

            except pyautogui.ImageNotFoundException:
                print("Erro não encontrado após clique direito.")

        # Segunda parte do código: captura de tela e análise de texto
        screenshot = pyautogui.screenshot(region=area)

        # Usar o pytesseract para extrair texto da captura de tela
        texto_extraido = pytesseract.image_to_string(screenshot)

        # Mostrar o texto extraído (para depuração)
        print("Texto extraído:\n", texto_extraido)

        # Dividir o texto extraído em linhas, removendo espaços em branco extras
        linhas = [linha.strip() for linha in texto_extraido.split('\n') if linha.strip()]
        
        total_grupos = len(linhas) // 3
        tipos = linhas[:total_grupos]
        estados = linhas[total_grupos:2 * total_grupos]
        centros = linhas[2 * total_grupos:]

        # Combinar os dados correspondentes
        linhas_combinadas = []
        for i in range(total_grupos):
            linha_completa = f"{tipos[i]} {estados[i]} {centros[i]}"
            linhas_combinadas.append(linha_completa)

        # Mostrar as linhas combinadas
        print("\nLinhas Combinadas:")
        for linha in linhas_combinadas:
            print(linha)

        encontrou_linha = False
        
        
        # Garantir que temos um número de linhas múltiplo de 3 (para combinar corretamente)
        if len(linhas) % 3 != 0:
            print("Erro: O número de linhas não é múltiplo de 3. Verifique a captura.")
            
            # Definir os comportamentos baseados em palavras-chave
            encontrou_linha = False
            for i, linha in enumerate(linhas_combinadas):
                if 'suspeita de fraude' in linha.lower(): 
                    if 'registad' in linha.lower():
                        print(f"Linha encontrada (Registado): {linha}")
                        encontrou_linha = True

                        contador_registados +=1
                        # Captura os primeiros dígitos (OT) no início da linha
                        match = re.match(r'^\d+', linha)
                        if match:
                            ot = match.group()
                            print(f"OT encontrado: {ot}")

                            altura_linha = 20  # Ajuste conforme necessário para a altura da linha real
                            y_pos = area[1] + (i * altura_linha) + 5
                            x_pos = area[0] + 30  # Ajuste conforme necessário para a primeira coluna

                            # Mover o mouse para a posição da linha específica e clicar
                            pyautogui.moveTo(x_pos, y_pos)
                            pyautogui.click()
                            
                            pyautogui.click(x_seguinte, y_seguinte, button='left', clicks=2, interval=0.25)
                            time.sleep(1)

                            pyautogui.click(x_processamento,y_processamento, button='left', clicks=2, interval=0.25)
                            time.sleep(1)

                            pyautogui.click(x_processamento_seguinte, y_processamento_seguinte, button='left', clicks=1, interval=0.25)
                            time.sleep(1)

                            pyautogui.click(x_imprimir, y_imprimir, button='left', clicks=1, interval=0.25)
                            time.sleep(0.5)

                            pyautogui.click( x_processamento_sim, y_processamento_sim, button='left', clicks=1, interval=0.25)
                            time.sleep(0.5)

                            pyautogui.click(x_registro, y_registro, button='left', clicks=2, interval=0.25)
                            time.sleep(1)

                            pyautogui.click(x_registado_seguinte, y_registado_seguinte, button='left', clicks=1, interval=0.25)
                            time.sleep(1)

                            pyautogui.click(x_registado_cmp1, y_registado_cmp1 , button='left', clicks=1, interval=0.25)
                            time.sleep(1)

                            keyboard.press_and_release('r')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('v')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('2')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('2')
                            time.sleep(0.2)

                            keyboard.press_and_release('shift+tab')
                            time.sleep(2)

                            screenshot = pyautogui.screenshot(region=area2)
                            texto_extraido = pytesseract.image_to_string(screenshot)
                            
                            texto_extraido = texto_extraido.strip()  # Remove espaços no início e no fim
                            texto_extraido = texto_extraido.replace("\n", "")  # Remove quebras de linha

                            # Mostrar o texto extraído para depuração
                            print("Texto extraído:\n", texto_extraido)

                            # Comparar o texto
                            if texto_extraido == "22000 V":
                                keyboard.press_and_release('tab')
                                time.sleep(0.2)
                                keyboard.press_and_release('2')
                                time.sleep(0.2)
                                
                            else:
                                keyboard.press_and_release('tab')
                                time.sleep(0.2)
                                
                            keyboard.press_and_release('tab')
                            time.sleep(0.2)
                            keyboard.press_and_release('s')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('s')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('r')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('2')
                            keyboard.press_and_release('0')
                            keyboard.press_and_release('0')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('4')
                            keyboard.press_and_release('3')
                            time.sleep(0.2)
        
                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('4')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('2')
                            keyboard.press_and_release('0')
                            keyboard.press_and_release('0')
                            time.sleep(1)
                            
                            pyautogui.click(x_registado_cmp_potencia, y_registado_cmp1_potencia, button='left', clicks=1, interval=0.25)
                            time.sleep(0.2)

                            keyboard.press_and_release('2')
                            keyboard.press_and_release('.')
                            keyboard.press_and_release('2')
                            time.sleep(0.2)
                            
                            pyautogui.click(x_propriedade, y_propriedade, button='left', clicks=2, interval=0.25)
                            time.sleep(0.2)
                            
                            keyboard.press_and_release('backspace')
                            time.sleep(0.2) 

                            keyboard.press_and_release('1')
                            keyboard.press_and_release('7')
                            keyboard.press_and_release('2')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            pyautogui.click(x_gis_x, y_gis_x, button='left', clicks=2, interval=0.25)
                            time.sleep(0.2)
                            
                            keyboard.press_and_release('backspace')
                            time.sleep(0.2)

                            keyboard.press_and_release('2')
                            time.sleep(0.2)

                            pyautogui.click(x_gis_y, y_gis_y, button='left', clicks=2, interval=0.25)
                            time.sleep(0.2)
                            
                            keyboard.press_and_release('backspace')
                            time.sleep(0.2)
                            
                            keyboard.press_and_release('1')
                            time.sleep(0.2)

                            
                            pyautogui.click(x_estado_instalacao, y_estado_instalacao, button='left', clicks=1, interval=0.25)
                            time.sleep(0.2) 

                            keyboard.press_and_release('s')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('s')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('s')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('s')
                            time.sleep(0.2)
                        
                            pyautogui.click(x_num_luz, y_num_luz , button='left', clicks=1, interval=0.25)
                            time.sleep(0.2) 

                            keyboard.press_and_release('8')
                            time.sleep(1)

                            pyautogui.click(x_quartos, y_quartos, button='left', clicks=1, interval=0.25)
                            time.sleep(0.2) 

                            keyboard.press_and_release('4')
                            time.sleep(0.2)
                            

                            pyautogui.click(x_registro, y_registro, button='left', clicks=1, interval=0.25)
                            time.sleep(0.2) 

                            keyboard.press_and_release('space')
                            keyboard.press_and_release('space')
                            keyboard.press_and_release('space')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('n')
                            time.sleep(0.2)
                            

                            pyautogui.click( x_registado_sim, y_registado_sim, button='left', clicks=1, interval=0.25)
                            time.sleep(0.2) 

                            keyboard.press_and_release('space')
                            keyboard.press_and_release('space')
                            keyboard.press_and_release('space')
                            time.sleep(0.2)
                            
                            pyautogui.click(x_anterior, y_anterior, button='left', clicks=3, interval=0.25)
                            time.sleep(0.1)
                        

                    elif 'em processamento' in linha.lower():
                        print(f"Linha encontrada (Em processamento): {linha}")
                        # print(f"Linha encontrada (Em Processamento): {linha}")
                        encontrou_linha = True
                        contador_em_processamento += 1

                        match = re.match(r'^\d+', linha)
                        if match:
                            ot = match.group()
                            print(f"OT encontrado: {ot}")

                            altura_linha = 20  # Ajuste conforme necessário para a altura da linha real
                            y_pos = area[1] + (i * altura_linha) + 5
                            x_pos = area[0] + 30

                            pyautogui.moveTo(x_pos, y_pos)
                            pyautogui.click()

                            pyautogui.click(x_seguinte, y_seguinte, button='left', clicks=2, interval=0.25)
                            time.sleep(1)

                            pyautogui.click(x_registado, y_registado, button='left', clicks=2, interval=0.25)
                            time.sleep(1)

                            pyautogui.click(x_processamento_seguinte, y_processamento_seguinte, button='left', clicks=1, interval=0.25)
                            time.sleep(1)

                            pyautogui.click(x_registado_cmp1, y_registado_cmp1, button='left', clicks=1, interval=0.25)
                            time.sleep(1)

                            keyboard.press_and_release('r')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('v')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('2')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('2')
                            time.sleep(0.2)

                            keyboard.press_and_release('shift+tab')
                            time.sleep(2)

                            screenshot = pyautogui.screenshot(region=area2)
                            texto_extraido = pytesseract.image_to_string(screenshot)
                            
                            texto_extraido = texto_extraido.strip()  # Remove espaços no início e no fim
                            texto_extraido = texto_extraido.replace("\n", "")  # Remove quebras de linha

                            # Mostrar o texto extraído para depuração
                            print("Texto extraído:\n", texto_extraido)

                            # Comparar o texto
                            if texto_extraido == "22000 V":
                                keyboard.press_and_release('tab')
                                time.sleep(0.2)
                                keyboard.press_and_release('2')
                                time.sleep(0.2)
                                
                            else:
                                keyboard.press_and_release('tab')
                                time.sleep(0.2)
                                
                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('s')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('s')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('r')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('2')
                            keyboard.press_and_release('0')
                            keyboard.press_and_release('0')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('4')
                            keyboard.press_and_release('3')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('4')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('2')
                            keyboard.press_and_release('0')
                            keyboard.press_and_release('0')
                            time.sleep(1)
                            
                            pyautogui.click(x_registado_cmp_potencia, y_registado_cmp1_potencia, button='left', clicks=1, interval=0.25)
                            time.sleep(0.2)

                            keyboard.press_and_release('2')
                            keyboard.press_and_release('.')
                            keyboard.press_and_release('2')
                            time.sleep(0.2)
                            
                            pyautogui.click(x_propriedade, y_propriedade, button='left', clicks=2, interval=0.25)
                            time.sleep(0.2)
                            
                            keyboard.press_and_release('backspace')
                            time.sleep(0.2)

                            keyboard.press_and_release('1')
                            keyboard.press_and_release('7')
                            keyboard.press_and_release('2')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            pyautogui.click(x_gis_x, y_gis_x, button='left', clicks=2, interval=0.25)
                            time.sleep(0.2)
                            
                            keyboard.press_and_release('backspace')
                            time.sleep(0.2)

                            keyboard.press_and_release('2')
                            time.sleep(0.2)

                            pyautogui.click(x_gis_y, y_gis_y, button='left', clicks=2, interval=0.25)
                            time.sleep(0.2)
                            
                            keyboard.press_and_release('backspace')
                            time.sleep(0.2)
                            
                            keyboard.press_and_release('1')
                            time.sleep(0.2)

                            pyautogui.click(x_estado_instalacao, y_estado_instalacao, button='left', clicks=1, interval=0.25)
                            time.sleep(0.2) 

                            keyboard.press_and_release('s')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('s')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('s')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('s')
                            time.sleep(0.2)

                            pyautogui.click(x_num_luz, y_num_luz, button='left', clicks=1, interval=0.25)
                            time.sleep(0.2) 

                            keyboard.press_and_release('8')
                            time.sleep(1)

                            pyautogui.click(x_quartos, y_quartos, button='left', clicks=1, interval=0.25)
                            time.sleep(0.2) 

                            keyboard.press_and_release('4')
                            time.sleep(0.2)

                            pyautogui.click(x_registro, y_registro, button='left', clicks=1, interval=0.25)
                            time.sleep(0.2) 

                            keyboard.press_and_release('space')
                            keyboard.press_and_release('space')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('n')
                            time.sleep(0.2)

                            pyautogui.click(x_registado_sim, y_registado_sim, button='left', clicks=1, interval=0.25)
                            time.sleep(0.2) 

                            keyboard.press_and_release('space')
                            keyboard.press_and_release('space')
                            time.sleep(0.2)

                            pyautogui.click(x_anterior, y_anterior, button='left', clicks=3, interval=0.25)
                            time.sleep(0.1)
                
                if not encontrou_linha:
                    contador_introduzido += 1
                    print("estou aqui")
                # print("Nenhuma linha correspondente encontrada. Pressionando Ctrl + I.")
                    keyboard.press_and_release('ctrl+i')
                    time.sleep(2)
                    keyboard.press_and_release('tab')
                    for _ in range(3):
                        keyboard.press_and_release('i')
                        time.sleep(1)
                    for _ in range(3):    
                        keyboard.press_and_release('tab')
                    keyboard.write('rede perda')
                    
                    pyautogui.click(x_seguinte, y_seguinte, button='left', clicks=2, interval=0.25)
                    time.sleep(1)
                    
                    for _ in range(4):    
                        keyboard.press_and_release('space')
                    time.sleep(1)


                    pyautogui.click(x_processamento,y_processamento, button='left', clicks=2, interval=0.25)
                    time.sleep(1)

                    pyautogui.click(x_processamento_seguinte, y_processamento_seguinte, button='left', clicks=1, interval=0.25)
                    time.sleep(1)

                    pyautogui.click(x_imprimir, y_imprimir, button='left', clicks=1, interval=0.25)
                    time.sleep(0.5)

                    pyautogui.click( x_processamento_sim, y_processamento_sim, button='left', clicks=1, interval=0.25)
                    time.sleep(0.5)

                    pyautogui.click(x_registado, y_registado, button='left', clicks=2, interval=0.25)
                    time.sleep(1)

                    pyautogui.click(x_registado_seguinte, y_registado_seguinte, button='left', clicks=1, interval=0.25)
                    time.sleep(1)

                    pyautogui.click(x_registado_cmp1, y_registado_cmp1 , button='left', clicks=1, interval=0.25)
                    time.sleep(1)

                    keyboard.press_and_release('r')
                    time.sleep(0.2)

                    keyboard.press_and_release('tab')
                    time.sleep(0.2)

                    keyboard.press_and_release('v')
                    time.sleep(0.2)

                    keyboard.press_and_release('tab')
                    time.sleep(0.2)

                    keyboard.press_and_release('2')
                    time.sleep(0.2)

                    keyboard.press_and_release('tab')
                    time.sleep(0.2)

                    keyboard.press_and_release('2')
                    time.sleep(0.2)

                    keyboard.press_and_release('shift+tab')
                    time.sleep(2)

                    screenshot = pyautogui.screenshot(region=area2)
                    texto_extraido = pytesseract.image_to_string(screenshot)
                    
                    texto_extraido = texto_extraido.strip()  # Remove espaços no início e no fim
                    texto_extraido = texto_extraido.replace("\n", "")  # Remove quebras de linha

                    # Mostrar o texto extraído para depuração
                    print("Texto extraído:\n", texto_extraido)

                    # Comparar o texto
                    if texto_extraido == "22000 V":
                        keyboard.press_and_release('tab')
                        time.sleep(0.2)
                        keyboard.press_and_release('2')
                        time.sleep(0.2)
                        
                    else:
                        keyboard.press_and_release('tab')
                        time.sleep(0.2)
                        
                    keyboard.press_and_release('tab')
                    time.sleep(0.2)
                    keyboard.press_and_release('s')
                    time.sleep(0.2)

                    keyboard.press_and_release('tab')
                    time.sleep(0.2)

                    keyboard.press_and_release('s')
                    time.sleep(0.2)

                    keyboard.press_and_release('tab')
                    time.sleep(0.2)

                    keyboard.press_and_release('r')
                    time.sleep(0.2)

                    keyboard.press_and_release('tab')
                    time.sleep(0.2)

                    keyboard.press_and_release('2')
                    keyboard.press_and_release('0')
                    keyboard.press_and_release('0')
                    time.sleep(0.2)

                    keyboard.press_and_release('tab')
                    time.sleep(0.2)

                    keyboard.press_and_release('4')
                    keyboard.press_and_release('3')
                    time.sleep(0.2)

                    keyboard.press_and_release('tab')
                    time.sleep(0.2)

                    keyboard.press_and_release('4')
                    time.sleep(0.2)

                    keyboard.press_and_release('tab')
                    time.sleep(0.2)

                    keyboard.press_and_release('2')
                    keyboard.press_and_release('0')
                    keyboard.press_and_release('0')
                    time.sleep(1)
                    
                    pyautogui.click(x_registado_cmp_potencia, y_registado_cmp1_potencia, button='left', clicks=1, interval=0.25)
                    time.sleep(0.2)

                    keyboard.press_and_release('2')
                    keyboard.press_and_release('.')
                    keyboard.press_and_release('2')
                    time.sleep(0.2)
                    
                    pyautogui.click(x_propriedade, y_propriedade, button='left', clicks=2, interval=0.25)
                    time.sleep(0.2)
                    
                    keyboard.press_and_release('backspace')
                    time.sleep(0.2) 

                    keyboard.press_and_release('1')
                    keyboard.press_and_release('7')
                    keyboard.press_and_release('2')
                    time.sleep(0.2)

                    keyboard.press_and_release('tab')
                    time.sleep(0.2)

                    pyautogui.click(x_gis_x, y_gis_x, button='left', clicks=2, interval=0.25)
                    time.sleep(0.2)
                    
                    keyboard.press_and_release('backspace')
                    time.sleep(0.2)

                    keyboard.press_and_release('2')
                    time.sleep(0.2)

                    pyautogui.click(x_gis_y, y_gis_y, button='left', clicks=2, interval=0.25)
                    time.sleep(0.2)
                    
                    keyboard.press_and_release('backspace')
                    time.sleep(0.2)
                    
                    keyboard.press_and_release('1')
                    time.sleep(0.2)

                    
                    pyautogui.click(x_estado_instalacao, y_estado_instalacao, button='left', clicks=1, interval=0.25)
                    time.sleep(0.2) 

                    keyboard.press_and_release('s')
                    time.sleep(0.2)

                    keyboard.press_and_release('tab')
                    time.sleep(0.2)

                    keyboard.press_and_release('s')
                    time.sleep(0.2)

                    keyboard.press_and_release('tab')
                    time.sleep(0.2)

                    keyboard.press_and_release('s')
                    time.sleep(0.2)

                    keyboard.press_and_release('tab')
                    time.sleep(0.2)

                    keyboard.press_and_release('s')
                    time.sleep(0.2)
                
                    pyautogui.click(x_num_luz, y_num_luz , button='left', clicks=1, interval=0.25)
                    time.sleep(0.2) 

                    keyboard.press_and_release('8')
                    time.sleep(1)

                    pyautogui.click(x_quartos, y_quartos, button='left', clicks=1, interval=0.25)
                    time.sleep(0.2) 

                    keyboard.press_and_release('4')
                    time.sleep(0.2)
                    

                    pyautogui.click(x_registro, y_registro, button='left', clicks=1, interval=0.25)
                    time.sleep(0.2) 

                    keyboard.press_and_release('space')
                    keyboard.press_and_release('space')
                    keyboard.press_and_release('space')
                    time.sleep(0.2)

                    keyboard.press_and_release('tab')
                    time.sleep(0.2)

                    keyboard.press_and_release('n')
                    time.sleep(0.2)
                    

                    pyautogui.click( x_registado_sim, y_registado_sim, button='left', clicks=1, interval=0.25)
                    time.sleep(0.2) 

                    keyboard.press_and_release('space')
                    keyboard.press_and_release('space')
                    keyboard.press_and_release('space')
                    time.sleep(0.2)
                    
                    pyautogui.click(x_anterior, y_anterior, button='left', clicks=3, interval=0.25)
                    time.sleep(0.1)           


        else:
            if len(linhas) % 3 == 0:
                if len(linhas) == 3:
        # Caso especial: se há exatamente 3 linhas, não combinar, apenas exibir
                    print("\nLinhas (3 linhas detectadas):")
                    for linha in linhas:
                        print(linha)
                    
                    encontrou_linha = False

                    for i, linha in enumerate(linhas):
                        if 'suspeita de fraude' in linha.lower():
                            if 'Registado' in linha.lower():
                                print(f"Linha encontrada (Registado): {linha}")
                                encontrou_linha = True
                                contador_registados +=1

                                # Extrair o número da O.T. usando regex (números no início da linha)
                                match = re.match(r'\d+', linha)
                                if match:
                                    ot = match.group()
                                    print(f"Número da O.T.: {ot}")

                                    # Calcular a posição Y para o clique
                                    altura_linha = 20  # Ajuste conforme necessário para a altura da linha real
                                    y_pos = area[1] + (i * altura_linha) + 5
                                    x_pos = area[0] + 30  # Ajuste conforme necessário para a primeira coluna

                                    # Mover o mouse para a posição da linha específica e clicar
                                    pyautogui.moveTo(x_pos, y_pos)
                                    pyautogui.click()

                                    pyautogui.click(x_seguinte, y_seguinte, button='left', clicks=2, interval=0.25)
                                    time.sleep(1)

                                    pyautogui.click(x_processamento,y_processamento, button='left', clicks=2, interval=0.25)
                                    time.sleep(1)

                                    pyautogui.click(x_processamento_seguinte, y_processamento_seguinte, button='left', clicks=1, interval=0.25)
                                    time.sleep(1)

                                    pyautogui.click(x_imprimir, y_imprimir, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.5)

                                    pyautogui.click( x_processamento_sim, y_processamento_sim, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.5)

                                    pyautogui.click(x_registro, y_registro, button='left', clicks=2, interval=0.25)
                                    time.sleep(1)

                                    pyautogui.click(x_registado_seguinte, y_registado_seguinte, button='left', clicks=1, interval=0.25)
                                    time.sleep(1)

                                    pyautogui.click(x_registado_cmp1, y_registado_cmp1 , button='left', clicks=1, interval=0.25)
                                    time.sleep(1)

                                    keyboard.press_and_release('r')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('v')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('2')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('2')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('shift+tab')
                                    time.sleep(2)

                                    screenshot = pyautogui.screenshot(region=area2)
                                    texto_extraido = pytesseract.image_to_string(screenshot)
                                    
                                    texto_extraido = texto_extraido.strip()  # Remove espaços no início e no fim
                                    texto_extraido = texto_extraido.replace("\n", "")  # Remove quebras de linha

                                    # Mostrar o texto extraído para depuração
                                    print("Texto extraído:\n", texto_extraido)

                                    # Comparar o texto
                                    if texto_extraido == "22000 V":
                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)
                                        keyboard.press_and_release('2')
                                        time.sleep(0.2)
                                        
                                    else:
                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)
                                        
                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)
                                    keyboard.press_and_release('s')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('s')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('r')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('2')
                                    keyboard.press_and_release('0')
                                    keyboard.press_and_release('0')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('4')
                                    keyboard.press_and_release('3')
                                    time.sleep(0.2)
                
                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('4')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('2')
                                    keyboard.press_and_release('0')
                                    keyboard.press_and_release('0')
                                    time.sleep(1)
                                    
                                    pyautogui.click(x_registado_cmp_potencia, y_registado_cmp1_potencia, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.2)

                                    keyboard.press_and_release('2')
                                    keyboard.press_and_release('.')
                                    keyboard.press_and_release('2')
                                    time.sleep(0.2)
                                    
                                    pyautogui.click(x_propriedade, y_propriedade, button='left', clicks=2, interval=0.25)
                                    time.sleep(0.2)
                                    
                                    keyboard.press_and_release('backspace')
                                    time.sleep(0.2) 

                                    keyboard.press_and_release('1')
                                    keyboard.press_and_release('7')
                                    keyboard.press_and_release('2')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    pyautogui.click(x_gis_x, y_gis_x, button='left', clicks=2, interval=0.25)
                                    time.sleep(0.2)
                                    
                                    keyboard.press_and_release('backspace')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('2')
                                    time.sleep(0.2)

                                    pyautogui.click(x_gis_y, y_gis_y, button='left', clicks=2, interval=0.25)
                                    time.sleep(0.2)
                                    
                                    keyboard.press_and_release('backspace')
                                    time.sleep(0.2)
                                    
                                    keyboard.press_and_release('1')
                                    time.sleep(0.2)

                                    
                                    pyautogui.click(x_estado_instalacao, y_estado_instalacao, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.2) 

                                    keyboard.press_and_release('s')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('s')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('s')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('s')
                                    time.sleep(0.2)
                                
                                    pyautogui.click(x_num_luz, y_num_luz , button='left', clicks=1, interval=0.25)
                                    time.sleep(0.2) 

                                    keyboard.press_and_release('8')
                                    time.sleep(1)

                                    pyautogui.click(x_quartos, y_quartos, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.2) 

                                    keyboard.press_and_release('4')
                                    time.sleep(0.2)
                                    

                                    pyautogui.click(x_registro, y_registro, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.2) 

                                    keyboard.press_and_release('space')
                                    keyboard.press_and_release('space')
                                    keyboard.press_and_release('space')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('n')
                                    time.sleep(0.2)
                                    

                                    pyautogui.click( x_registado_sim, y_registado_sim, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.2) 

                                    keyboard.press_and_release('space')
                                    keyboard.press_and_release('space')
                                    keyboard.press_and_release('space')
                                    time.sleep(0.2)
                                    
                                    pyautogui.click(x_anterior, y_anterior, button='left', clicks=3, interval=0.25)
                                    time.sleep(0.1)

                                    
                            elif 'em processamento' in linha.lower():
                            # print(f"Linha encontrada (Em Processamento): {linha}")
                                encontrou_linha = True
                                contador_em_processamento += 1

                                match = re.match(r'\d+', linha)
                                if match:
                                    ot = match.group()
                                    print(f"Número da O.T.: {ot}")

                                    # Calcular a posição Y para o clique
                                    altura_linha = 20  # Ajuste conforme necessário para a altura da linha real
                                    y_pos = area[1] + (i * altura_linha) + 5
                                    x_pos = area[0] + 30  # Ajuste conforme necessário para a primeira coluna

                                    # Mover o mouse para a posição da linha específica e clicar
                                    pyautogui.moveTo(x_pos, y_pos)
                                    pyautogui.click()

                                    pyautogui.click(x_seguinte, y_seguinte, button='left', clicks=2, interval=0.25)
                                    time.sleep(1)

                                    pyautogui.click(x_registado, y_registado, button='left', clicks=2, interval=0.25)
                                    time.sleep(1)

                                    pyautogui.click(x_processamento_seguinte, y_processamento_seguinte, button='left', clicks=1, interval=0.25)
                                    time.sleep(1)

                                    pyautogui.click(x_registado_cmp1, y_registado_cmp1, button='left', clicks=1, interval=0.25)
                                    time.sleep(1)

                                    keyboard.press_and_release('r')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('v')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('2')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('2')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('shift+tab')
                                    time.sleep(2)

                                    screenshot = pyautogui.screenshot(region=area2)
                                    texto_extraido = pytesseract.image_to_string(screenshot)
                                    
                                    texto_extraido = texto_extraido.strip()  # Remove espaços no início e no fim
                                    texto_extraido = texto_extraido.replace("\n", "")  # Remove quebras de linha

                                    # Mostrar o texto extraído para depuração
                                    print("Texto extraído:\n", texto_extraido)

                                    # Comparar o texto
                                    if texto_extraido == "22000 V":
                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)
                                        keyboard.press_and_release('2')
                                        time.sleep(0.2)
                                        
                                    else:
                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)
                                        
                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('s')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('s')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('r')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('2')
                                    keyboard.press_and_release('0')
                                    keyboard.press_and_release('0')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('4')
                                    keyboard.press_and_release('3')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('4')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('2')
                                    keyboard.press_and_release('0')
                                    keyboard.press_and_release('0')
                                    time.sleep(1)
                                    
                                    pyautogui.click(x_registado_cmp_potencia, y_registado_cmp1_potencia, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.2)

                                    keyboard.press_and_release('2')
                                    keyboard.press_and_release('.')
                                    keyboard.press_and_release('2')
                                    time.sleep(0.2)
                                    
                                    pyautogui.click(x_propriedade, y_propriedade, button='left', clicks=2, interval=0.25)
                                    time.sleep(0.2)
                                    
                                    keyboard.press_and_release('backspace')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('1')
                                    keyboard.press_and_release('7')
                                    keyboard.press_and_release('2')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    pyautogui.click(x_gis_x, y_gis_x, button='left', clicks=2, interval=0.25)
                                    time.sleep(0.2)
                                    
                                    keyboard.press_and_release('backspace')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('2')
                                    time.sleep(0.2)

                                    pyautogui.click(x_gis_y, y_gis_y, button='left', clicks=2, interval=0.25)
                                    time.sleep(0.2)
                                    
                                    keyboard.press_and_release('backspace')
                                    time.sleep(0.2)
                                    
                                    keyboard.press_and_release('1')
                                    time.sleep(0.2)

                                    pyautogui.click(x_estado_instalacao, y_estado_instalacao, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.2) 

                                    keyboard.press_and_release('s')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('s')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('s')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('s')
                                    time.sleep(0.2)

                                    pyautogui.click(x_num_luz, y_num_luz, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.2) 

                                    keyboard.press_and_release('8')
                                    time.sleep(1)

                                    pyautogui.click(x_quartos, y_quartos, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.2) 

                                    keyboard.press_and_release('4')
                                    time.sleep(0.2)

                                    pyautogui.click(x_registro, y_registro, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.2) 

                                    keyboard.press_and_release('space')
                                    keyboard.press_and_release('space')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('n')
                                    time.sleep(0.2)

                                    pyautogui.click(x_registado_sim, y_registado_sim, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.2) 

                                    keyboard.press_and_release('space')
                                    keyboard.press_and_release('space')
                                    time.sleep(0.2)

                                    pyautogui.click(x_anterior, y_anterior, button='left', clicks=3, interval=0.25)
                                    time.sleep(0.1)
                

                    if not encontrou_linha:
                        contador_introduzido += 1
                        print("introducao com 3 linhas apenas")
                    # print("Nenhuma linha correspondente encontrada. Pressionando Ctrl + I.")
                        keyboard.press_and_release('ctrl+i')
                        time.sleep(2)
                        keyboard.press_and_release('tab')
                        for _ in range(3):
                            keyboard.press_and_release('i')
                            time.sleep(1)
                        for _ in range(3):    
                            keyboard.press_and_release('tab')
                        keyboard.write('rede perda')
                        
                        pyautogui.click(x_seguinte, y_seguinte, button='left', clicks=2, interval=0.25)
                        time.sleep(1)
                        
                        for _ in range(4):    
                            keyboard.press_and_release('space')
                        time.sleep(1)

                        pyautogui.click(x_processamento,y_processamento, button='left', clicks=2, interval=0.25)
                        time.sleep(1)

                        pyautogui.click(x_processamento_seguinte, y_processamento_seguinte, button='left', clicks=1, interval=0.25)
                        time.sleep(1)

                        pyautogui.click(x_imprimir, y_imprimir, button='left', clicks=1, interval=0.25)
                        time.sleep(0.5)

                        pyautogui.click( x_processamento_sim, y_processamento_sim, button='left', clicks=1, interval=0.25)
                        time.sleep(0.5)

                        pyautogui.click(x_registado, y_registado, button='left', clicks=2, interval=0.25)
                        time.sleep(1)

                        pyautogui.click(x_registado_seguinte, y_registado_seguinte, button='left', clicks=1, interval=0.25)
                        time.sleep(1)

                        pyautogui.click(x_registado_cmp1, y_registado_cmp1 , button='left', clicks=1, interval=0.25)
                        time.sleep(1)

                        keyboard.press_and_release('r')
                        time.sleep(0.2)

                        keyboard.press_and_release('tab')
                        time.sleep(0.2)

                        keyboard.press_and_release('v')
                        time.sleep(0.2)

                        keyboard.press_and_release('tab')
                        time.sleep(0.2)

                        keyboard.press_and_release('2')
                        time.sleep(0.2)

                        keyboard.press_and_release('tab')
                        time.sleep(0.2)

                        keyboard.press_and_release('2')
                        time.sleep(0.2)

                        keyboard.press_and_release('shift+tab')
                        time.sleep(2)

                        screenshot = pyautogui.screenshot(region=area2)
                        texto_extraido = pytesseract.image_to_string(screenshot)
                        
                        texto_extraido = texto_extraido.strip()  # Remove espaços no início e no fim
                        texto_extraido = texto_extraido.replace("\n", "")  # Remove quebras de linha

                        # Mostrar o texto extraído para depuração
                        print("Texto extraído:\n", texto_extraido)

                        # Comparar o texto
                        if texto_extraido == "22000 V":
                            keyboard.press_and_release('tab')
                            time.sleep(0.2)
                            keyboard.press_and_release('2')
                            time.sleep(0.2)
                            
                        else:
                            keyboard.press_and_release('tab')
                            time.sleep(0.2)
                            
                        keyboard.press_and_release('tab')
                        time.sleep(0.2)
                        keyboard.press_and_release('s')
                        time.sleep(0.2)

                        keyboard.press_and_release('tab')
                        time.sleep(0.2)

                        keyboard.press_and_release('s')
                        time.sleep(0.2)

                        keyboard.press_and_release('tab')
                        time.sleep(0.2)

                        keyboard.press_and_release('r')
                        time.sleep(0.2)

                        keyboard.press_and_release('tab')
                        time.sleep(0.2)

                        keyboard.press_and_release('2')
                        keyboard.press_and_release('0')
                        keyboard.press_and_release('0')
                        time.sleep(0.2)

                        keyboard.press_and_release('tab')
                        time.sleep(0.2)

                        keyboard.press_and_release('4')
                        keyboard.press_and_release('3')
                        time.sleep(0.2)
    
                        keyboard.press_and_release('tab')
                        time.sleep(0.2)

                        keyboard.press_and_release('4')
                        time.sleep(0.2)

                        keyboard.press_and_release('tab')
                        time.sleep(0.2)

                        keyboard.press_and_release('2')
                        keyboard.press_and_release('0')
                        keyboard.press_and_release('0')
                        time.sleep(1)
                        
                        pyautogui.click(x_registado_cmp_potencia, y_registado_cmp1_potencia, button='left', clicks=1, interval=0.25)
                        time.sleep(0.2)

                        keyboard.press_and_release('2')
                        keyboard.press_and_release('.')
                        keyboard.press_and_release('2')
                        time.sleep(0.2)
                        
                        pyautogui.click(x_propriedade, y_propriedade, button='left', clicks=2, interval=0.25)
                        time.sleep(0.2)
                        
                        keyboard.press_and_release('backspace')
                        time.sleep(0.2) 

                        keyboard.press_and_release('1')
                        keyboard.press_and_release('7')
                        keyboard.press_and_release('2')
                        time.sleep(0.2)

                        keyboard.press_and_release('tab')
                        time.sleep(0.2)

                        pyautogui.click(x_gis_x, y_gis_x, button='left', clicks=2, interval=0.25)
                        time.sleep(0.2)
                        
                        keyboard.press_and_release('backspace')
                        time.sleep(0.2)

                        keyboard.press_and_release('2')
                        time.sleep(0.2)

                        pyautogui.click(x_gis_y, y_gis_y, button='left', clicks=2, interval=0.25)
                        time.sleep(0.2)
                        
                        keyboard.press_and_release('backspace')
                        time.sleep(0.2)
                        
                        keyboard.press_and_release('1')
                        time.sleep(0.2)

                        
                        pyautogui.click(x_estado_instalacao, y_estado_instalacao, button='left', clicks=1, interval=0.25)
                        time.sleep(0.2) 

                        keyboard.press_and_release('s')
                        time.sleep(0.2)

                        keyboard.press_and_release('tab')
                        time.sleep(0.2)

                        keyboard.press_and_release('s')
                        time.sleep(0.2)

                        keyboard.press_and_release('tab')
                        time.sleep(0.2)

                        keyboard.press_and_release('s')
                        time.sleep(0.2)

                        keyboard.press_and_release('tab')
                        time.sleep(0.2)

                        keyboard.press_and_release('s')
                        time.sleep(0.2)
                    
                        pyautogui.click(x_num_luz, y_num_luz , button='left', clicks=1, interval=0.25)
                        time.sleep(0.2) 

                        keyboard.press_and_release('8')
                        time.sleep(1)

                        pyautogui.click(x_quartos, y_quartos, button='left', clicks=1, interval=0.25)
                        time.sleep(0.2) 

                        keyboard.press_and_release('4')
                        time.sleep(0.2)
                        

                        pyautogui.click(x_registro, y_registro, button='left', clicks=1, interval=0.25)
                        time.sleep(0.2) 

                        keyboard.press_and_release('space')
                        keyboard.press_and_release('space')
                        keyboard.press_and_release('space')
                        time.sleep(0.2)

                        keyboard.press_and_release('tab')
                        time.sleep(0.2)

                        keyboard.press_and_release('n')
                        time.sleep(0.2)
                        

                        pyautogui.click( x_registado_sim, y_registado_sim, button='left', clicks=1, interval=0.25)
                        time.sleep(0.2) 

                        keyboard.press_and_release('space')
                        keyboard.press_and_release('space')
                        keyboard.press_and_release('space')
                        time.sleep(0.2)
                        
                        pyautogui.click(x_anterior, y_anterior, button='left', clicks=3, interval=0.25)
                        time.sleep(0.1)
                        continue           
                else: 
                    
                    total_grupos = len(linhas) // 3
                    tipos = linhas[:total_grupos]
                    estados = linhas[total_grupos:2 * total_grupos]
                    centros = linhas[2 * total_grupos:]

                    # Combinar os dados correspondentes
                    linhas_combinadas = []
                    for i in range(total_grupos):
                        linha_completa = f"{tipos[i]} {estados[i]} {centros[i]}"
                        linhas_combinadas.append(linha_completa)

                    # Mostrar as linhas combinadas
                    print("\nLinhas Combinadas:")
                    for linha in linhas_combinadas:
                        print(linha)

                    # Definir os comportamentos baseados em palavras-chave
                    encontrou_linha = False

                    for i, linha in enumerate(linhas_combinadas):
                        if 'suspeita de fraude' in linha.lower():
                            if 'Registado' in linha.lower():
                                print(f"Linha encontrada (Registado): {linha}")
                                encontrou_linha = True
                                contador_registados +=1

                                # Extrair o número da O.T. usando regex (números no início da linha)
                                match = re.match(r'\d+', linha)
                                if match:
                                    ot = match.group()
                                    print(f"Número da O.T.: {ot}")

                                    # Calcular a posição Y para o clique
                                    altura_linha = 20  # Ajuste conforme necessário para a altura da linha real
                                    y_pos = area[1] + (i * altura_linha) + 5
                                    x_pos = area[0] + 30  # Ajuste conforme necessário para a primeira coluna

                                    # Mover o mouse para a posição da linha específica e clicar
                                    pyautogui.moveTo(x_pos, y_pos)
                                    pyautogui.click()
                                    print(f"Mouse movido e clique realizado na linha com O.T.: {ot}")

                                    pyautogui.click(x_seguinte, y_seguinte, button='left', clicks=2, interval=0.25)
                                    time.sleep(1)

                                    pyautogui.click(x_processamento,y_processamento, button='left', clicks=2, interval=0.25)
                                    time.sleep(1)

                                    pyautogui.click(x_processamento_seguinte, y_processamento_seguinte, button='left', clicks=1, interval=0.25)
                                    time.sleep(1)

                                    pyautogui.click(x_imprimir, y_imprimir, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.5)

                                    pyautogui.click( x_processamento_sim, y_processamento_sim, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.5)

                                    pyautogui.click(x_registro, y_registro, button='left', clicks=2, interval=0.25)
                                    time.sleep(1)

                                    pyautogui.click(x_registado_seguinte, y_registado_seguinte, button='left', clicks=1, interval=0.25)
                                    time.sleep(1)

                                    pyautogui.click(x_registado_cmp1, y_registado_cmp1 , button='left', clicks=1, interval=0.25)
                                    time.sleep(1)

                                    keyboard.press_and_release('r')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('v')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('2')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('2')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('shift+tab')
                                    time.sleep(2)

                                    screenshot = pyautogui.screenshot(region=area2)
                                    texto_extraido = pytesseract.image_to_string(screenshot)
                                    
                                    texto_extraido = texto_extraido.strip()  # Remove espaços no início e no fim
                                    texto_extraido = texto_extraido.replace("\n", "")  # Remove quebras de linha

                                    # Mostrar o texto extraído para depuração
                                    print("Texto extraído:\n", texto_extraido)

                                    # Comparar o texto
                                    if texto_extraido == "22000 V":
                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)
                                        keyboard.press_and_release('2')
                                        time.sleep(0.2)
                                        
                                    else:
                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)
                                        
                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)
                                    keyboard.press_and_release('s')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('s')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('r')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('2')
                                    keyboard.press_and_release('0')
                                    keyboard.press_and_release('0')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('4')
                                    keyboard.press_and_release('3')
                                    time.sleep(0.2)
                
                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('4')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('2')
                                    keyboard.press_and_release('0')
                                    keyboard.press_and_release('0')
                                    time.sleep(1)
                                    
                                    pyautogui.click(x_registado_cmp_potencia, y_registado_cmp1_potencia, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.2)

                                    keyboard.press_and_release('2')
                                    keyboard.press_and_release('.')
                                    keyboard.press_and_release('2')
                                    time.sleep(0.2)
                                    
                                    pyautogui.click(x_propriedade, y_propriedade, button='left', clicks=2, interval=0.25)
                                    time.sleep(0.2)
                                    
                                    keyboard.press_and_release('backspace')
                                    time.sleep(0.2) 

                                    keyboard.press_and_release('1')
                                    keyboard.press_and_release('7')
                                    keyboard.press_and_release('2')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    pyautogui.click(x_gis_x, y_gis_x, button='left', clicks=2, interval=0.25)
                                    time.sleep(0.2)
                                    
                                    keyboard.press_and_release('backspace')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('2')
                                    time.sleep(0.2)

                                    pyautogui.click(x_gis_y, y_gis_y, button='left', clicks=2, interval=0.25)
                                    time.sleep(0.2)
                                    
                                    keyboard.press_and_release('backspace')
                                    time.sleep(0.2)
                                    
                                    keyboard.press_and_release('1')
                                    time.sleep(0.2)

                                    
                                    pyautogui.click(x_estado_instalacao, y_estado_instalacao, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.2) 

                                    keyboard.press_and_release('s')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('s')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('s')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('s')
                                    time.sleep(0.2)
                                
                                    pyautogui.click(x_num_luz, y_num_luz , button='left', clicks=1, interval=0.25)
                                    time.sleep(0.2) 

                                    keyboard.press_and_release('8')
                                    time.sleep(1)

                                    pyautogui.click(x_quartos, y_quartos, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.2) 

                                    keyboard.press_and_release('4')
                                    time.sleep(0.2)
                                    

                                    pyautogui.click(x_registro, y_registro, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.2) 

                                    keyboard.press_and_release('space')
                                    keyboard.press_and_release('space')
                                    keyboard.press_and_release('space')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('n')
                                    time.sleep(0.2)
                                    

                                    pyautogui.click( x_registado_sim, y_registado_sim, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.2) 

                                    keyboard.press_and_release('space')
                                    keyboard.press_and_release('space')
                                    keyboard.press_and_release('space')
                                    time.sleep(0.2)
                                    
                                    pyautogui.click(x_anterior, y_anterior, button='left', clicks=3, interval=0.25)
                                    time.sleep(0.1)
                            


                        # Caso o estado seja "em processamento", retorna ao fluxo principal
                            elif 'em processamento' in linha.lower():
                                # print(f"Linha encontrada (Em Processamento): {linha}")
                                encontrou_linha = True
                                contador_em_processamento += 1

                                match = re.match(r'\d+', linha)
                                if match:
                                    ot = match.group()
                                    print(f"Número da O.T.: {ot}")

                                    # Calcular a posição Y para o clique
                                    altura_linha = 20  # Ajuste conforme necessário para a altura da linha real
                                    y_pos = area[1] + (i * altura_linha) + 5
                                    x_pos = area[0] + 30  # Ajuste conforme necessário para a primeira coluna

                                    # Mover o mouse para a posição da linha específica e clicar
                                    pyautogui.moveTo(x_pos, y_pos)
                                    pyautogui.click()

                                    pyautogui.click(x_seguinte, y_seguinte, button='left', clicks=2, interval=0.25)
                                    time.sleep(1)

                                    pyautogui.click(x_registado, y_registado, button='left', clicks=2, interval=0.25)
                                    time.sleep(1)

                                    pyautogui.click(x_processamento_seguinte, y_processamento_seguinte, button='left', clicks=1, interval=0.25)
                                    time.sleep(1)

                                    pyautogui.click(x_registado_cmp1, y_registado_cmp1, button='left', clicks=1, interval=0.25)
                                    time.sleep(1)

                                    keyboard.press_and_release('r')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('v')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('2')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('2')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('shift+tab')
                                    time.sleep(2)

                                    screenshot = pyautogui.screenshot(region=area2)
                                    texto_extraido = pytesseract.image_to_string(screenshot)
                                    
                                    texto_extraido = texto_extraido.strip()  # Remove espaços no início e no fim
                                    texto_extraido = texto_extraido.replace("\n", "")  # Remove quebras de linha

                                    # Mostrar o texto extraído para depuração
                                    print("Texto extraído:\n", texto_extraido)

                                    # Comparar o texto
                                    if texto_extraido == "22000 V":
                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)
                                        keyboard.press_and_release('2')
                                        time.sleep(0.2)
                                        
                                    else:
                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)
                                        
                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('s')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('s')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('r')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('2')
                                    keyboard.press_and_release('0')
                                    keyboard.press_and_release('0')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('4')
                                    keyboard.press_and_release('3')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('4')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('2')
                                    keyboard.press_and_release('0')
                                    keyboard.press_and_release('0')
                                    time.sleep(1)
                                    
                                    pyautogui.click(x_registado_cmp_potencia, y_registado_cmp1_potencia, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.2)

                                    keyboard.press_and_release('2')
                                    keyboard.press_and_release('.')
                                    keyboard.press_and_release('2')
                                    time.sleep(0.2)
                                    
                                    pyautogui.click(x_propriedade, y_propriedade, button='left', clicks=2, interval=0.25)
                                    time.sleep(0.2)
                                    
                                    keyboard.press_and_release('backspace')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('1')
                                    keyboard.press_and_release('7')
                                    keyboard.press_and_release('2')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    pyautogui.click(x_gis_x, y_gis_x, button='left', clicks=2, interval=0.25)
                                    time.sleep(0.2)
                                    
                                    keyboard.press_and_release('backspace')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('2')
                                    time.sleep(0.2)

                                    pyautogui.click(x_gis_y, y_gis_y, button='left', clicks=2, interval=0.25)
                                    time.sleep(0.2)
                                    
                                    keyboard.press_and_release('backspace')
                                    time.sleep(0.2)
                                    
                                    keyboard.press_and_release('1')
                                    time.sleep(0.2)

                                    pyautogui.click(x_estado_instalacao, y_estado_instalacao, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.2) 

                                    keyboard.press_and_release('s')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('s')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('s')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('s')
                                    time.sleep(0.2)

                                    pyautogui.click(x_num_luz, y_num_luz, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.2) 

                                    keyboard.press_and_release('8')
                                    time.sleep(1)

                                    pyautogui.click(x_quartos, y_quartos, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.2) 

                                    keyboard.press_and_release('4')
                                    time.sleep(0.2)

                                    pyautogui.click(x_registro, y_registro, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.2) 

                                    keyboard.press_and_release('space')
                                    keyboard.press_and_release('space')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.2)

                                    keyboard.press_and_release('n')
                                    time.sleep(0.2)

                                    pyautogui.click(x_registado_sim, y_registado_sim, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.2) 

                                    keyboard.press_and_release('space')
                                    keyboard.press_and_release('space')
                                    time.sleep(0.2)

                                    pyautogui.click(x_anterior, y_anterior, button='left', clicks=3, interval=0.25)
                                    time.sleep(0.1)
                

                                # print("Retornando ao código principal.")
                                    break

                # Se nenhuma linha correspondente for encontrada, pressionar Ctrl + I
                    if not encontrou_linha:
                        pyautogui.click(click_position)
                        time.sleep(0.1)

                        keyboard.press_and_release('page down')
                        time.sleep(0.5)
                        # print("Nenhuma linha correspondente encontrada. Pressionando Ctrl + I.")
                        screenshot = pyautogui.screenshot(region=area)

            # Usar o pytesseract para extrair texto da captura de tela
                        texto_extraido = pytesseract.image_to_string(screenshot)

                        # Mostrar o texto extraído (para depuração)
                        print("Texto extraído:\n", texto_extraido)

                        # Dividir o texto extraído em linhas, removendo espaços em branco extras
                        linhas = [linha.strip() for linha in texto_extraido.split('\n') if linha.strip()]
                    

                        total_grupos = len(linhas) // 3
                        tipos = linhas[:total_grupos]
                        estados = linhas[total_grupos:2 * total_grupos]
                        centros = linhas[2 * total_grupos:]

                        # Combinar os dados correspondentes
                        linhas_combinadas = []
                        for i in range(total_grupos):
                            linha_completa = f"{tipos[i]} {estados[i]} {centros[i]}"
                            linhas_combinadas.append(linha_completa)

                        # Mostrar as linhas combinadas
                        print("\nLinhas Combinadas:")
                        for linha in linhas_combinadas:
                            print(linha)

                        # Definir os comportamentos baseados em palavras-chave
                        encontrou_linha = False

                        for i, linha in enumerate(linhas_combinadas):
                            if 'suspeita de fraude' in linha.lower():
                                if 'Registado' in linha.lower():
                                    print(f"Linha encontrada (Registado): {linha}")
                                    encontrou_linha = True
                                    contador_registados +=1

                                    # Extrair o número da O.T. usando regex (números no início da linha)
                                    match = re.match(r'\d+', linha)
                                    if match:
                                        ot = match.group()
                                        print(f"Número da O.T.: {ot}")

                                        # Calcular a posição Y para o clique
                                        altura_linha = 20  # Ajuste conforme necessário para a altura da linha real
                                        y_pos = area[1] + (i * altura_linha) + 5
                                        x_pos = area[0] + 30  # Ajuste conforme necessário para a primeira coluna

                                        # Mover o mouse para a posição da linha específica e clicar
                                        pyautogui.moveTo(x_pos, y_pos)
                                        pyautogui.click()
                                        print(f"Mouse movido e clique realizado na linha com O.T.: {ot}")

                                        pyautogui.click(x_seguinte, y_seguinte, button='left', clicks=2, interval=0.25)
                                        time.sleep(1)

                                        pyautogui.click(x_processamento,y_processamento, button='left', clicks=2, interval=0.25)
                                        time.sleep(1)

                                        pyautogui.click(x_processamento_seguinte, y_processamento_seguinte, button='left', clicks=1, interval=0.25)
                                        time.sleep(1)

                                        pyautogui.click(x_imprimir, y_imprimir, button='left', clicks=1, interval=0.25)
                                        time.sleep(0.5)

                                        pyautogui.click( x_processamento_sim, y_processamento_sim, button='left', clicks=1, interval=0.25)
                                        time.sleep(0.5)

                                        pyautogui.click(x_registado, y_registado, button='left', clicks=2, interval=0.25)
                                        time.sleep(1)

                                        pyautogui.click(x_registado_seguinte, y_registado_seguinte, button='left', clicks=1, interval=0.25)
                                        time.sleep(1)

                                        pyautogui.click(x_registado_cmp1, y_registado_cmp1 , button='left', clicks=1, interval=0.25)
                                        time.sleep(1)

                                        keyboard.press_and_release('r')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('v')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('2')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('2')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('shift+tab')
                                        time.sleep(2)

                                        screenshot = pyautogui.screenshot(region=area2)
                                        texto_extraido = pytesseract.image_to_string(screenshot)
                                        
                                        texto_extraido = texto_extraido.strip()  # Remove espaços no início e no fim
                                        texto_extraido = texto_extraido.replace("\n", "")  # Remove quebras de linha

                                        # Mostrar o texto extraído para depuração
                                        print("Texto extraído:\n", texto_extraido)

                                        # Comparar o texto
                                        if texto_extraido == "22000 V":
                                            keyboard.press_and_release('tab')
                                            time.sleep(0.2)
                                            keyboard.press_and_release('2')
                                            time.sleep(0.2)
                                            
                                        else:
                                            keyboard.press_and_release('tab')
                                            time.sleep(0.2)
                                            
                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)
                                        keyboard.press_and_release('s')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('s')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('r')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('2')
                                        keyboard.press_and_release('0')
                                        keyboard.press_and_release('0')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('4')
                                        keyboard.press_and_release('3')
                                        time.sleep(0.2)
                    
                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('4')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('2')
                                        keyboard.press_and_release('0')
                                        keyboard.press_and_release('0')
                                        time.sleep(1)
                                        
                                        pyautogui.click(x_registado_cmp_potencia, y_registado_cmp1_potencia, button='left', clicks=1, interval=0.25)
                                        time.sleep(0.2)

                                        keyboard.press_and_release('2')
                                        keyboard.press_and_release('.')
                                        keyboard.press_and_release('2')
                                        time.sleep(0.2)
                                        
                                        pyautogui.click(x_propriedade, y_propriedade, button='left', clicks=2, interval=0.25)
                                        time.sleep(0.2)
                                        
                                        keyboard.press_and_release('backspace')
                                        time.sleep(0.2) 

                                        keyboard.press_and_release('1')
                                        keyboard.press_and_release('7')
                                        keyboard.press_and_release('2')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)

                                        pyautogui.click(x_gis_x, y_gis_x, button='left', clicks=2, interval=0.25)
                                        time.sleep(0.2)
                                        
                                        keyboard.press_and_release('backspace')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('2')
                                        time.sleep(0.2)

                                        pyautogui.click(x_gis_y, y_gis_y, button='left', clicks=2, interval=0.25)
                                        time.sleep(0.2)
                                        
                                        keyboard.press_and_release('backspace')
                                        time.sleep(0.2)
                                        
                                        keyboard.press_and_release('1')
                                        time.sleep(0.2)

                                        
                                        pyautogui.click(x_estado_instalacao, y_estado_instalacao, button='left', clicks=1, interval=0.25)
                                        time.sleep(0.2) 

                                        keyboard.press_and_release('s')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('s')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('s')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('s')
                                        time.sleep(0.2)
                                    
                                        pyautogui.click(x_num_luz, y_num_luz , button='left', clicks=1, interval=0.25)
                                        time.sleep(0.2) 

                                        keyboard.press_and_release('8')
                                        time.sleep(1)

                                        pyautogui.click(x_quartos, y_quartos, button='left', clicks=1, interval=0.25)
                                        time.sleep(0.2) 

                                        keyboard.press_and_release('4')
                                        time.sleep(0.2)
                                        

                                        pyautogui.click(x_registro, y_registro, button='left', clicks=1, interval=0.25)
                                        time.sleep(0.2) 

                                        keyboard.press_and_release('space')
                                        keyboard.press_and_release('space')
                                        keyboard.press_and_release('space')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('n')
                                        time.sleep(0.2)
                                        

                                        pyautogui.click( x_registado_sim, y_registado_sim, button='left', clicks=1, interval=0.25)
                                        time.sleep(0.2) 

                                        keyboard.press_and_release('space')
                                        keyboard.press_and_release('space')
                                        keyboard.press_and_release('space')
                                        time.sleep(0.2)
                                        
                                        pyautogui.click(x_anterior, y_anterior, button='left', clicks=3, interval=0.25)
                                        time.sleep(0.1)
                                


                            # Caso o estado seja "em processamento", retorna ao fluxo principal
                                elif 'em processamento' in linha.lower():
                                    # print(f"Linha encontrada (Em Processamento): {linha}")
                                    encontrou_linha = True
                                    contador_em_processamento += 1

                                    match = re.match(r'\d+', linha)
                                    if match:
                                        ot = match.group()
                                        print(f"Número da O.T.: {ot}")

                                        # Calcular a posição Y para o clique
                                        altura_linha = 20  # Ajuste conforme necessário para a altura da linha real
                                        y_pos = area[1] + (i * altura_linha) + 5
                                        x_pos = area[0] + 30  # Ajuste conforme necessário para a primeira coluna

                                        # Mover o mouse para a posição da linha específica e clicar
                                        pyautogui.moveTo(x_pos, y_pos)
                                        pyautogui.click()

                                        pyautogui.click(x_seguinte, y_seguinte, button='left', clicks=2, interval=0.25)
                                        time.sleep(1)

                                        pyautogui.click(x_registado, y_registado, button='left', clicks=2, interval=0.25)
                                        time.sleep(1)

                                        pyautogui.click(x_processamento_seguinte, y_processamento_seguinte, button='left', clicks=1, interval=0.25)
                                        time.sleep(1)

                                        pyautogui.click(x_registado_cmp1, y_registado_cmp1, button='left', clicks=1, interval=0.25)
                                        time.sleep(1)

                                        keyboard.press_and_release('r')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('v')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('2')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('2')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('shift+tab')
                                        time.sleep(2)

                                        screenshot = pyautogui.screenshot(region=area2)
                                        texto_extraido = pytesseract.image_to_string(screenshot)
                                        
                                        texto_extraido = texto_extraido.strip()  # Remove espaços no início e no fim
                                        texto_extraido = texto_extraido.replace("\n", "")  # Remove quebras de linha

                                        # Mostrar o texto extraído para depuração
                                        print("Texto extraído:\n", texto_extraido)

                                        # Comparar o texto
                                        if texto_extraido == "22000 V":
                                            keyboard.press_and_release('tab')
                                            time.sleep(0.2)
                                            keyboard.press_and_release('2')
                                            time.sleep(0.2)
                                            
                                        else:
                                            keyboard.press_and_release('tab')
                                            time.sleep(0.2)
                                            
                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('s')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('s')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('r')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('2')
                                        keyboard.press_and_release('0')
                                        keyboard.press_and_release('0')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('4')
                                        keyboard.press_and_release('3')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('4')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('2')
                                        keyboard.press_and_release('0')
                                        keyboard.press_and_release('0')
                                        time.sleep(1)
                                        
                                        pyautogui.click(x_registado_cmp_potencia, y_registado_cmp1_potencia, button='left', clicks=1, interval=0.25)
                                        time.sleep(0.2)

                                        keyboard.press_and_release('2')
                                        keyboard.press_and_release('.')
                                        keyboard.press_and_release('2')
                                        time.sleep(0.2)
                                        
                                        pyautogui.click(x_propriedade, y_propriedade, button='left', clicks=2, interval=0.25)
                                        time.sleep(0.2)
                                        
                                        keyboard.press_and_release('backspace')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('1')
                                        keyboard.press_and_release('7')
                                        keyboard.press_and_release('2')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)

                                        pyautogui.click(x_gis_x, y_gis_x, button='left', clicks=2, interval=0.25)
                                        time.sleep(0.2)
                                        
                                        keyboard.press_and_release('backspace')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('2')
                                        time.sleep(0.2)

                                        pyautogui.click(x_gis_y, y_gis_y, button='left', clicks=2, interval=0.25)
                                        time.sleep(0.2)
                                        
                                        keyboard.press_and_release('backspace')
                                        time.sleep(0.2)
                                        
                                        keyboard.press_and_release('1')
                                        time.sleep(0.2)

                                        pyautogui.click(x_estado_instalacao, y_estado_instalacao, button='left', clicks=1, interval=0.25)
                                        time.sleep(0.2) 

                                        keyboard.press_and_release('s')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('s')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('s')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('s')
                                        time.sleep(0.2)

                                        pyautogui.click(x_num_luz, y_num_luz, button='left', clicks=1, interval=0.25)
                                        time.sleep(0.2) 

                                        keyboard.press_and_release('8')
                                        time.sleep(1)

                                        pyautogui.click(x_quartos, y_quartos, button='left', clicks=1, interval=0.25)
                                        time.sleep(0.2) 

                                        keyboard.press_and_release('4')
                                        time.sleep(0.2)

                                        pyautogui.click(x_registro, y_registro, button='left', clicks=1, interval=0.25)
                                        time.sleep(0.2) 

                                        keyboard.press_and_release('space')
                                        keyboard.press_and_release('space')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.2)

                                        keyboard.press_and_release('n')
                                        time.sleep(0.2)

                                        pyautogui.click(x_registado_sim, y_registado_sim, button='left', clicks=1, interval=0.25)
                                        time.sleep(0.2) 

                                        keyboard.press_and_release('space')
                                        keyboard.press_and_release('space')
                                        time.sleep(0.2)

                                        pyautogui.click(x_anterior, y_anterior, button='left', clicks=3, interval=0.25)
                                        time.sleep(0.1)
                            

                                    # print("Retornando ao código principal.")
                                    break
                            

                        if not encontrou_linha:
                            contador_introduzido += 1
                        # print("Nenhuma linha correspondente encontrada. Pressionando Ctrl + I.")
                            keyboard.press_and_release('ctrl+i')
                            time.sleep(2)
                            keyboard.press_and_release('tab')
                            for _ in range(3):
                                keyboard.press_and_release('i')
                                time.sleep(1)
                            for _ in range(3):    
                                keyboard.press_and_release('tab')
                            keyboard.write('rede perda')
                            
                            pyautogui.click(x_seguinte, y_seguinte, button='left', clicks=2, interval=0.25)
                            time.sleep(1)
                            
                            for _ in range(4):    
                                keyboard.press_and_release('space')
                            time.sleep(1)
                            
                            pyautogui.click(x_processamento,y_processamento, button='left', clicks=2, interval=0.25)
                            time.sleep(1)

                            pyautogui.click(x_processamento_seguinte, y_processamento_seguinte, button='left', clicks=1, interval=0.25)
                            time.sleep(1)

                            pyautogui.click(x_imprimir, y_imprimir, button='left', clicks=1, interval=0.25)
                            time.sleep(0.5)

                            pyautogui.click( x_processamento_sim, y_processamento_sim, button='left', clicks=1, interval=0.25)
                            time.sleep(0.5)

                            pyautogui.click(x_registado, y_registado, button='left', clicks=2, interval=0.25)
                            time.sleep(1)

                            pyautogui.click(x_registado_seguinte, y_registado_seguinte, button='left', clicks=1, interval=0.25)
                            time.sleep(1)

                            pyautogui.click(x_registado_cmp1, y_registado_cmp1 , button='left', clicks=1, interval=0.25)
                            time.sleep(1)

                            keyboard.press_and_release('r')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('v')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('2')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('2')
                            time.sleep(0.2)

                            keyboard.press_and_release('shift+tab')
                            time.sleep(2)

                            screenshot = pyautogui.screenshot(region=area2)
                            texto_extraido = pytesseract.image_to_string(screenshot)
                            
                            texto_extraido = texto_extraido.strip()  # Remove espaços no início e no fim
                            texto_extraido = texto_extraido.replace("\n", "")  # Remove quebras de linha

                            # Mostrar o texto extraído para depuração
                            print("Texto extraído:\n", texto_extraido)

                            # Comparar o texto
                            if texto_extraido == "22000 V":
                                keyboard.press_and_release('tab')
                                time.sleep(0.2)
                                keyboard.press_and_release('2')
                                time.sleep(0.2)
                                
                            else:
                                keyboard.press_and_release('tab')
                                time.sleep(0.2)
                                
                            keyboard.press_and_release('tab')
                            time.sleep(0.2)
                            keyboard.press_and_release('s')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('s')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('r')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('2')
                            keyboard.press_and_release('0')
                            keyboard.press_and_release('0')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('4')
                            keyboard.press_and_release('3')
                            time.sleep(0.2)
        
                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('4')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('2')
                            keyboard.press_and_release('0')
                            keyboard.press_and_release('0')
                            time.sleep(1)
                            
                            pyautogui.click(x_registado_cmp_potencia, y_registado_cmp1_potencia, button='left', clicks=1, interval=0.25)
                            time.sleep(0.2)

                            keyboard.press_and_release('2')
                            keyboard.press_and_release('.')
                            keyboard.press_and_release('2')
                            time.sleep(0.2)
                            
                            pyautogui.click(x_propriedade, y_propriedade, button='left', clicks=2, interval=0.25)
                            time.sleep(0.2)
                            
                            keyboard.press_and_release('backspace')
                            time.sleep(0.2) 

                            keyboard.press_and_release('1')
                            keyboard.press_and_release('7')
                            keyboard.press_and_release('2')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            pyautogui.click(x_gis_x, y_gis_x, button='left', clicks=2, interval=0.25)
                            time.sleep(0.2)
                            
                            keyboard.press_and_release('backspace')
                            time.sleep(0.2)

                            keyboard.press_and_release('2')
                            time.sleep(0.2)

                            pyautogui.click(x_gis_y, y_gis_y, button='left', clicks=2, interval=0.25)
                            time.sleep(0.2)
                            
                            keyboard.press_and_release('backspace')
                            time.sleep(0.2)
                            
                            keyboard.press_and_release('1')
                            time.sleep(0.2)

                            
                            pyautogui.click(x_estado_instalacao, y_estado_instalacao, button='left', clicks=1, interval=0.25)
                            time.sleep(0.2) 

                            keyboard.press_and_release('s')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('s')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('s')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('s')
                            time.sleep(0.2)
                        
                            pyautogui.click(x_num_luz, y_num_luz , button='left', clicks=1, interval=0.25)
                            time.sleep(0.2) 

                            keyboard.press_and_release('8')
                            time.sleep(1)

                            pyautogui.click(x_quartos, y_quartos, button='left', clicks=1, interval=0.25)
                            time.sleep(0.2) 

                            keyboard.press_and_release('4')
                            time.sleep(0.2)
                            

                            pyautogui.click(x_registro, y_registro, button='left', clicks=1, interval=0.25)
                            time.sleep(0.2) 

                            keyboard.press_and_release('space')
                            keyboard.press_and_release('space')
                            keyboard.press_and_release('space')
                            time.sleep(0.2)

                            keyboard.press_and_release('tab')
                            time.sleep(0.2)

                            keyboard.press_and_release('n')
                            time.sleep(0.2)
                            

                            pyautogui.click( x_registado_sim, y_registado_sim, button='left', clicks=1, interval=0.25)
                            time.sleep(0.2) 

                            keyboard.press_and_release('space')
                            keyboard.press_and_release('space')
                            keyboard.press_and_release('space')
                            time.sleep(0.2)
                            
                            pyautogui.click(x_anterior, y_anterior, button='left', clicks=3, interval=0.25)
                            time.sleep(0.1)
                            
                        
                    
    

except KeyboardInterrupt:
    print("\nPrograma encerrado pelo utilizador.") 
# Hora de término
hora_fim = time.time() + 2 * 3600
tempo_execucao = (hora_fim - hora_inicio)/60
numeros_errados_totais = contador_introduzido - numeros_errados
print(f"\n\nProcesso concluído!")
print(f"Hora de início: {time.strftime('%H:%M:%S', time.gmtime(hora_inicio))}")
print(f"Hora de término: {time.strftime('%H:%M:%S', time.gmtime(hora_fim))}")
print(f"Tempo total de execução: {tempo_execucao:.2f} min")
print(f"Número de dados para processamento: {num_dados}")
print(f"Total de dados processados: {total_processados}")
print(f"Total de inspecções introduzidas: {contador_introduzido}")
print(f"Total de inspecções colocadas em processamento: {contador_registados}")
print(f"Total de inspecções resolvidas: {contador_em_processamento}")
print(f"Total de numeros errados: {numeros_errados}")
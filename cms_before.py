import pyautogui
import pyperclip
import keyboard
import time
import pytesseract
from PIL import Image
import re
erD =  [ 'at 1', 'f 3', 'e ', 'r ', 411 ]
numerosErradosp2 = [130, 140] 

#print()
# Caminho do executável do Tesseract (ajuste conforme seu sistema)
# pytesseract.pytesseract.tesseract_cmd =C:\Program Files\Tesseract-OCR\tesseract.exe'  # Para Windows 
  

pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"  # Caminho no Linux



# Lista de dados a serem c
# ado
dados = ['14478427371', '14440926468', '01317050266', '54229687097', '01344030612', '01343424667', '01343424113', '01343900336', '01344036528', '01347794537', '07117073820', '01317039285', '01344309537', '01351576820', '04286937349', '54736668929', '30280076560', '01343425615', '54735032861', '01621040433', '30280003275', '01344811260', '14320996367', '01350762413', '54181205524', '14478062871', '22131897187', '54181185304', '30280137263', '07049105401', '07112228494', '01351059017', '04262237387', '54205379677', '54181205524', '54281320561', '54180686047', '22117843726', '54181162782', '54229591265', '54229584393', '54180689769', '01351584949', '14320709927', '01344009640', '14319880325', '07048441914', '01340651486', '01347615997', '04286111416', '01319525737', '07117073838', '01351816820', '01342054887', '22132932280', '54230433499', '14320524979', '54229584393', '54181194868', '30280293132', '01344844871', '14315743527', '54280993046', '01318720966', '22140443551', '01345652422', '22119225948', '84625250632', '14478499503', '01342076070', '54216462645', '01349391787', '22120993336', '01349259596', '01351389182', '04286007705', '07117030879', '54734111096', '07138151167', '01351172711', '22121019503', '22117851224', '14478348684', '54181112357', '70002788266', '22132943527', '54731463870', '07120796128', '54228001399', '07116783973', '14315743527', '54735078567', '14478571863', '01345656944', '54735034024', '22133270490', '54203304560', '07123049517', '54216444353', '07112335067', '54735027705', '07115093838', '04289249155', '54181138996', '14478463483', '01351582240', '07117073275', '54734155499', '04287216446', '04286929502', '54733821257', '54180397017', '54733831801', '54205762112', '22117839195', '07117294715', '01347015420', '07103758426', '07138152389', '07117050976', '54733821646', '14319292737', '54217255048', '14320675417', '22132941315', '30280065134', '54228545544', '07118199715', '70003618868', '01350649149', '22117844898', '54281150026', '54228545585', '54228530231', '07117030044', '54734109413', '84625035708', '01342963590', '14478062871', '04262237387', '07101797665', '54228545593', '01344814361', '22119191686', '01075461564', '01345751844', '04287210829', '54205409748', '70003630319', '54216954278', '07111837725', '01351385487', '14478621502', '54228081466', '54220323559', '04287209524', '01350766414', '14478552087', '04286888534', '70002790072', '14441173581', '22114422649', '01345378481', '07114747541', '14322959108', '07115094448', '07116760575', '04287221867', '54180322015', '54205325183', '54734253518', '01347758821', '07113147776', '54181233781', '54203807828', '01343918387', '54227666226', '07060163602', '14478619373', '54229584260', '54181028975', '22140461314', '54203805871', '14319540531', '54734206326', '14322897209', '54281125671', '54181138998', '54230420975', '07114922177', '07114933166', '54731383839', '14478760698', '14478550800', '14478691885', '14322946543', '14320681043', '01344016264', '14318999415', '54229688855', '01342962410', '07114921963', '54228536048', '14320758395', '54181112407', '01351392251', '07116762340', '30280173649', '01345626764', '04287222253', '07049109874', '14320371967', '01344009640', '54180686047', '14478641450', '22120972223', '54229591265', '54229584393', '22114419132', '07114933950', '14320482186', '01342061924', '22114408267', '14319880325', '54230420975', '54203139321', '01350664437', '01343922488', '54228493182', '07114892131', '22132922133', '22131897187', '22132922109', '22129156869', '07115115326', '07049564706', '01345385676', '01347764449', '22131931697', '01317777702', '54291792544', '54732591034', '54180102532', '22132938964', '54181193266', '14322897209', '14478327688', '01347782292', '14478634901', '54205379677', '14478166169', '01344286958', '04287222253', '04286476728', '01351400732', '30280137263', '70002620709', '14321407554', '54203353039', '54228533078', '07139972074', '01350761795', '25111435548', '07117074851', '54181165629', '54281334042', '07118835904', '54203908246', '01347779512', '14478550453', '01351587728', '01345379646', '14478293088', '30280007292', '07114891000', '54227850465', '30280292324', '54228884307', '54181139202', '54281322112', '54732485732', '07054916031', '30280270544', '54731459266', '54230049477', '07117018890', '14320523914', '07107114295', '01351373756', '54737162468', '54228507080', '01317050266', '54291792544', '01344023781', '01351675531', '07114747020', '54280999704', '01344309537', '22120982156', '22131879334', '54281156221', '01343424667', '22132925292', '07114894319', '07056012474', '54228464548', '07049661270', '07055719798', '54180341494', '30280223170', '22120976949', '01343478663', '54281129582', '01344843956', '14478702674', '22121019537', '14441173466', '01319496194', '01351618127', '22117852917', '01343490791', '14478764740', '07115082575', '01342076088', '07048387216', '54281334190', '01343478663', '07107107398', '70002627340', '01343906077', '07114895340', '07049146207', '01343424659', '01345656951', '01343895890', '01313147777', '22131933024'
]
            

   
 
#   
# Variáveis para marcar a hora de início es fim
hora_inicio = time.time() + 2 * 3600
num_dados = len(dados)

# Coordenadas fixas
#area = (41, 546, 910, 133)  # Ajuste conforme necessário
# area = (41, 526, 905, 145)

#Coordenadas fixas 
area = (41, 546, 910, 133)
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
x_cancelar, y_cancelar = (616, 483)


# area = (42, 547, 910, 131)
# # area = (33, 519, 918, 161)
# x_pf, y_pf = 89, 250
# x_contador_btn, y_contador_btn = 361, 318
# x_ok_btn, y_ok_btn = 899, 541  # Coordenadas do botão "OK" no erro
# x_clique_esquerdo, y_clique_esquero = 381, 472
# x_seguinte, y_seguinte = 508, 742
# x_processamento,y_processamento = 349, 355
# x_processamento_seguinte, y_processamento_seguinte = 503, 674
# x_imprimir, y_imprimir = 561, 192
# x_processamento_sim, y_processamento_sim = 503, 674
# x_registado, y_registado = 541, 356
# x_registado_seguinte, y_registado_seguinte = 509, 673
# x_registado_cmp1, y_registado_cmp1 = 503, 178                     
# x_registado_cmp_potencia, y_registado_cmp1_potencia = 820, 284
# x_propriedade, y_propriedade = 780, 303
# x_gis_x, y_gis_x = 753, 331
# x_gis_y, y_gis_y = 762, 358

# x_registro, y_registro =  503, 674
# x_registado_sim, y_registado_sim =  503, 674
# x_anterior, y_anterior = 390, 734
# area2 = (443, 248, 89, 16)
# click_position = 941, 631
# x_cancelar, y_cancelar = (616, 483)















































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
numero = ""
numeros = []
# Monitorar a combinação Ctrl + Q para interrupção
# Encerra o programa de maneira segura
try:
    time.sleep(2)
    for item in dados:
        pyautogui.click(x_pf, y_pf, button='left', clicks=2, interval=0.25)
        time.sleep(0.9)

        pyautogui.click(x_contador_btn, y_contador_btn, button='left', clicks=1, interval=0.25)
        time.sleep(0.1)

        pyperclip.copy(item)

        pyautogui.hotkey("ctrl", "v")
        print(item)
        time.sleep(1)

        pyautogui.press("enter")
        time.sleep(0.8)
                     
        total_processados += 1

        try:
            erro_na_tela = pyautogui.locateOnScreen(erro_img_path, confidence=0.5)
            erro_na_tela1 = pyautogui.locateOnScreen(erro_img_path1, confidence=0.5)  # Aumentar a confiança

            if erro_na_tela:
                numeros_errados += 1
                numero += item
                numeros = re.findall(r'\d{11}', numero)
                print("Erro detectado, clicando em OK...")
                # Clica no botão "OK"
                pyautogui.click(x_ok_btn, y_ok_btn, button='left', clicks=1, interval=0.25)   

                continue        
    
        except pyautogui.ImageNotFoundException:
            # print("Erro não encontrado.")
            # Clica com o botão direito na coordenada especificada
            pyautogui.click(x_clique_esquerdo, y_clique_esquero, button='left', clicks=2, interval=0.25)
            time.sleep(2)
            keyboard.press_and_release("space")
            time.sleep(0.1)  

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
        
        keyboard.press_and_release("space")
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
                if 'por suspeita de fraude' in linha.lower(): 
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
                            time.sleep(4)

                            pyautogui.click(x_imprimir, y_imprimir, button='left', clicks=1, interval=0.25)
                            time.sleep(2)


                            pyautogui.click( x_processamento_sim, y_processamento_sim, button='left', clicks=1, interval=0.25)
                            time.sleep(4)

                            pyautogui.click(x_cancelar, y_cancelar, button='left', clicks=1, interval=0.25)
                            time.sleep(2)

                            # pyautogui.click(x_registado, y_registado, button='left', clicks=2, interval=0.25)
                            # time.sleep(2)

                            # pyautogui.click(x_registado_seguinte, y_registado_seguinte, button='left', clicks=3, interval=0.5)
                            # time.sleep(3)

                            # keyboard.press_and_release('space')

                            # pyautogui.click(x_registado_cmp1, y_registado_cmp1 , button='left', clicks=1, interval=0.25)
                            # time.sleep(5)

                            # keyboard.press_and_release('r')
                            # time.sleep(0.5)

                            # keyboard.press_and_release('tab')
                            # time.sleep(0.5)

                            # keyboard.press_and_release('v')
                            # time.sleep(0.5)

                            # keyboard.press_and_release('tab')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('2')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('tab')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('2')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('shift+tab')
                            # time.sleep(2)

                            # screenshot = pyautogui.screenshot(region=area2)
                            # texto_extraido = pytesseract.image_to_string(screenshot)
                            
                            # texto_extraido = texto_extraido.strip()  # Remove espaços no início e no fim
                            # texto_extraido = texto_extraido.replace("\n", "")  # Remove quebras de linha

                            # # Mostrar o texto extraído para depuração
                            # print("Texto extraído:\n", texto_extraido)

                            # # Comparar o texto
                            # if texto_extraido == "22000 V":
                            #     keyboard.press_and_release('tab')
                            #     time.sleep(0.3)
                            #     keyboard.press_and_release('2')
                            #     time.sleep(0.3)
                                
                            # else:
                            #     keyboard.press_and_release('tab')
                            #     time.sleep(0.3)
                                
                            # keyboard.press_and_release('tab')
                            # time.sleep(0.3)
                            # keyboard.press_and_release('s')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('tab')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('s')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('tab')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('r')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('tab')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('2')
                            # keyboard.press_and_release('0')
                            # keyboard.press_and_release('0')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('tab')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('4')
                            # keyboard.press_and_release('3')
                            # time.sleep(0.3)
        
                            # keyboard.press_and_release('tab')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('4')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('tab')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('2')
                            # keyboard.press_and_release('0')
                            # keyboard.press_and_release('0')
                            # time.sleep(1)
                            
                            # pyautogui.click(x_registado_cmp_potencia, y_registado_cmp1_potencia, button='left', clicks=1, interval=0.25)
                            # time.sleep(0.3)

                            # keyboard.press_and_release('2')
                            # keyboard.press_and_release('.')
                            # keyboard.press_and_release('2')
                            # time.sleep(0.3)
                            
                            # pyautogui.click(x_propriedade, y_propriedade, button='left', clicks=2, interval=0.25)
                            # time.sleep(0.3)
                            
                            # keyboard.press_and_release('backspace')
                            # time.sleep(0.3) 

                            # keyboard.press_and_release('1')
                            # keyboard.press_and_release('7')
                            # keyboard.press_and_release('2')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('tab')
                            # time.sleep(0.3)

                            # pyautogui.click(x_gis_x, y_gis_x, button='left', clicks=2, interval=0.25)
                            # time.sleep(0.3)
                            
                            # keyboard.press_and_release('backspace')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('2')
                            # time.sleep(0.3)

                            # pyautogui.click(x_gis_y, y_gis_y, button='left', clicks=2, interval=0.25)
                            # time.sleep(0.3)
                            
                            # keyboard.press_and_release('backspace')
                            # time.sleep(0.3)
                            
                            # keyboard.press_and_release('1')
                            # time.sleep(0.3)

                            
                            # pyautogui.click(x_estado_instalacao, y_estado_instalacao, button='left', clicks=1, interval=0.25)
                            # time.sleep(0.3) 

                            # keyboard.press_and_release('s')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('tab')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('s')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('tab')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('s')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('tab')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('s')
                            # time.sleep(0.3)
                        
                            # pyautogui.click(x_num_luz, y_num_luz , button='left', clicks=1, interval=0.25)
                            # time.sleep(0.3) 

                            # keyboard.press_and_release('8')
                            # time.sleep(1)

                            # pyautogui.click(x_quartos, y_quartos, button='left', clicks=1, interval=0.25)
                            # time.sleep(0.3) 

                            # keyboard.press_and_release('4')
                            # time.sleep(0.3)
                            

                            # pyautogui.click(x_registro, y_registro, button='left', clicks=1, interval=0.25)
                            # time.sleep(0.3) 

                            # keyboard.press_and_release('space')
                            # keyboard.press_and_release('space')
                            # keyboard.press_and_release('space')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('tab')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('n')
                            # time.sleep(0.3)
                            

                            # pyautogui.click( x_registado_sim, y_registado_sim, button='left', clicks=1, interval=0.25)
                            # time.sleep(0.3) 

                            # keyboard.press_and_release('space')
                            # keyboard.press_and_release('space')
                            # keyboard.press_and_release('space')
                            # time.sleep(0.3)
                            
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
                            time.sleep(5)

                            pyautogui.click(x_registado_cmp1, y_registado_cmp1, button='left', clicks=1, interval=0.25)
                            time.sleep(4)

                            keyboard.press_and_release('r')
                            time.sleep(0.3)

                            keyboard.press_and_release('tab')
                            time.sleep(0.3)

                            keyboard.press_and_release('v')
                            time.sleep(0.3)

                            keyboard.press_and_release('tab')
                            time.sleep(0.3)

                            keyboard.press_and_release('2')
                            time.sleep(0.3)

                            keyboard.press_and_release('tab')
                            time.sleep(0.3)

                            keyboard.press_and_release('2')
                            time.sleep(0.3)

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
                                time.sleep(0.3)
                                keyboard.press_and_release('2')
                                time.sleep(0.3)
                                
                            else:
                                keyboard.press_and_release('tab')
                                time.sleep(0.3)
                                
                            keyboard.press_and_release('tab')
                            time.sleep(0.3)

                            keyboard.press_and_release('s')
                            time.sleep(0.3)

                            keyboard.press_and_release('tab')
                            time.sleep(0.3)

                            keyboard.press_and_release('s')
                            time.sleep(0.3)

                            keyboard.press_and_release('tab')
                            time.sleep(0.3)

                            keyboard.press_and_release('r')
                            time.sleep(0.3)

                            keyboard.press_and_release('tab')
                            time.sleep(0.3)

                            keyboard.press_and_release('2')
                            keyboard.press_and_release('0')
                            keyboard.press_and_release('0')
                            time.sleep(0.3)

                            keyboard.press_and_release('tab')
                            time.sleep(0.3)

                            keyboard.press_and_release('4')
                            keyboard.press_and_release('3')
                            time.sleep(0.3)

                            keyboard.press_and_release('tab')
                            time.sleep(0.3)

                            keyboard.press_and_release('4')
                            time.sleep(0.3)

                            keyboard.press_and_release('tab')
                            time.sleep(0.3)

                            keyboard.press_and_release('2')
                            keyboard.press_and_release('0')
                            keyboard.press_and_release('0')
                            time.sleep(1)
                            
                            pyautogui.click(x_registado_cmp_potencia, y_registado_cmp1_potencia, button='left', clicks=1, interval=0.25)
                            time.sleep(0.3)

                            keyboard.press_and_release('2')
                            keyboard.press_and_release('.')
                            keyboard.press_and_release('2')
                            time.sleep(0.3)
                            
                            pyautogui.click(x_propriedade, y_propriedade, button='left', clicks=2, interval=0.25)
                            time.sleep(0.3)
                            
                            keyboard.press_and_release('backspace')
                            time.sleep(0.3)

                            keyboard.press_and_release('1')
                            keyboard.press_and_release('7')
                            keyboard.press_and_release('2')
                            time.sleep(0.3)

                            keyboard.press_and_release('tab')
                            time.sleep(0.3)

                            pyautogui.click(x_gis_x, y_gis_x, button='left', clicks=2, interval=0.25)
                            time.sleep(0.3)
                            
                            keyboard.press_and_release('backspace')
                            time.sleep(0.3)

                            keyboard.press_and_release('2')
                            time.sleep(0.3)

                            pyautogui.click(x_gis_y, y_gis_y, button='left', clicks=2, interval=0.25)
                            time.sleep(0.3)
                            
                            keyboard.press_and_release('backspace')
                            time.sleep(0.3)
                            
                            keyboard.press_and_release('1')
                            time.sleep(0.3)

                            # pyautogui.click(x_estado_instalacao, y_estado_instalacao, button='left', clicks=1, interval=0.25)
                            # time.sleep(0.3) 

                            # keyboard.press_and_release('s')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('tab')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('s')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('tab')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('s')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('tab')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('s')
                            # time.sleep(0.3)

                            # pyautogui.click(x_num_luz, y_num_luz, button='left', clicks=1, interval=0.25)
                            # time.sleep(0.3) 

                            # keyboard.press_and_release('8')
                            # time.sleep(1)

                            # pyautogui.click(x_quartos, y_quartos, button='left', clicks=1, interval=0.25)
                            # time.sleep(0.3) 

                            # keyboard.press_and_release('4')
                            # time.sleep(0.3)

                            # pyautogui.click(x_registro, y_registro, button='left', clicks=1, interval=0.25)
                            # time.sleep(0.3) 

                            # keyboard.press_and_release('space')
                            # keyboard.press_and_release('space')
                            # time.sleep(0.3)

                            keyboard.press_and_release('tab')
                            time.sleep(0.3)

                            keyboard.press_and_release('n')
                            time.sleep(0.3)

                            pyautogui.click(x_registado_sim, y_registado_sim, button='left', clicks=1, interval=0.25)
                            time.sleep(0.3) 

                            keyboard.press_and_release('space')
                            keyboard.press_and_release('space')
                            time.sleep(0.3)

                            pyautogui.click(x_anterior, y_anterior, button='left', clicks=3, interval=0.25)
                            time.sleep(0.1)
                            
                            
                
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
                    if 'por suspeita de fraude' in linha.lower():
                        if 'registad' in linha.lower():
                            print(f"Linha encontrada (Registado): {linha}")
                            encontrou_linha = True
                            contador_registados +=1

                            # Extrair o número da O.T. usando regex (números no início da linha)
                            match = re.match(r'^\d+', linha)
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
                                time.sleep(4)

                                pyautogui.click(x_imprimir, y_imprimir, button='left', clicks=1, interval=0.25)
                                time.sleep(2)


                                pyautogui.click( x_processamento_sim, y_processamento_sim, button='left', clicks=1, interval=0.25)
                                time.sleep(4)

                                pyautogui.click(x_cancelar, y_cancelar, button='left', clicks=1, interval=0.25)
                                time.sleep(2)

                                # pyautogui.click(x_registado, y_registado, button='left', clicks=2, interval=0.25)
                                # time.sleep(2)

                                # pyautogui.click(x_registado_seguinte, y_registado_seguinte, button='left', clicks=3, interval=0.5)
                                # time.sleep(3)
                                # keyboard.press_and_release('space')

                                # pyautogui.click(x_registado_cmp1, y_registado_cmp1 , button='left', clicks=1, interval=0.25)
                                # time.sleep(5)

                                # keyboard.press_and_release('r')
                                # time.sleep(0.5)

                                # keyboard.press_and_release('tab')
                                # time.sleep(0.5)

                                # keyboard.press_and_release('v')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('tab')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('2')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('tab')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('2')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('shift+tab')
                                # time.sleep(2)

                                # screenshot = pyautogui.screenshot(region=area2)
                                # texto_extraido = pytesseract.image_to_string(screenshot)
                                
                                # texto_extraido = texto_extraido.strip()  # Remove espaços no início e no fim
                                # texto_extraido = texto_extraido.replace("\n", "")  # Remove quebras de linha

                                # # Mostrar o texto extraído para depuração
                                # print("Texto extraído:\n", texto_extraido)

                                # # Comparar o texto
                                # if texto_extraido == "22000 V":
                                #     keyboard.press_and_release('tab')
                                #     time.sleep(0.3)
                                #     keyboard.press_and_release('2')
                                #     time.sleep(0.3)
                                    
                                # else:
                                #     keyboard.press_and_release('tab')
                                #     time.sleep(0.3)
                                    
                                # keyboard.press_and_release('tab')
                                # time.sleep(0.3)
                                # keyboard.press_and_release('s')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('tab')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('s')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('tab')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('r')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('tab')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('2')
                                # keyboard.press_and_release('0')
                                # keyboard.press_and_release('0')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('tab')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('4')
                                # keyboard.press_and_release('3')
                                # time.sleep(0.3)
            
                                # keyboard.press_and_release('tab')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('4')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('tab')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('2')
                                # keyboard.press_and_release('0')
                                # keyboard.press_and_release('0')
                                # time.sleep(1)
                                
                                # pyautogui.click(x_registado_cmp_potencia, y_registado_cmp1_potencia, button='left', clicks=1, interval=0.25)
                                # time.sleep(0.3)

                                # keyboard.press_and_release('2')
                                # keyboard.press_and_release('.')
                                # keyboard.press_and_release('2')
                                # time.sleep(0.3)
                                
                                # pyautogui.click(x_propriedade, y_propriedade, button='left', clicks=2, interval=0.25)
                                # time.sleep(0.3)
                                
                                # keyboard.press_and_release('backspace')
                                # time.sleep(0.3) 

                                # keyboard.press_and_release('1')
                                # keyboard.press_and_release('7')
                                # keyboard.press_and_release('2')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('tab')
                                # time.sleep(0.3)

                                # pyautogui.click(x_gis_x, y_gis_x, button='left', clicks=2, interval=0.25)
                                # time.sleep(0.3)
                                
                                # keyboard.press_and_release('backspace')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('2')
                                # time.sleep(0.3)

                                # pyautogui.click(x_gis_y, y_gis_y, button='left', clicks=2, interval=0.25)
                                # time.sleep(0.3)
                                
                                # keyboard.press_and_release('backspace')
                                # time.sleep(0.3)
                                
                                # keyboard.press_and_release('1')
                                # time.sleep(0.3)

                                
                                # pyautogui.click(x_estado_instalacao, y_estado_instalacao, button='left', clicks=1, interval=0.25)
                                # time.sleep(0.3) 

                                # keyboard.press_and_release('s')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('tab')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('s')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('tab')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('s')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('tab')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('s')
                                # time.sleep(0.3)
                            
                                # pyautogui.click(x_num_luz, y_num_luz , button='left', clicks=1, interval=0.25)
                                # time.sleep(0.3) 

                                # keyboard.press_and_release('8')
                                # time.sleep(1)

                                # pyautogui.click(x_quartos, y_quartos, button='left', clicks=1, interval=0.25)
                                # time.sleep(0.3) 

                                # keyboard.press_and_release('4')
                                # time.sleep(0.3)
                                

                                # pyautogui.click(x_registro, y_registro, button='left', clicks=1, interval=0.25)
                                # time.sleep(0.3) 

                                # keyboard.press_and_release('space')
                                # keyboard.press_and_release('space')
                                # keyboard.press_and_release('space')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('tab')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('n')
                                # time.sleep(0.3)
                                

                                # pyautogui.click( x_registado_sim, y_registado_sim, button='left', clicks=1, interval=0.25)
                                # time.sleep(0.3) 

                                # keyboard.press_and_release('space')
                                # keyboard.press_and_release('space')
                                # keyboard.press_and_release('space')
                                # time.sleep(0.3)
                                
                                pyautogui.click(x_anterior, y_anterior, button='left', clicks=3, interval=0.25)
                                time.sleep(0.1)
                        


                    # Caso o estado seja "em processamento", retorna ao fluxo principal
                    elif 'em processament' in linha.lower():
                            # print(f"Linha encontrada (Em Processamento): {linha}")
                            encontrou_linha = True
                            contador_em_processamento += 1

                            match = re.match(r'^\d+', linha)
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
                                time.sleep(5)

                                pyautogui.click(x_registado_cmp1, y_registado_cmp1, button='left', clicks=1, interval=0.25)
                                time.sleep(4)

                                keyboard.press_and_release('r')
                                time.sleep(0.3)

                                keyboard.press_and_release('tab')
                                time.sleep(0.3)

                                keyboard.press_and_release('v')
                                time.sleep(0.3)

                                keyboard.press_and_release('tab')
                                time.sleep(0.3)

                                keyboard.press_and_release('2')
                                time.sleep(0.3)

                                keyboard.press_and_release('tab')
                                time.sleep(0.3)

                                keyboard.press_and_release('2')
                                time.sleep(0.3)

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
                                    time.sleep(0.3)
                                    keyboard.press_and_release('2')
                                    time.sleep(0.3)
                                    
                                else:
                                    keyboard.press_and_release('tab')
                                    time.sleep(0.3)
                                    
                                keyboard.press_and_release('tab')
                                time.sleep(0.3)

                                keyboard.press_and_release('s')
                                time.sleep(0.3)

                                keyboard.press_and_release('tab')
                                time.sleep(0.3)

                                keyboard.press_and_release('s')
                                time.sleep(0.3)

                                keyboard.press_and_release('tab')
                                time.sleep(0.3)

                                keyboard.press_and_release('r')
                                time.sleep(0.3)

                                keyboard.press_and_release('tab')
                                time.sleep(0.3)

                                keyboard.press_and_release('2')
                                keyboard.press_and_release('0')
                                keyboard.press_and_release('0')
                                time.sleep(0.3)

                                keyboard.press_and_release('tab')
                                time.sleep(0.3)

                                keyboard.press_and_release('4')
                                keyboard.press_and_release('3')
                                time.sleep(0.3)

                                keyboard.press_and_release('tab')
                                time.sleep(0.3)

                                keyboard.press_and_release('4')
                                time.sleep(0.3)

                                keyboard.press_and_release('tab')
                                time.sleep(0.3)

                                keyboard.press_and_release('2')
                                keyboard.press_and_release('0')
                                keyboard.press_and_release('0')
                                time.sleep(1)
                                
                                pyautogui.click(x_registado_cmp_potencia, y_registado_cmp1_potencia, button='left', clicks=1, interval=0.25)
                                time.sleep(0.3)

                                keyboard.press_and_release('2')
                                keyboard.press_and_release('.')
                                keyboard.press_and_release('2')
                                time.sleep(0.3)
                                
                                pyautogui.click(x_propriedade, y_propriedade, button='left', clicks=2, interval=0.25)
                                time.sleep(0.3)
                                
                                keyboard.press_and_release('backspace')
                                time.sleep(0.3)

                                keyboard.press_and_release('1')
                                keyboard.press_and_release('7')
                                keyboard.press_and_release('2')
                                time.sleep(0.3)

                                keyboard.press_and_release('tab')
                                time.sleep(0.3)

                                pyautogui.click(x_gis_x, y_gis_x, button='left', clicks=2, interval=0.25)
                                time.sleep(0.3)
                                
                                keyboard.press_and_release('backspace')
                                time.sleep(0.3)

                                keyboard.press_and_release('2')
                                time.sleep(0.3)

                                pyautogui.click(x_gis_y, y_gis_y, button='left', clicks=2, interval=0.25)
                                time.sleep(0.3)
                                
                                keyboard.press_and_release('backspace')
                                time.sleep(0.3)
                                
                                keyboard.press_and_release('1')
                                time.sleep(0.3)

                                # pyautogui.click(x_estado_instalacao, y_estado_instalacao, button='left', clicks=1, interval=0.25)
                                # time.sleep(0.3) 

                                # keyboard.press_and_release('s')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('tab')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('s')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('tab')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('s')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('tab')
                                # time.sleep(0.3)

                                # keyboard.press_and_release('s')
                                # time.sleep(0.3)

                                # pyautogui.click(x_num_luz, y_num_luz, button='left', clicks=1, interval=0.25)
                                # time.sleep(0.3) 

                                # keyboard.press_and_release('8')
                                # time.sleep(1)

                                # pyautogui.click(x_quartos, y_quartos, button='left', clicks=1, interval=0.25)
                                # time.sleep(0.3) 

                                # keyboard.press_and_release('4')
                                # time.sleep(0.3)

                                pyautogui.click(x_registro, y_registro, button='left', clicks=1, interval=0.25)
                                time.sleep(0.3) 

                                keyboard.press_and_release('space')
                                keyboard.press_and_release('space')
                                time.sleep(0.3)

                                keyboard.press_and_release('tab')
                                time.sleep(0.3)

                                keyboard.press_and_release('n')
                                time.sleep(0.3)

                                pyautogui.click(x_registado_sim, y_registado_sim, button='left', clicks=1, interval=0.25)
                                time.sleep(0.3) 

                                keyboard.press_and_release('space')
                                keyboard.press_and_release('space')
                                time.sleep(0.3)

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
                        
                        # pyautogui.click(x_processamento,y_processamento, button='left', clicks=2, interval=0.25)
                        # time.sleep(1)

                        # pyautogui.click(x_processamento_seguinte, y_processamento_seguinte, button='left', clicks=1, interval=0.25)
                        # time.sleep(4)

                        # pyautogui.click(x_imprimir, y_imprimir, button='left', clicks=1, interval=0.25)
                        # time.sleep(2)


                        # pyautogui.click( x_processamento_sim, y_processamento_sim, button='left', clicks=1, interval=0.25)
                        # time.sleep(4)

                        # pyautogui.click(x_cancelar, y_cancelar, button='left', clicks=1, interval=0.25)
                        # time.sleep(2)

                        # pyautogui.click(x_registado, y_registado, button='left', clicks=2, interval=0.25)
                        # time.sleep(2)

                        # pyautogui.click(x_registado_seguinte, y_registado_seguinte, button='left', clicks=3, interval=0.5)
                        # time.sleep(3)

                        # keyboard.press_and_release('space')

                        # pyautogui.click(x_registado_cmp1, y_registado_cmp1 , button='left', clicks=1, interval=0.25)
                        # time.sleep(5)

                        # keyboard.press_and_release('r')
                        # time.sleep(0.5)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.5)

                        # keyboard.press_and_release('v')
                        # time.sleep(0.5)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('2')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('2')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('shift+tab')
                        # time.sleep(2)

                        # screenshot = pyautogui.screenshot(region=area2)
                        # texto_extraido = pytesseract.image_to_string(screenshot)
                        
                        # texto_extraido = texto_extraido.strip()  # Remove espaços no início e no fim
                        # texto_extraido = texto_extraido.replace("\n", "")  # Remove quebras de linha

                        # # Mostrar o texto extraído para depuração
                        # print("Texto extraído:\n", texto_extraido)

                        # # Comparar o texto
                        # if texto_extraido == "22000 V":
                        #     keyboard.press_and_release('tab')
                        #     time.sleep(0.3)
                        #     keyboard.press_and_release('2')
                        #     time.sleep(0.3)
                            
                        # else:
                        #     keyboard.press_and_release('tab')
                        #     time.sleep(0.3)
                            
                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)
                        # keyboard.press_and_release('s')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('s')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('r')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('2')
                        # keyboard.press_and_release('0')
                        # keyboard.press_and_release('0')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('4')
                        # keyboard.press_and_release('3')
                        # time.sleep(0.3)
    
                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('4')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('2')
                        # keyboard.press_and_release('0')
                        # keyboard.press_and_release('0')
                        # time.sleep(1)
                        
                        # pyautogui.click(x_registado_cmp_potencia, y_registado_cmp1_potencia, button='left', clicks=1, interval=0.25)
                        # time.sleep(0.3)

                        # keyboard.press_and_release('2')
                        # keyboard.press_and_release('.')
                        # keyboard.press_and_release('2')
                        # time.sleep(0.3)
                        
                        # pyautogui.click(x_propriedade, y_propriedade, button='left', clicks=2, interval=0.25)
                        # time.sleep(0.3)
                        
                        # keyboard.press_and_release('backspace')
                        # time.sleep(0.3) 

                        # keyboard.press_and_release('1')
                        # keyboard.press_and_release('7')
                        # keyboard.press_and_release('2')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # pyautogui.click(x_gis_x, y_gis_x, button='left', clicks=2, interval=0.25)
                        # time.sleep(0.3)
                        
                        # keyboard.press_and_release('backspace')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('2')
                        # time.sleep(0.3)

                        # pyautogui.click(x_gis_y, y_gis_y, button='left', clicks=2, interval=0.25)
                        # time.sleep(0.3)
                        
                        # keyboard.press_and_release('backspace')
                        # time.sleep(0.3)
                        
                        # keyboard.press_and_release('1')
                        # time.sleep(0.3)

                        
                        # pyautogui.click(x_estado_instalacao, y_estado_instalacao, button='left', clicks=1, interval=0.25)
                        # time.sleep(0.3) 

                        # keyboard.press_and_release('s')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('s')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('s')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('s')
                        # time.sleep(0.3)
                    
                        # pyautogui.click(x_num_luz, y_num_luz , button='left', clicks=1, interval=0.25)
                        # time.sleep(0.3) 

                        # keyboard.press_and_release('8')
                        # time.sleep(1)

                        # pyautogui.click(x_quartos, y_quartos, button='left', clicks=1, interval=0.25)
                        # time.sleep(0.3) 

                        # keyboard.press_and_release('4')
                        # time.sleep(0.3)
                        

                        # pyautogui.click(x_registro, y_registro, button='left', clicks=1, interval=0.25)
                        # time.sleep(0.3) 

                        # keyboard.press_and_release('space')
                        # keyboard.press_and_release('space')
                        # keyboard.press_and_release('space')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('n')
                        # time.sleep(0.3)
                        

                        # pyautogui.click( x_registado_sim, y_registado_sim, button='left', clicks=1, interval=0.25)
                        # time.sleep(0.3) 

                        # keyboard.press_and_release('space')
                        # keyboard.press_and_release('space')
                        # keyboard.press_and_release('space')
                        # time.sleep(0.3)
                        
                        pyautogui.click(x_anterior, y_anterior, button='left', clicks=3, interval=0.25)
                        time.sleep(0.1)  







                if len(linhas) % 3 == 2 or len(linhas) % 3 == 1:
                    print("\nLinhas (linha(s) detectada(s)):")
                    for linha in linhas:
                        print(linha)  
                    
                    encontrou_linha = False

                    for i, linha in enumerate(linhas):
                        if 'por suspeita de fraude' in linha.lower():
                            if 'registad' in linha.lower():
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
                                    time.sleep(4)

                                    pyautogui.click(x_imprimir, y_imprimir, button='left', clicks=1, interval=0.25)
                                    time.sleep(2)


                                    pyautogui.click( x_processamento_sim, y_processamento_sim, button='left', clicks=1, interval=0.25)
                                    time.sleep(4)
                                    pyautogui.click(x_cancelar, y_cancelar, button='left', clicks=1, interval=0.25)
                                    time.sleep(2)

                                    # pyautogui.click(x_registado, y_registado, button='left', clicks=2, interval=0.25)
                                    # time.sleep(2)

                                    # pyautogui.click(x_registado_seguinte, y_registado_seguinte, button='left', clicks=3, interval=0.5)
                                    # time.sleep(3)

                                    # keyboard.press_and_release('space')

                                    # pyautogui.click(x_registado_cmp1, y_registado_cmp1 , button='left', clicks=1, interval=0.25)
                                    # time.sleep(5)

                                    # keyboard.press_and_release('r')
                                    # time.sleep(0.5)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.5)

                                    # keyboard.press_and_release('v')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('2')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('2')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('shift+tab')
                                    # time.sleep(2)

                                    # screenshot = pyautogui.screenshot(region=area2)
                                    # texto_extraido = pytesseract.image_to_string(screenshot)
                                    
                                    # texto_extraido = texto_extraido.strip()  # Remove espaços no início e no fim
                                    # texto_extraido = texto_extraido.replace("\n", "")  # Remove quebras de linha

                                    # # Mostrar o texto extraído para depuração
                                    # print("Texto extraído:\n", texto_extraido)

                                    # # Comparar o texto
                                    # if texto_extraido == "22000 V":
                                    #     keyboard.press_and_release('tab')
                                    #     time.sleep(0.3)
                                    #     keyboard.press_and_release('2')
                                    #     time.sleep(0.3)
                                        
                                    # else:
                                    #     keyboard.press_and_release('tab')
                                    #     time.sleep(0.3)
                                        
                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)
                                    # keyboard.press_and_release('s')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('s')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('r')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('2')
                                    # keyboard.press_and_release('0')
                                    # keyboard.press_and_release('0')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('4')
                                    # keyboard.press_and_release('3')
                                    # time.sleep(0.3)
                
                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('4')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('2')
                                    # keyboard.press_and_release('0')
                                    # keyboard.press_and_release('0')
                                    # time.sleep(1)
                                    
                                    # pyautogui.click(x_registado_cmp_potencia, y_registado_cmp1_potencia, button='left', clicks=1, interval=0.25)
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('2')
                                    # keyboard.press_and_release('.')
                                    # keyboard.press_and_release('2')
                                    # time.sleep(0.3)
                                    
                                    # pyautogui.click(x_propriedade, y_propriedade, button='left', clicks=2, interval=0.25)
                                    # time.sleep(0.3)
                                    
                                    # keyboard.press_and_release('backspace')
                                    # time.sleep(0.3) 

                                    # keyboard.press_and_release('1')
                                    # keyboard.press_and_release('7')
                                    # keyboard.press_and_release('2')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # pyautogui.click(x_gis_x, y_gis_x, button='left', clicks=2, interval=0.25)
                                    # time.sleep(0.3)
                                    
                                    # keyboard.press_and_release('backspace')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('2')
                                    # time.sleep(0.3)

                                    # pyautogui.click(x_gis_y, y_gis_y, button='left', clicks=2, interval=0.25)
                                    # time.sleep(0.3)
                                    
                                    # keyboard.press_and_release('backspace')
                                    # time.sleep(0.3)
                                    
                                    # keyboard.press_and_release('1')
                                    # time.sleep(0.3)

                                    
                                    # pyautogui.click(x_estado_instalacao, y_estado_instalacao, button='left', clicks=1, interval=0.25)
                                    # time.sleep(0.3) 

                                    # keyboard.press_and_release('s')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('s')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('s')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('s')
                                    # time.sleep(0.3)
                                
                                    # pyautogui.click(x_num_luz, y_num_luz , button='left', clicks=1, interval=0.25)
                                    # time.sleep(0.3) 

                                    # keyboard.press_and_release('8')
                                    # time.sleep(1)

                                    # pyautogui.click(x_quartos, y_quartos, button='left', clicks=1, interval=0.25)
                                    # time.sleep(0.3) 

                                    # keyboard.press_and_release('4')
                                    # time.sleep(0.3)
                                    

                                    # pyautogui.click(x_registro, y_registro, button='left', clicks=1, interval=0.25)
                                    # time.sleep(0.3) 

                                    # keyboard.press_and_release('space')
                                    # keyboard.press_and_release('space')
                                    # keyboard.press_and_release('space')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('n')
                                    # time.sleep(0.3)
                                    

                                    # pyautogui.click( x_registado_sim, y_registado_sim, button='left', clicks=1, interval=0.25)
                                    # time.sleep(0.3) 

                                    # keyboard.press_and_release('space')
                                    # keyboard.press_and_release('space')
                                    # keyboard.press_and_release('space')
                                    # time.sleep(0.3)
                                    
                                    pyautogui.click(x_anterior, y_anterior, button='left', clicks=3, interval=0.25)
                                    time.sleep(0.1)
                        


                            # Caso o estado seja "em processamento", retorna ao fluxo principal
                            elif 'em processament' in linha.lower():
                                    # print(f"Linha encontrada (Em Processamento): {linha}")
                                    encontrou_linha = True
                                    contador_em_processamento += 1

                                    match = re.match(r'^\d+', linha)
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
                                        time.sleep(5)

                                        pyautogui.click(x_registado_cmp1, y_registado_cmp1, button='left', clicks=1, interval=0.25)
                                        time.sleep(4)

                                        keyboard.press_and_release('r')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('v')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('2')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('2')
                                        time.sleep(0.3)

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
                                            time.sleep(0.3)
                                            keyboard.press_and_release('2')
                                            time.sleep(0.3)
                                            
                                        else:
                                            keyboard.press_and_release('tab')
                                            time.sleep(0.3)
                                            
                                        keyboard.press_and_release('tab')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('s')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('s')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('r')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('2')
                                        keyboard.press_and_release('0')
                                        keyboard.press_and_release('0')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('4')
                                        keyboard.press_and_release('3')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('4')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('2')
                                        keyboard.press_and_release('0')
                                        keyboard.press_and_release('0')
                                        time.sleep(1)
                                        
                                        pyautogui.click(x_registado_cmp_potencia, y_registado_cmp1_potencia, button='left', clicks=1, interval=0.25)
                                        time.sleep(0.3)

                                        keyboard.press_and_release('2')
                                        keyboard.press_and_release('.')
                                        keyboard.press_and_release('2')
                                        time.sleep(0.3)
                                        
                                        pyautogui.click(x_propriedade, y_propriedade, button='left', clicks=2, interval=0.25)
                                        time.sleep(0.3)
                                        
                                        keyboard.press_and_release('backspace')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('1')
                                        keyboard.press_and_release('7')
                                        keyboard.press_and_release('2')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.3)

                                        pyautogui.click(x_gis_x, y_gis_x, button='left', clicks=2, interval=0.25)
                                        time.sleep(0.3)
                                        
                                        keyboard.press_and_release('backspace')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('2')
                                        time.sleep(0.3)

                                        pyautogui.click(x_gis_y, y_gis_y, button='left', clicks=2, interval=0.25)
                                        time.sleep(0.3)
                                        
                                        keyboard.press_and_release('backspace')
                                        time.sleep(0.3)
                                        
                                        keyboard.press_and_release('1')
                                        time.sleep(0.3)

                                        # pyautogui.click(x_estado_instalacao, y_estado_instalacao, button='left', clicks=1, interval=0.25)
                                        # time.sleep(0.3) 

                                        # keyboard.press_and_release('s')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('tab')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('s')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('tab')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('s')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('tab')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('s')
                                        # time.sleep(0.3)

                                        # pyautogui.click(x_num_luz, y_num_luz, button='left', clicks=1, interval=0.25)
                                        # time.sleep(0.3) 

                                        # keyboard.press_and_release('8')
                                        # time.sleep(1)

                                        # pyautogui.click(x_quartos, y_quartos, button='left', clicks=1, interval=0.25)
                                        # time.sleep(0.3) 

                                        # keyboard.press_and_release('4')
                                        # time.sleep(0.3)

                                        pyautogui.click(x_registro, y_registro, button='left', clicks=1, interval=0.25)
                                        time.sleep(0.3) 

                                        keyboard.press_and_release('space')
                                        keyboard.press_and_release('space')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('n')
                                        time.sleep(0.3)

                                        pyautogui.click(x_registado_sim, y_registado_sim, button='left', clicks=1, interval=0.25)
                                        time.sleep(0.3) 

                                        keyboard.press_and_release('space')
                                        keyboard.press_and_release('space')
                                        time.sleep(0.3)

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
                        
                        # pyautogui.click(x_processamento,y_processamento, button='left', clicks=2, interval=0.25)
                        # time.sleep(1)

                        # pyautogui.click(x_processamento_seguinte, y_processamento_seguinte, button='left', clicks=1, interval=0.25)
                        # time.sleep(4)

                        # pyautogui.click(x_imprimir, y_imprimir, button='left', clicks=1, interval=0.25)
                        # time.sleep(2)


                        # pyautogui.click( x_processamento_sim, y_processamento_sim, button='left', clicks=1, interval=0.25)
                        # time.sleep(4)

                        # pyautogui.click(x_cancelar, y_cancelar, button='left', clicks=1, interval=0.25)
                        # time.sleep(2)

                        # pyautogui.click(x_registado, y_registado, button='left', clicks=2, interval=0.25)
                        # time.sleep(2)

                        # pyautogui.click(x_registado_seguinte, y_registado_seguinte, button='left', clicks=3, interval=0.5)
                        # time.sleep(3)

                        # keyboard.press_and_release('space')

                        # pyautogui.click(x_registado_cmp1, y_registado_cmp1 , button='left', clicks=1, interval=0.25)
                        # time.sleep(5)

                        # keyboard.press_and_release('r')
                        # time.sleep(0.5)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.5)

                        # keyboard.press_and_release('v')
                        # time.sleep(0.5)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('2')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('2')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('shift+tab')
                        # time.sleep(2)

                        # screenshot = pyautogui.screenshot(region=area2)
                        # texto_extraido = pytesseract.image_to_string(screenshot)
                        
                        # texto_extraido = texto_extraido.strip()  # Remove espaços no início e no fim
                        # texto_extraido = texto_extraido.replace("\n", "")  # Remove quebras de linha

                        # # Mostrar o texto extraído para depuração
                        # print("Texto extraído:\n", texto_extraido)

                        # # Comparar o texto
                        # if texto_extraido == "22000 V":
                        #     keyboard.press_and_release('tab')
                        #     time.sleep(0.3)
                        #     keyboard.press_and_release('2')
                        #     time.sleep(0.3)
                            
                        # else:
                        #     keyboard.press_and_release('tab')
                        #     time.sleep(0.3)
                            
                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)
                        # keyboard.press_and_release('s')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('s')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('r')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('2')
                        # keyboard.press_and_release('0')
                        # keyboard.press_and_release('0')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('4')
                        # keyboard.press_and_release('3')
                        # time.sleep(0.3)
    
                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('4')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('2')
                        # keyboard.press_and_release('0')
                        # keyboard.press_and_release('0')
                        # time.sleep(1)
                        
                        # pyautogui.click(x_registado_cmp_potencia, y_registado_cmp1_potencia, button='left', clicks=1, interval=0.25)
                        # time.sleep(0.3)

                        # keyboard.press_and_release('2')
                        # keyboard.press_and_release('.')
                        # keyboard.press_and_release('2')
                        # time.sleep(0.3)
                        
                        # pyautogui.click(x_propriedade, y_propriedade, button='left', clicks=2, interval=0.25)
                        # time.sleep(0.3)
                        
                        # keyboard.press_and_release('backspace')
                        # time.sleep(0.3) 

                        # keyboard.press_and_release('1')
                        # keyboard.press_and_release('7')
                        # keyboard.press_and_release('2')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # pyautogui.click(x_gis_x, y_gis_x, button='left', clicks=2, interval=0.25)
                        # time.sleep(0.3)
                        
                        # keyboard.press_and_release('backspace')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('2')
                        # time.sleep(0.3)

                        # pyautogui.click(x_gis_y, y_gis_y, button='left', clicks=2, interval=0.25)
                        # time.sleep(0.3)
                        
                        # keyboard.press_and_release('backspace')
                        # time.sleep(0.3)
                        
                        # keyboard.press_and_release('1')
                        # time.sleep(0.3)

                        
                        # pyautogui.click(x_estado_instalacao, y_estado_instalacao, button='left', clicks=1, interval=0.25)
                        # time.sleep(0.3) 

                        # keyboard.press_and_release('s')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('s')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('s')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('s')
                        # time.sleep(0.3)
                    
                        # pyautogui.click(x_num_luz, y_num_luz , button='left', clicks=1, interval=0.25)
                        # time.sleep(0.3) 

                        # keyboard.press_and_release('8')
                        # time.sleep(1)

                        # pyautogui.click(x_quartos, y_quartos, button='left', clicks=1, interval=0.25)
                        # time.sleep(0.3) 

                        # keyboard.press_and_release('4')
                        # time.sleep(0.3)
                        

                        # pyautogui.click(x_registro, y_registro, button='left', clicks=1, interval=0.25)
                        # time.sleep(0.3) 

                        # keyboard.press_and_release('space')
                        # keyboard.press_and_release('space')
                        # keyboard.press_and_release('space')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('n')
                        # time.sleep(0.3)
                        

                        # pyautogui.click( x_registado_sim, y_registado_sim, button='left', clicks=1, interval=0.25)
                        # time.sleep(0.3) 

                        # keyboard.press_and_release('space')
                        # keyboard.press_and_release('space')
                        # keyboard.press_and_release('space')
                        # time.sleep(0.3)
                        
                        pyautogui.click(x_anterior, y_anterior, button='left', clicks=3, interval=0.25)
                        time.sleep(0.1)  







        else:
            if len(linhas) % 3 == 0:
                if len(linhas) <= 3:    
        # Caso especial: se há exatamente 3 linhas, não combinar, apenas exibir
                    print("\nLinhas (3 linhas detectadas):")
                    for linha in linhas:
                        print(linha)
                    
                    encontrou_linha = False

                    for i, linha in enumerate(linhas):
                        if 'por suspeita de fraude' in linha.lower():
                            if 'registad' in linha.lower():
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
                                    time.sleep(4)

                                    pyautogui.click(x_imprimir, y_imprimir, button='left', clicks=1, interval=0.25)
                                    time.sleep(2)


                                    pyautogui.click( x_processamento_sim, y_processamento_sim, button='left', clicks=1, interval=0.25)
                                    time.sleep(4)

                                    pyautogui.click(x_cancelar, y_cancelar, button='left', clicks=1, interval=0.25)
                                    time.sleep(2)

                                    # pyautogui.click(x_registado, y_registado, button='left', clicks=2, interval=0.25)
                                    # time.sleep(2)

                                    # pyautogui.click(x_registado_seguinte, y_registado_seguinte, button='left', clicks=3, interval=0.5)
                                    # time.sleep(3)

                                    # keyboard.press_and_release('space')

                                    # pyautogui.click(x_registado_cmp1, y_registado_cmp1 , button='left', clicks=1, interval=0.25)
                                    # time.sleep(5)

                                    # keyboard.press_and_release('r')
                                    # time.sleep(0.5)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.5)

                                    # keyboard.press_and_release('v')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('2')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('2')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('shift+tab')
                                    # time.sleep(2)

                                    # screenshot = pyautogui.screenshot(region=area2)
                                    # texto_extraido = pytesseract.image_to_string(screenshot)
                                    
                                    # texto_extraido = texto_extraido.strip()  # Remove espaços no início e no fim
                                    # texto_extraido = texto_extraido.replace("\n", "")  # Remove quebras de linha

                                    # # Mostrar o texto extraído para depuração
                                    # print("Texto extraído:\n", texto_extraido)

                                    # # Comparar o texto
                                    # if texto_extraido == "22000 V":
                                    #     keyboard.press_and_release('tab')
                                    #     time.sleep(0.3)
                                    #     keyboard.press_and_release('2')
                                    #     time.sleep(0.3)
                                        
                                    # else:
                                    #     keyboard.press_and_release('tab')
                                    #     time.sleep(0.3)
                                        
                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)
                                    # keyboard.press_and_release('s')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('s')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('r')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('2')
                                    # keyboard.press_and_release('0')
                                    # keyboard.press_and_release('0')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('4')
                                    # keyboard.press_and_release('3')
                                    # time.sleep(0.3)
                
                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('4')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('2')
                                    # keyboard.press_and_release('0')
                                    # keyboard.press_and_release('0')
                                    # time.sleep(1)
                                    
                                    # pyautogui.click(x_registado_cmp_potencia, y_registado_cmp1_potencia, button='left', clicks=1, interval=0.25)
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('2')
                                    # keyboard.press_and_release('.')
                                    # keyboard.press_and_release('2')
                                    # time.sleep(0.3)
                                    
                                    # pyautogui.click(x_propriedade, y_propriedade, button='left', clicks=2, interval=0.25)
                                    # time.sleep(0.3)
                                    
                                    # keyboard.press_and_release('backspace')
                                    # time.sleep(0.3) 

                                    # keyboard.press_and_release('1')
                                    # keyboard.press_and_release('7')
                                    # keyboard.press_and_release('2')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # pyautogui.click(x_gis_x, y_gis_x, button='left', clicks=2, interval=0.25)
                                    # time.sleep(0.3)
                                    
                                    # keyboard.press_and_release('backspace')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('2')
                                    # time.sleep(0.3)

                                    # pyautogui.click(x_gis_y, y_gis_y, button='left', clicks=2, interval=0.25)
                                    # time.sleep(0.3)
                                    
                                    # keyboard.press_and_release('backspace')
                                    # time.sleep(0.3)
                                    
                                    # keyboard.press_and_release('1')
                                    # time.sleep(0.3)

                                    
                                    # pyautogui.click(x_estado_instalacao, y_estado_instalacao, button='left', clicks=1, interval=0.25)
                                    # time.sleep(0.3) 

                                    # keyboard.press_and_release('s')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('s')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('s')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('s')
                                    # time.sleep(0.3)
                                
                                    # pyautogui.click(x_num_luz, y_num_luz , button='left', clicks=1, interval=0.25)
                                    # time.sleep(0.3) 

                                    # keyboard.press_and_release('8')
                                    # time.sleep(1)

                                    # pyautogui.click(x_quartos, y_quartos, button='left', clicks=1, interval=0.25)
                                    # time.sleep(0.3) 

                                    # keyboard.press_and_release('4')
                                    # time.sleep(0.3)
                                    

                                    # pyautogui.click(x_registro, y_registro, button='left', clicks=1, interval=0.25)
                                    # time.sleep(0.3) 

                                    # keyboard.press_and_release('space')
                                    # keyboard.press_and_release('space')
                                    # keyboard.press_and_release('space')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('n')
                                    # time.sleep(0.3)
                                    

                                    # pyautogui.click( x_registado_sim, y_registado_sim, button='left', clicks=1, interval=0.25)
                                    # time.sleep(0.3) 

                                    # keyboard.press_and_release('space')
                                    # keyboard.press_and_release('space')
                                    # keyboard.press_and_release('space')
                                    # time.sleep(0.3)
                                    
                                    pyautogui.click(x_anterior, y_anterior, button='left', clicks=3, interval=0.25)
                                    time.sleep(0.1)

                                    
                            elif 'em processament' in linha.lower():
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
                                    time.sleep(5)

                                    pyautogui.click(x_registado_cmp1, y_registado_cmp1, button='left', clicks=1, interval=0.25)
                                    time.sleep(2)

                                    keyboard.press_and_release('r')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('v')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('2')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('2')
                                    time.sleep(0.3)

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
                                        time.sleep(0.3)
                                        keyboard.press_and_release('2')
                                        time.sleep(0.3)
                                        
                                    else:
                                        keyboard.press_and_release('tab')
                                        time.sleep(0.3)
                                        
                                    keyboard.press_and_release('tab')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('s')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('s')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('r')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('2')
                                    keyboard.press_and_release('0')
                                    keyboard.press_and_release('0')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('4')
                                    keyboard.press_and_release('3')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('4')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('2')
                                    keyboard.press_and_release('0')
                                    keyboard.press_and_release('0')
                                    time.sleep(1)
                                    
                                    pyautogui.click(x_registado_cmp_potencia, y_registado_cmp1_potencia, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.3)

                                    keyboard.press_and_release('2')
                                    keyboard.press_and_release('.')
                                    keyboard.press_and_release('2')
                                    time.sleep(0.3)
                                    
                                    pyautogui.click(x_propriedade, y_propriedade, button='left', clicks=2, interval=0.25)
                                    time.sleep(0.3)
                                    
                                    keyboard.press_and_release('backspace')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('1')
                                    keyboard.press_and_release('7')
                                    keyboard.press_and_release('2')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.3)

                                    pyautogui.click(x_gis_x, y_gis_x, button='left', clicks=2, interval=0.25)
                                    time.sleep(0.3)
                                    
                                    keyboard.press_and_release('backspace')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('2')
                                    time.sleep(0.3)

                                    pyautogui.click(x_gis_y, y_gis_y, button='left', clicks=2, interval=0.25)
                                    time.sleep(0.3)
                                    
                                    keyboard.press_and_release('backspace')
                                    time.sleep(0.3)
                                    
                                    keyboard.press_and_release('1')
                                    time.sleep(0.3)

                                    # pyautogui.click(x_estado_instalacao, y_estado_instalacao, button='left', clicks=1, interval=0.25)
                                    # time.sleep(0.3) 

                                    # keyboard.press_and_release('s')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('s')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('s')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('s')
                                    # time.sleep(0.3)

                                    # pyautogui.click(x_num_luz, y_num_luz, button='left', clicks=1, interval=0.25)
                                    # time.sleep(0.3) 

                                    # keyboard.press_and_release('8')
                                    # time.sleep(1)

                                    # pyautogui.click(x_quartos, y_quartos, button='left', clicks=1, interval=0.25)
                                    # time.sleep(0.3) 

                                    # keyboard.press_and_release('4')
                                    # time.sleep(0.3)

                                    pyautogui.click(x_registro, y_registro, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.3) 

                                    keyboard.press_and_release('space')
                                    keyboard.press_and_release('space')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('n')
                                    time.sleep(0.3)

                                    pyautogui.click(x_registado_sim, y_registado_sim, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.3) 

                                    keyboard.press_and_release('space')
                                    keyboard.press_and_release('space')
                                    time.sleep(0.3)

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

                        # pyautogui.click(x_processamento,y_processamento, button='left', clicks=2, interval=0.25)
                        # time.sleep(1)

                        # pyautogui.click(x_processamento_seguinte, y_processamento_seguinte, button='left', clicks=1, interval=0.25)
                        # time.sleep(4)

                        # pyautogui.click(x_imprimir, y_imprimir, button='left', clicks=1, interval=0.25)
                        # time.sleep(2)


                        # pyautogui.click( x_processamento_sim, y_processamento_sim, button='left', clicks=1, interval=0.25)
                        # time.sleep(4)
                        # pyautogui.click(x_cancelar, y_cancelar, button='left', clicks=1, interval=0.25)
                        # time.sleep(2)

                        # pyautogui.click(x_registado, y_registado, button='left', clicks=2, interval=0.25)
                        # time.sleep(2)

                        # pyautogui.click(x_registado_seguinte, y_registado_seguinte, button='left', clicks=3, interval=0.5)
                        # time.sleep(3)

                        # keyboard.press_and_release('space')

                        # pyautogui.click(x_registado_cmp1, y_registado_cmp1 , button='left', clicks=1, interval=0.25)
                        # time.sleep(5)

                        # keyboard.press_and_release('r')
                        # time.sleep(0.5)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.5)

                        # keyboard.press_and_release('v')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('2')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('2')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('shift+tab')
                        # time.sleep(2)

                        # screenshot = pyautogui.screenshot(region=area2)
                        # texto_extraido = pytesseract.image_to_string(screenshot)
                        
                        # texto_extraido = texto_extraido.strip()  # Remove espaços no início e no fim
                        # texto_extraido = texto_extraido.replace("\n", "")  # Remove quebras de linha

                        # # Mostrar o texto extraído para depuração
                        # print("Texto extraído:\n", texto_extraido)

                        # # Comparar o texto
                        # if texto_extraido == "22000 V":
                        #     keyboard.press_and_release('tab')
                        #     time.sleep(0.3)
                        #     keyboard.press_and_release('2')
                        #     time.sleep(0.3)
                            
                        # else:
                        #     keyboard.press_and_release('tab')
                        #     time.sleep(0.3)
                            
                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)
                        # keyboard.press_and_release('s')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('s')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('r')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('2')
                        # keyboard.press_and_release('0')
                        # keyboard.press_and_release('0')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('4')
                        # keyboard.press_and_release('3')
                        # time.sleep(0.3)
    
                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('4')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('2')
                        # keyboard.press_and_release('0')
                        # keyboard.press_and_release('0')
                        # time.sleep(1)
                        
                        # pyautogui.click(x_registado_cmp_potencia, y_registado_cmp1_potencia, button='left', clicks=1, interval=0.25)
                        # time.sleep(0.3)

                        # keyboard.press_and_release('2')
                        # keyboard.press_and_release('.')
                        # keyboard.press_and_release('2')
                        # time.sleep(0.3)
                        
                        # pyautogui.click(x_propriedade, y_propriedade, button='left', clicks=2, interval=0.25)
                        # time.sleep(0.3)
                        
                        # keyboard.press_and_release('backspace')
                        # time.sleep(0.3) 

                        # keyboard.press_and_release('1')
                        # keyboard.press_and_release('7')
                        # keyboard.press_and_release('2')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # pyautogui.click(x_gis_x, y_gis_x, button='left', clicks=2, interval=0.25)
                        # time.sleep(0.3)
                        
                        # keyboard.press_and_release('backspace')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('2')
                        # time.sleep(0.3)

                        # pyautogui.click(x_gis_y, y_gis_y, button='left', clicks=2, interval=0.25)
                        # time.sleep(0.3)
                        
                        # keyboard.press_and_release('backspace')
                        # time.sleep(0.3)
                        
                        # keyboard.press_and_release('1')
                        # time.sleep(0.3)

                        
                        # pyautogui.click(x_estado_instalacao, y_estado_instalacao, button='left', clicks=1, interval=0.25)
                        # time.sleep(0.3) 

                        # keyboard.press_and_release('s')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('s')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('s')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('s')
                        # time.sleep(0.3)
                    
                        # pyautogui.click(x_num_luz, y_num_luz , button='left', clicks=1, interval=0.25)
                        # time.sleep(0.3) 

                        # keyboard.press_and_release('8')
                        # time.sleep(1)

                        # pyautogui.click(x_quartos, y_quartos, button='left', clicks=1, interval=0.25)
                        # time.sleep(0.3) 

                        # keyboard.press_and_release('4')
                        # time.sleep(0.3)
                        

                        # pyautogui.click(x_registro, y_registro, button='left', clicks=1, interval=0.25)
                        # time.sleep(0.3) 

                        # keyboard.press_and_release('space')
                        # keyboard.press_and_release('space')
                        # keyboard.press_and_release('space')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('tab')
                        # time.sleep(0.3)

                        # keyboard.press_and_release('n')
                        # time.sleep(0.3)
                        

                        # pyautogui.click( x_registado_sim, y_registado_sim, button='left', clicks=1, interval=0.25)
                        # time.sleep(0.3) 

                        # keyboard.press_and_release('space')
                        # keyboard.press_and_release('space')
                        # keyboard.press_and_release('space')
                        # time.sleep(0.3)
                        
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
                        if 'por suspeita de fraude' in linha.lower():
                            if 'registad' in linha.lower():
                                print(f"Linha encontrada (Registado): {linha}")
                                encontrou_linha = True
                                contador_registados +=1

                                # Extrair o número da O.T. usando regex (números no início da linha)
                                match = re.match(r'^\d+', linha)
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
                                    time.sleep(4)

                                    pyautogui.click(x_imprimir, y_imprimir, button='left', clicks=1, interval=0.25)
                                    time.sleep(2)


                                    pyautogui.click( x_processamento_sim, y_processamento_sim, button='left', clicks=1, interval=0.25)
                                    time.sleep(4)

                                    pyautogui.click(x_cancelar, y_cancelar, button='left', clicks=1, interval=0.25)
                                    time.sleep(2)

                                    # pyautogui.click(x_registado, y_registado, button='left', clicks=2, interval=0.25)
                                    # time.sleep(2)

                                    # pyautogui.click(x_registado_seguinte, y_registado_seguinte, button='left', clicks=3, interval=0.5)
                                    # time.sleep(3)

                                    # keyboard.press_and_release('space')

                                    # pyautogui.click(x_registado_cmp1, y_registado_cmp1 , button='left', clicks=1, interval=0.25)
                                    # time.sleep(5)

                                    # keyboard.press_and_release('r')
                                    # time.sleep(0.5)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.5)

                                    # keyboard.press_and_release('v')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('2')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('2')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('shift+tab')
                                    # time.sleep(2)

                                    # screenshot = pyautogui.screenshot(region=area2)
                                    # texto_extraido = pytesseract.image_to_string(screenshot)
                                    
                                    # texto_extraido = texto_extraido.strip()  # Remove espaços no início e no fim
                                    # texto_extraido = texto_extraido.replace("\n", "")  # Remove quebras de linha

                                    # # Mostrar o texto extraído para depuração
                                    # print("Texto extraído:\n", texto_extraido)

                                    # # Comparar o texto
                                    # if texto_extraido == "22000 V":
                                    #     keyboard.press_and_release('tab')
                                    #     time.sleep(0.3)
                                    #     keyboard.press_and_release('2')
                                    #     time.sleep(0.3)
                                        
                                    # else:
                                    #     keyboard.press_and_release('tab')
                                    #     time.sleep(0.3)
                                        
                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)
                                    # keyboard.press_and_release('s')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('s')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('r')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('2')
                                    # keyboard.press_and_release('0')
                                    # keyboard.press_and_release('0')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('4')
                                    # keyboard.press_and_release('3')
                                    # time.sleep(0.3)
                
                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('4')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('2')
                                    # keyboard.press_and_release('0')
                                    # keyboard.press_and_release('0')
                                    # time.sleep(1)
                                    
                                    # pyautogui.click(x_registado_cmp_potencia, y_registado_cmp1_potencia, button='left', clicks=1, interval=0.25)
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('2')
                                    # keyboard.press_and_release('.')
                                    # keyboard.press_and_release('2')
                                    # time.sleep(0.3)
                                    
                                    # pyautogui.click(x_propriedade, y_propriedade, button='left', clicks=2, interval=0.25)
                                    # time.sleep(0.3)
                                    
                                    # keyboard.press_and_release('backspace')
                                    # time.sleep(0.3) 

                                    # keyboard.press_and_release('1')
                                    # keyboard.press_and_release('7')
                                    # keyboard.press_and_release('2')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # pyautogui.click(x_gis_x, y_gis_x, button='left', clicks=2, interval=0.25)
                                    # time.sleep(0.3)
                                    
                                    # keyboard.press_and_release('backspace')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('2')
                                    # time.sleep(0.3)

                                    # pyautogui.click(x_gis_y, y_gis_y, button='left', clicks=2, interval=0.25)
                                    # time.sleep(0.3)
                                    
                                    # keyboard.press_and_release('backspace')
                                    # time.sleep(0.3)
                                    
                                    # keyboard.press_and_release('1')
                                    # time.sleep(0.3)

                                    
                                    # pyautogui.click(x_estado_instalacao, y_estado_instalacao, button='left', clicks=1, interval=0.25)
                                    # time.sleep(0.3) 

                                    # keyboard.press_and_release('s')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('s')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('s')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('s')
                                    # time.sleep(0.3)
                                
                                    # pyautogui.click(x_num_luz, y_num_luz , button='left', clicks=1, interval=0.25)
                                    # time.sleep(0.3) 

                                    # keyboard.press_and_release('8')
                                    # time.sleep(1)

                                    # pyautogui.click(x_quartos, y_quartos, button='left', clicks=1, interval=0.25)
                                    # time.sleep(0.3) 

                                    # keyboard.press_and_release('4')
                                    # time.sleep(0.3)
                                    

                                    # pyautogui.click(x_registro, y_registro, button='left', clicks=1, interval=0.25)
                                    # time.sleep(0.3) 

                                    # keyboard.press_and_release('space')
                                    # keyboard.press_and_release('space')
                                    # keyboard.press_and_release('space')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('n')
                                    # time.sleep(0.3)
                                    

                                    # pyautogui.click( x_registado_sim, y_registado_sim, button='left', clicks=1, interval=0.25)
                                    # time.sleep(0.3) 

                                    # keyboard.press_and_release('space')
                                    # keyboard.press_and_release('space')
                                    # keyboard.press_and_release('space')
                                    # time.sleep(0.3)
                                    
                                    pyautogui.click(x_anterior, y_anterior, button='left', clicks=3, interval=0.25)
                                    time.sleep(0.1)
                            


                        # Caso o estado seja "em processamento", retorna ao fluxo principal
                            elif 'em processament' in linha.lower():
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
                                    time.sleep(5)

                                    pyautogui.click(x_registado_cmp1, y_registado_cmp1, button='left', clicks=1, interval=0.25)
                                    time.sleep(2)

                                    keyboard.press_and_release('r')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('v')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('2')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('2')
                                    time.sleep(0.3)

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
                                        time.sleep(0.3)
                                        keyboard.press_and_release('2')
                                        time.sleep(0.3)
                                        
                                    else:
                                        keyboard.press_and_release('tab')
                                        time.sleep(0.3)
                                        
                                    keyboard.press_and_release('tab')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('s')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('s')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('r')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('2')
                                    keyboard.press_and_release('0')
                                    keyboard.press_and_release('0')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('4')
                                    keyboard.press_and_release('3')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('4')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('2')
                                    keyboard.press_and_release('0')
                                    keyboard.press_and_release('0')
                                    time.sleep(1)
                                    
                                    pyautogui.click(x_registado_cmp_potencia, y_registado_cmp1_potencia, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.3)

                                    keyboard.press_and_release('2')
                                    keyboard.press_and_release('.')
                                    keyboard.press_and_release('2')
                                    time.sleep(0.3)
                                    
                                    pyautogui.click(x_propriedade, y_propriedade, button='left', clicks=2, interval=0.25)
                                    time.sleep(0.3)
                                    
                                    keyboard.press_and_release('backspace')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('1')
                                    keyboard.press_and_release('7')
                                    keyboard.press_and_release('2')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.3)

                                    pyautogui.click(x_gis_x, y_gis_x, button='left', clicks=2, interval=0.25)
                                    time.sleep(0.3)
                                    
                                    keyboard.press_and_release('backspace')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('2')
                                    time.sleep(0.3)

                                    pyautogui.click(x_gis_y, y_gis_y, button='left', clicks=2, interval=0.25)
                                    time.sleep(0.3)
                                    
                                    keyboard.press_and_release('backspace')
                                    time.sleep(0.3)
                                    
                                    keyboard.press_and_release('1')
                                    time.sleep(0.3)

                                    # pyautogui.click(x_estado_instalacao, y_estado_instalacao, button='left', clicks=1, interval=0.25)
                                    # time.sleep(0.3) 

                                    # keyboard.press_and_release('s')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('s')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('s')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('tab')
                                    # time.sleep(0.3)

                                    # keyboard.press_and_release('s')
                                    # time.sleep(0.3)

                                    # pyautogui.click(x_num_luz, y_num_luz, button='left', clicks=1, interval=0.25)
                                    # time.sleep(0.3) 

                                    # keyboard.press_and_release('8')
                                    # time.sleep(1)

                                    # pyautogui.click(x_quartos, y_quartos, button='left', clicks=1, interval=0.25)
                                    # time.sleep(0.3) 

                                    # keyboard.press_and_release('4')
                                    # time.sleep(0.3)

                                    pyautogui.click(x_registro, y_registro, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.3) 

                                    keyboard.press_and_release('space')
                                    keyboard.press_and_release('space')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('tab')
                                    time.sleep(0.3)

                                    keyboard.press_and_release('n')
                                    time.sleep(0.3)

                                    pyautogui.click(x_registado_sim, y_registado_sim, button='left', clicks=1, interval=0.25)
                                    time.sleep(0.3) 

                                    keyboard.press_and_release('space')
                                    keyboard.press_and_release('space')
                                    time.sleep(0.3)

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
                            if 'por suspeita de fraude' in linha.lower():
                                if 'registad' in linha.lower():
                                    print(f"Linha encontrada (Registado): {linha}")
                                    encontrou_linha = True
                                    contador_registados +=1

                                    # Extrair o número da O.T. usando regex (números no início da linha)
                                    match = re.match(r'^\d+', linha)
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
                                        time.sleep(4)

                                        pyautogui.click(x_imprimir, y_imprimir, button='left', clicks=1, interval=0.25)
                                        time.sleep(2)


                                        pyautogui.click( x_processamento_sim, y_processamento_sim, button='left', clicks=1, interval=0.25)
                                        time.sleep(4)
                                        pyautogui.click(x_cancelar, y_cancelar, button='left', clicks=1, interval=0.25)
                                        time.sleep(2)

                                        # pyautogui.click(x_registado, y_registado, button='left', clicks=2, interval=0.25)
                                        # time.sleep(2)

                                        # pyautogui.click(x_registado_seguinte, y_registado_seguinte, button='left', clicks=3, interval=0.5)
                                        # time.sleep(3)

                                        # keyboard.press_and_release('space')

                                        # pyautogui.click(x_registado_cmp1, y_registado_cmp1 , button='left', clicks=1, interval=0.25)
                                        # time.sleep(5)

                                        # keyboard.press_and_release('r')
                                        # time.sleep(0.5)

                                        # keyboard.press_and_release('tab')
                                        # time.sleep(0.5)

                                        # keyboard.press_and_release('v')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('tab')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('2')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('tab')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('2')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('shift+tab')
                                        # time.sleep(2)

                                        # screenshot = pyautogui.screenshot(region=area2)
                                        # texto_extraido = pytesseract.image_to_string(screenshot)
                                        
                                        # texto_extraido = texto_extraido.strip()  # Remove espaços no início e no fim
                                        # texto_extraido = texto_extraido.replace("\n", "")  # Remove quebras de linha

                                        # # Mostrar o texto extraído para depuração
                                        # print("Texto extraído:\n", texto_extraido)

                                        # # Comparar o texto
                                        # if texto_extraido == "22000 V":
                                        #     keyboard.press_and_release('tab')
                                        #     time.sleep(0.3)
                                        #     keyboard.press_and_release('2')
                                        #     time.sleep(0.3)
                                            
                                        # else:
                                        #     keyboard.press_and_release('tab')
                                        #     time.sleep(0.3)
                                            
                                        # keyboard.press_and_release('tab')
                                        # time.sleep(0.3)
                                        # keyboard.press_and_release('s')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('tab')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('s')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('tab')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('r')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('tab')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('2')
                                        # keyboard.press_and_release('0')
                                        # keyboard.press_and_release('0')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('tab')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('4')
                                        # keyboard.press_and_release('3')
                                        # time.sleep(0.3)
                    
                                        # keyboard.press_and_release('tab')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('4')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('tab')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('2')
                                        # keyboard.press_and_release('0')
                                        # keyboard.press_and_release('0')
                                        # time.sleep(1)
                                        
                                        # pyautogui.click(x_registado_cmp_potencia, y_registado_cmp1_potencia, button='left', clicks=1, interval=0.25)
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('2')
                                        # keyboard.press_and_release('.')
                                        # keyboard.press_and_release('2')
                                        # time.sleep(0.3)
                                        
                                        # pyautogui.click(x_propriedade, y_propriedade, button='left', clicks=2, interval=0.25)
                                        # time.sleep(0.3)
                                        
                                        # keyboard.press_and_release('backspace')
                                        # time.sleep(0.3) 

                                        # keyboard.press_and_release('1')
                                        # keyboard.press_and_release('7')
                                        # keyboard.press_and_release('2')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('tab')
                                        # time.sleep(0.3)

                                        # pyautogui.click(x_gis_x, y_gis_x, button='left', clicks=2, interval=0.25)
                                        # time.sleep(0.3)
                                        
                                        # keyboard.press_and_release('backspace')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('2')
                                        # time.sleep(0.3)

                                        # pyautogui.click(x_gis_y, y_gis_y, button='left', clicks=2, interval=0.25)
                                        # time.sleep(0.3)
                                        
                                        # keyboard.press_and_release('backspace')
                                        # time.sleep(0.3)
                                        
                                        # keyboard.press_and_release('1')
                                        # time.sleep(0.3)

                                        
                                        # pyautogui.click(x_estado_instalacao, y_estado_instalacao, button='left', clicks=1, interval=0.25)
                                        # time.sleep(0.3) 

                                        # keyboard.press_and_release('s')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('tab')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('s')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('tab')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('s')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('tab')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('s')
                                        # time.sleep(0.3)
                                    
                                        # pyautogui.click(x_num_luz, y_num_luz , button='left', clicks=1, interval=0.25)
                                        # time.sleep(0.3) 

                                        # keyboard.press_and_release('8')
                                        # time.sleep(1)

                                        # pyautogui.click(x_quartos, y_quartos, button='left', clicks=1, interval=0.25)
                                        # time.sleep(0.3) 

                                        # keyboard.press_and_release('4')
                                        # time.sleep(0.3)
                                        

                                        # pyautogui.click(x_registro, y_registro, button='left', clicks=1, interval=0.25)
                                        # time.sleep(0.3) 

                                        # keyboard.press_and_release('space')
                                        # keyboard.press_and_release('space')
                                        # keyboard.press_and_release('space')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('tab')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('n')
                                        # time.sleep(0.3)
                                        

                                        # pyautogui.click( x_registado_sim, y_registado_sim, button='left', clicks=1, interval=0.25)
                                        # time.sleep(0.3) 

                                        # keyboard.press_and_release('space')
                                        # keyboard.press_and_release('space')
                                        # keyboard.press_and_release('space')
                                        # time.sleep(0.3)
                                        
                                        pyautogui.click(x_anterior, y_anterior, button='left', clicks=3, interval=0.25)
                                        time.sleep(0.1)
                                


                            # Caso o estado seja "em processamento", retorna ao fluxo principal
                                elif 'em processament' in linha.lower():
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
                                        time.sleep(5)

                                        pyautogui.click(x_registado_cmp1, y_registado_cmp1, button='left', clicks=1, interval=0.25)
                                        time.sleep(2)

                                        keyboard.press_and_release('r')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('v')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('2')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('2')
                                        time.sleep(0.3)

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
                                            time.sleep(0.3)
                                            keyboard.press_and_release('2')
                                            time.sleep(0.3)
                                            
                                        else:
                                            keyboard.press_and_release('tab')
                                            time.sleep(0.3)
                                            
                                        keyboard.press_and_release('tab')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('s')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('s')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('r')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('2')
                                        keyboard.press_and_release('0')
                                        keyboard.press_and_release('0')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('4')
                                        keyboard.press_and_release('3')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('4')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('2')
                                        keyboard.press_and_release('0')
                                        keyboard.press_and_release('0')
                                        time.sleep(1)
                                        
                                        pyautogui.click(x_registado_cmp_potencia, y_registado_cmp1_potencia, button='left', clicks=1, interval=0.25)
                                        time.sleep(0.3)

                                        keyboard.press_and_release('2')
                                        keyboard.press_and_release('.')
                                        keyboard.press_and_release('2')
                                        time.sleep(0.3)
                                        
                                        pyautogui.click(x_propriedade, y_propriedade, button='left', clicks=2, interval=0.25)
                                        time.sleep(0.3)
                                        
                                        keyboard.press_and_release('backspace')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('1')
                                        keyboard.press_and_release('7')
                                        keyboard.press_and_release('2')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.3)

                                        pyautogui.click(x_gis_x, y_gis_x, button='left', clicks=2, interval=0.25)
                                        time.sleep(0.3)
                                        
                                        keyboard.press_and_release('backspace')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('2')
                                        time.sleep(0.3)

                                        pyautogui.click(x_gis_y, y_gis_y, button='left', clicks=2, interval=0.25)
                                        time.sleep(0.3)
                                        
                                        keyboard.press_and_release('backspace')
                                        time.sleep(0.3)
                                        
                                        keyboard.press_and_release('1')
                                        time.sleep(0.3)

                                        # pyautogui.click(x_estado_instalacao, y_estado_instalacao, button='left', clicks=1, interval=0.25)
                                        # time.sleep(0.3) 

                                        # keyboard.press_and_release('s')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('tab')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('s')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('tab')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('s')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('tab')
                                        # time.sleep(0.3)

                                        # keyboard.press_and_release('s')
                                        # time.sleep(0.3)

                                        # pyautogui.click(x_num_luz, y_num_luz, button='left', clicks=1, interval=0.25)
                                        # time.sleep(0.3) 

                                        # keyboard.press_and_release('8')
                                        # time.sleep(1)

                                        # pyautogui.click(x_quartos, y_quartos, button='left', clicks=1, interval=0.25)
                                        # time.sleep(0.3) 

                                        # keyboard.press_and_release('4')
                                        # time.sleep(0.3)

                                        pyautogui.click(x_registro, y_registro, button='left', clicks=1, interval=0.25)
                                        time.sleep(0.3) 

                                        keyboard.press_and_release('space')
                                        keyboard.press_and_release('space')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('tab')
                                        time.sleep(0.3)

                                        keyboard.press_and_release('n')
                                        time.sleep(0.3)

                                        pyautogui.click(x_registado_sim, y_registado_sim, button='left', clicks=1, interval=0.25)
                                        time.sleep(0.3) 

                                        keyboard.press_and_release('space')
                                        keyboard.press_and_release('space')
                                        time.sleep(0.3)

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
                            
                            # pyautogui.click(x_processamento,y_processamento, button='left', clicks=2, interval=0.25)
                            # time.sleep(1)

                            # pyautogui.click(x_processamento_seguinte, y_processamento_seguinte, button='left', clicks=1, interval=0.25)
                            # time.sleep(4)

                            # pyautogui.click(x_imprimir, y_imprimir, button='left', clicks=1, interval=0.25)
                            # time.sleep(2)

                            # pyautogui.click( x_processamento_sim, y_processamento_sim, button='left', clicks=1, interval=0.25)
                            # time.sleep(4)

                            # pyautogui.click(x_cancelar, y_cancelar, button='left', clicks=1, interval=0.25)
                            # time.sleep(2)

                            # pyautogui.click(x_registado, y_registado, button='left', clicks=2, interval=0.25)
                            # time.sleep(2)

                            # pyautogui.click(x_registado_seguinte, y_registado_seguinte, button='left', clicks=3, interval=0.5)
                            # time.sleep(3)

                            # keyboard.press_and_release('space')

                            # pyautogui.click(x_registado_cmp1, y_registado_cmp1 , button='left', clicks=1, interval=0.25)
                            # time.sleep(5)

                            # keyboard.press_and_release('r')
                            # time.sleep(0.5)

                            # keyboard.press_and_release('tab')
                            # time.sleep(0.5)

                            # keyboard.press_and_release('v')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('tab')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('2')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('tab')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('2')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('shift+tab')
                            # time.sleep(2)

                            # screenshot = pyautogui.screenshot(region=area2)
                            # texto_extraido = pytesseract.image_to_string(screenshot)
                            
                            # texto_extraido = texto_extraido.strip()  # Remove espaços no início e no fim
                            # texto_extraido = texto_extraido.replace("\n", "")  # Remove quebras de linha

                            # # Mostrar o texto extraído para depuração
                            # print("Texto extraído:\n", texto_extraido)

                            # # Comparar o texto
                            # if texto_extraido == "22000 V":
                            #     keyboard.press_and_release('tab')
                            #     time.sleep(0.3)
                            #     keyboard.press_and_release('2')
                            #     time.sleep(0.3)
                                
                            # else:
                            #     keyboard.press_and_release('tab')
                            #     time.sleep(0.3)
                                
                            # keyboard.press_and_release('tab')
                            # time.sleep(0.3)
                            # keyboard.press_and_release('s')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('tab')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('s')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('tab')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('r')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('tab')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('2')
                            # keyboard.press_and_release('0')
                            # keyboard.press_and_release('0')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('tab')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('4')
                            # keyboard.press_and_release('3')
                            # time.sleep(0.3)
        
                            # keyboard.press_and_release('tab')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('4')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('tab')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('2')
                            # keyboard.press_and_release('0')
                            # keyboard.press_and_release('0')
                            # time.sleep(1)
                            
                            # pyautogui.click(x_registado_cmp_potencia, y_registado_cmp1_potencia, button='left', clicks=1, interval=0.25)
                            # time.sleep(0.3)

                            # keyboard.press_and_release('2')
                            # keyboard.press_and_release('.')
                            # keyboard.press_and_release('2')
                            # time.sleep(0.3)
                            
                            # pyautogui.click(x_propriedade, y_propriedade, button='left', clicks=2, interval=0.25)
                            # time.sleep(0.3)
                            
                            # keyboard.press_and_release('backspace')
                            # time.sleep(0.3) 

                            # keyboard.press_and_release('1')
                            # keyboard.press_and_release('7')
                            # keyboard.press_and_release('2')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('tab')
                            # time.sleep(0.3)

                            # pyautogui.click(x_gis_x, y_gis_x, button='left', clicks=2, interval=0.25)
                            # time.sleep(0.3)
                            
                            # keyboard.press_and_release('backspace')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('2')
                            # time.sleep(0.3)

                            # pyautogui.click(x_gis_y, y_gis_y, button='left', clicks=2, interval=0.25)
                            # time.sleep(0.3)
                            
                            # keyboard.press_and_release('backspace')
                            # time.sleep(0.3)
                            
                            # keyboard.press_and_release('1')
                            # time.sleep(0.3)

                            
                            # pyautogui.click(x_estado_instalacao, y_estado_instalacao, button='left', clicks=1, interval=0.25)
                            # time.sleep(0.3) 

                            # keyboard.press_and_release('s')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('tab')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('s')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('tab')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('s')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('tab')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('s')
                            # time.sleep(0.3)
                        
                            # pyautogui.click(x_num_luz, y_num_luz , button='left', clicks=1, interval=0.25)
                            # time.sleep(0.3) 

                            # keyboard.press_and_release('8')
                            # time.sleep(1)

                            # pyautogui.click(x_quartos, y_quartos, button='left', clicks=1, interval=0.25)
                            # time.sleep(0.3) 

                            # keyboard.press_and_release('4')
                            # time.sleep(0.3)
                            

                            # pyautogui.click(x_registro, y_registro, button='left', clicks=1, interval=0.25)
                            # time.sleep(0.3) 

                            # keyboard.press_and_release('space')
                            # keyboard.press_and_release('space')
                            # keyboard.press_and_release('space')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('tab')
                            # time.sleep(0.3)

                            # keyboard.press_and_release('n')
                            # time.sleep(0.3)
                            

                            # pyautogui.click( x_registado_sim, y_registado_sim, button='left', clicks=1, interval=0.25)
                            # time.sleep(0.3) 

                            # keyboard.press_and_release('space')
                            # keyboard.press_and_release('space')
                            # keyboard.press_and_release('space')
                            # time.sleep(0.3)
                            
                            pyautogui.click(x_anterior, y_anterior, button='left', clicks=3, interval=0.25)
                            time.sleep(0.1)
                            
                            continue
                    
    

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
print(f"Numeros errados: {numeros},")
print(f"Total de numeros errados: {numeros_errados}")
import time
import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui

webbrowser.open('https://web.whatsapp.com/') 
time.sleep(30) 

workbook = openpyxl.load_workbook("teste.xlsx") # nome da planilha
pagina_clientes = workbook["cliente"]  # nome da aba  

# Vai ler os dados da planilha por linha
for linha in pagina_clientes.iter_rows(min_row=2):

    nome = linha[1].value
 

    if nome is None:
        continue

    ddd = linha[2].value
    telefone = linha[3].value
    vencimento = linha[5].value


    # msg personalizada
    mensagem = f"Olá {nome} seu boleto vence no dia {vencimento.strftime('%d/%m/%Y')}. Favor pagar no link https://www.link_do_pagamento.com"    
    numero = f"55{ddd}{telefone}" 

    
    try:
        link_msg_whatsapp = f'https://web.whatsapp.com/send?phone={numero}&text={quote(mensagem)}'
   
        # abre a conversa no whatapp web
        webbrowser.open(link_msg_whatsapp)
        time.sleep(45)
        
        # clica diretamente no botao enviar
        pyautogui.click(x=1331, y=667)
        time.sleep(20)
        
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(20)
    except Exception as e:
        print(f"Não foi possível enviar mensagem para {nome}")
        with open('erros.csv', 'a', newline='', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome}, {numero}')
        
    print("Nome:", nome)
    print("Número:", numero)
    print("Vencimento:", vencimento)
    print("-" * 30)
    
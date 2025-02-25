import pyautogui
import pyperclip
import time
import webbrowser
from datetime import datetime

def abrir_whatsapp():
    webbrowser.open("https://web.whatsapp.com/")
    while True:  
        try:
            pyautogui.locateOnScreen("Assets/chat.png")
            break
        except pyautogui.ImageNotFoundException:
            pass
        time.sleep(1)

def buscar_contato(contato):
    pyautogui.click(230, 300)  # Clique na barra de pesquisa (ajuste conforme necessário)
    pyautogui.write(contato)
    pyautogui.press("enter")

def enviar_mensagem(mensagem):
    pyperclip.copy(mensagem)  # Copia a mensagem para evitar problemas com acentos
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")

def ativar_tela(counter):
    if counter >= 180:  # 180 segundos = 3 minutos
        neutral = pyautogui.position()
        pyautogui.moveTo(100, 200)
        time.sleep(0.5)  # Pequena pausa para evitar falhas
        pyautogui.moveTo(neutral)

def agendar_envio(contato, mensagem, data_hora):
    counter = 0
    data_hora_obj = datetime.strptime(data_hora, "%Y-%m-%d %H:%M")
    
    while True:
        agora = datetime.now()
        if agora >= data_hora_obj:
            abrir_whatsapp()
            buscar_contato(contato)
            enviar_mensagem(mensagem)
            print("Mensagem enviada!")
            break
        time.sleep(10)  # Verifica a cada 10 segundos
        counter += 10  # Agora o contador será atualizado corretamente
        ativar_tela(counter)
        counter = 0
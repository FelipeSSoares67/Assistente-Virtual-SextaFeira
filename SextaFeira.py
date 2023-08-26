import speech_recognition as sr
import pyttsx3
import pyaudio
import os
import pyautogui as exe
import time
from subprocess32 import run
import pywhatkit as yt

audio = sr.Recognizer()
SextaFeira = pyttsx3.init()

def voz():
    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language="pt-br")
            comando = comando.lower()
            if 'sexta-feira' in comando:
                print(comando.replace('sexta-feira',''))
                SextaFeira.say(comando.replace('sexta-feira',''))
                SextaFeira.runAndWait()

    except:
        print('erro no microfone')

    return comando

def executar_comandos():
    comando = voz()

    if 'sexta-feira tocar' in comando:
        musica = comando.replace('sexta-feira tocar','')
        os.system("spotify")
        time.sleep(5)
        exe.hotkey('ctrl','l')

        exe.write(musica, interval = 0.5)

        for key in ['enter','pagdow','tab','tab','tab','enter']:
            time.sleep(0.5)
            exe.press(key)

    elif "sexta-feira abrir ópera" in comando:
        run("C:/Users/felip/AppData/Local/Programs/Opera GX/launcher.exe")

    elif "sexta-feira abrir app" in comando:
        item = comando.replace('sexta-feira abrir app','')
        exe.press('win')
        exe.write(item, interval=0.3)
        time.sleep(3)
        exe.press('enter')

    elif 'sexta-feira abrir site' in comando:
        item = comando.replace('sexta-feira abrir site ','')
        run("C:/Users/felip/AppData/Local/Programs/Opera GX/launcher.exe")
        time.sleep(1)
        exe.hotkey('ctrl','l')
        exe.write(f'https://www.{item}.com', interval = 0.1)
        exe.press('enter')

    elif 'sexta-feira pesquisar' in comando:
        pesquisar = comando.replace('sexta-feira pesquisar','')
        run("C:/Users/felip/AppData/Local/Programs/Opera GX/launcher.exe")
        time.sleep(1)
        exe.hotkey('ctrl','l')
        exe.write(pesquisar, interval = 0.1)
        exe.press('enter')

    elif 'sexta-feira reproduzir' in comando:
        musica = comando.replace('sexta-feira reproduzir','')
        resultado = yt.playonyt(musica)

    elif 'sexta-feira fechar' in comando:
        exe.hotkey('alt','f4')

    elif 'sexta-feira tarefa' in comando:
        tarefa = comando.replace('sexta-feira tarefa','')
        exe.press('win')
        exe.write("to do", interval=0.5)
        exe.press('enter')
        time.sleep(3)
        exe.hotkey('ctrll','n')
        exe.write(tarefa, interval=0.5)
        time.sleep(3)
        exe.press('enter')
        exe.hotkey('alt','f4')


while True:
    comando = voz()
    executar_comandos()  
    if comando is not None:
        if 'sexta-feira obrigado' in comando:
            break

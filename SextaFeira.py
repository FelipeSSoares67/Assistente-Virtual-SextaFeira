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
        app = comando.replace('sexta-feira abrir','')
        run("C:/Users/felip/AppData/Local/Programs/Opera GX/launcher.exe")

    elif 'sexta-feira abrir steam' in comando: 
        app = comando.replace('sexta-feira abrir','')
        run("C:\Program Files (x86)\Steam\steam.exe") 

    elif 'sexta-feira abrir epic games' in comando: 
        app = comando.replace('sexta-feira abrir','')
        run("C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe") 
        
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

executar_comandos()     

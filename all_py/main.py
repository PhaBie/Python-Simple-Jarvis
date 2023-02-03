import pyttsx3 
import time
import webbrowser
import shutil
import speech_recognition as sr
import datetime
import os
import winshell
import wikipedia
import sys, os, glob, traceback, platform
sys.path.append('/usr/share/inkscape/extensions')
sys.path.append(r'c:/Program Files/Inkscape/share/extensions')
sys.path.append(os.path.dirname(__file__))
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


print(Fore.GREEN + " ██████╗ ██╗  ██╗ █████╗ ██████╗ ██╗███████╗    ███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗ ")
print(Fore.GREEN + " ██╔══██╗██║  ██║██╔══██╗██╔══██╗██║██╔════╝    ██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║ ")
print(Fore.GREEN + " ██████╔╝███████║███████║██████╔╝██║█████╗      ███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║ ")
print(Fore.CYAN + " ██╔═══╝ ██╔══██║██╔══██║██╔══██╗██║██╔══╝      ╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║ ")
print(Fore.CYAN + " ██║     ██║  ██║██║  ██║██████╔╝██║███████╗    ███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║ ")
print(Fore.CYAN + " ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚══════╝    ╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝ ")       
print(Fore.GREEN + "                                                                                                      ")                                                                  

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.setProperty('rate',180)
    engine.runAndWait()

def commands():



    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")

        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-EN')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("I don't understand, Say that again please...")
        return "None"
    return query

def wishings():

    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("good Evening!")

    speak("I am Jarvis Mr.Tosakul. Please tell me how may I help you ")


if __name__ == "__main__":

    while True:
        wishings()
        query = commands().lower()
        if 'time' in query:

            strTime = datetime.datetime.now().strftime("%H:%M:%S")

            speak(f"Sir, the time is {strTime}")

        elif 'open my game' in query:

            speak("Opening your game now !!")

            os.startfile("C:\Program Files\Epic Games\DeathStranding\DeathStranding.exe")

        elif 'open browser' in query:

            speak("Opening your browser now !!")

            os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")

        elif 'open youtube' in query:
            speak("Opening Youtube Now!!")
            webbrowser.get('windows-default').open_new_tab('https://www.youtube.com/')

        elif 'open facebook' in query:
            speak("Opening facebook Now!!")
            webbrowser.get('windows-default').open_new_tab('https://www.facebook.com/')

        elif 'open instagram' in query:
            speak("Opening IG Now!!")
            webbrowser.get('windows-default').open_new_tab('https://www.instagram.com/')


        elif 'open my browser' in query:
            speak("Opening your browser Now!!")
            webbrowser.get('windows-default').open_new_tab('https://www.youtube.com/')
            webbrowser.get('windows-default').open_new_tab('https://www.facebook.com/')
            webbrowser.get('windows-default').open_new_tab('https://www.instagram.com/')



        elif 'open' in query:

            speak("System Cleaning Now")

            folders = [
                f'C:\\Windows\\Temp'
            ]


            message = ''

            print('#'*43)
            print('#',' '*39, '#')
            print('#', ' '*9, 'PhaBie Clean Mode', ' '*9, '#')
            print('#', ' '*39, '#')
            print('#' '', 'Deleting all temp file', '', '#')
            print('#', ' '*39, '#')
            print('#'*43)

            for folder in folders:
                for filename in os.listdir(folder):
                    file_path = os.path.join(folder, filename)

                    try:
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                            os.unlink(file_path)

                            print(f"Delete: {filename}")
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                    except Exception as e:
                        message = 'Failed to delete %s. Reason: %s' % (file_path, e)
            speak("Success clean all temp file")
            print(Fore.LIGHTGREEN_EX + 'Success clean all temp file')

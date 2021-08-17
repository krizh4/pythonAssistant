import speech_recognition as sr
import pyttsx3
import pywhatkit
import webbrowser
from time import ctime
import time
import requests, json

engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)

def listen():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("I'm listening")
        audio = r.listen(source)
    data = ""

    try:
        data = r.recognize_google(audio)
        print(f"You said: {data}")

    except sr.UnknownValueError:
        print("I can't understand")

    except sr.RequestError:
        print("Request failed {0}".format())
    
    return data

def respond(audioString):
    try:
        print(audioString)
        engine.say(audioString)
        engine.runAndWait()
        return listening
    except NameError:
        return

def openapp(appname):
    listening = True
    os.startfile(appname)
    return listening

def assist(data):
    #links to apps
    spotify = "App_Shortcuts\Spotify.lnk"
    chrome = "App_Shortcuts\Chrome.lnk"
    photoshop = "App_Shortcuts\Photoshop.lnk"
    word = "App_Shortcuts\Word.lnk"
    try:
        if "how are you" in data:
            listening = True
            respond("I'm well how about you")
        
        if "what time is it" in data:
            listening = True
            respond(ctime())

        if "who are you" in data:
            listening = True
            respond("Hello, I am Sarah")
        
        #apps opening
        if "open spotify" in data:
            openapp(spotify)
        
        if "open word" in data:
            openapp(word)

        if "open photoshop" in data:
            openapp(photoshop)

        if "open chrome" in data:
            openapp(chrome)

        if "stop listening" in data:
            listening = False
            respond("stoped listening")

        #special features
        if "play" in data:
            if "play spotify" in data:
                listening = True
                webbrowser.open("https://open.spotify.com/playlist/37i9dQZF1EuPcQ7TNislHh?si=fa7111596a38410b")
            else:
                listening = True
                play = data.replace('play', '')
                pywhatkit.playonyt(play)

        
        return listening
    
    except UnboundLocalError:
        listening = True
        return listening


time.sleep(2)
name = "Krishmika"
respond(f"Hi {name}, how can i help you")
listening = True
while listening == True:
    data = listen()
    listening = assist(data.lower())

#devil-prog(krizha)

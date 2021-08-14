import speech_recognition as sr
from time import ctime
import time
import playsound
import os
from gtts import gTTS, tts
import requests, json

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
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("speech.mp3")
    playsound.playsound("speech.mp3", True)

def assist(data):
    if "how are you" in data:
        listening = True
        respond("I'm well how about you")
    
    if "What time is it" in data:
        listening = True
        respond(ctime())

    if "stop listening" in data:
        listening = False
        respond("stoped listening")
        return listening

    return listening

time.sleep(2)
name = "yourName"
respond(f"Hi {name}, how can i help you")
listening = True
while listening == True:
    data = listen()
    listening = assist(data)
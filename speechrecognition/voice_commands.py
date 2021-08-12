import sys
import speech_recognition as sr
from tkinter import *

r = sr.Recognizer()

audiofile = sr.AudioFile('audio.wav')
with audiofile as source:
    audio = r.record(source)

out = r.recognize_google(audio)
print(out)
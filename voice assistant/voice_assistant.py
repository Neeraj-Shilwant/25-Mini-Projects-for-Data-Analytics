import pyttsx3
import datetime
import webbrowser
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if(hour > 0 and hour <= 12):
        speak("Good Morning Sir!")
    elif(hour > 12 and hour <= 6):
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("I am your Assistant!")
    speak("Jarvis 1 point o")
def username():
    speak("What do I call you sir?")
    uname = takeCommand()
    speak(uname)
    speak()

def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")



wishme()
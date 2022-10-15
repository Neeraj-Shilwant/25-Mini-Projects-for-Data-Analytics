import pyttsx3
import datetime
import speech_recognition as sr
import smtplib
import os 
import pyaudio
import shutil
import wikipedia
import webbrowser

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
    speak(f"welcome Mister {uname}")
    columns = shutil.get_terminal_size().columns
    print("#####################")
    print(f"Welcome Mr. {uname}")
    print("#####################")

    speak("How Can i Help you Sir")

def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
    except Exception as e:
        print(e)
        speak("Sorry Sir!, unable to recognize Can you please speak Again")
        return "None"
    return query

def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)  #smtp sever with port number 587
    server.ehlo()
    server.starttls()

    server.login('neershil67@gmail.com','neershil@6700')
    server.sendmail('neershil67@gmail.com',to,content)
    server.close()

if __name__ == '__main__':
    clear = lambda:os.system('cls')
    clear()
    wishme()
    username()
    while True:
        query = takeCommand().lower()
        #all commands will be stored in query in lowercase
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")           


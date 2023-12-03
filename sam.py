import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#pipprint(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<16:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Sam, Samanvitha's assistant, please tell me how may I help you ")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising..")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        print("Say that again. please...")
        return "None"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('samanvithabhat3@gmail.com','9379460338')
    server.sendmail('samanvithabhat3@gmail.com',to,content)
    server.close()    






if __name__=="__main__":

    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia..")
            query=query.replace("wikipeda","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is{strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\SAMANVITHA\\Desktop\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to="samanvithabhat3@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                speak("sorry Im not able to send this email")


        
        





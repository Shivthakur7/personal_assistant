import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices=  engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour) 
    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    elif hour==22:
        speak("good night")
    else:
        speak("good evening")

    speak("I am darling how may i help you")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"
    return query
        

if __name__== "__main__":
     wishMe()
     if 1:
         query = takeCommand().lower()
    


     if 'wikipedia' in query:
        speak("searching wikipedia...")
        query =query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
     

     elif'open youtube' in query:
         webbrowser.open("youtube.com")

     elif'open google' in query:
         webbrowser.open("google.com")

     elif'open stack overflow' in query:
         webbrowser.open("stackoverflow.com")

     elif 'play music' in query:
         music_dir ='D:\\music'
         songs =os.listdir(music_dir)
         print (songs)
         os.startfile(os.path.join(music_dir,songs[1]))

     elif'the time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"Sir, the time is{strTime}")


     elif'open code' in query:
         codepath ="C:\\Users\\asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
         os.startfile(codepath)
     
     elif 'microsoft' in query:
         codepath= "C:\\Program Files (x86)\\Microsoft\\Edge\\Application"
         os.startfile(codepath)
     

        
import os
import time
import pyttsx3
import datetime
import pyaudio
import wikipedia
import webbrowser
import wolframalpha
import subprocess
import speech_recognition as sr 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    pass

def wishMe():
    hour = datetime.datetime.now().hour

    if hour >= 0 and hour < 12:
        speak("Hello, Good Morning.")
        print("Hello, Good Morning.")
    elif hour >= 12 and hour < 18:
        speak("Hello, Good Afternoon.")
        print("Hello, Good Afternoon.")
    else:
        speak("Hello, Good Evening.")
        print("Hello, Good Evening.")


#function for taking command from user
def tackCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        speak("please say that again")
        print("please say that again")
        return "None"
    return query




if __name__ == "__main__":
    wishMe()
    speak("I am Katana.")
    print("I am Katana.")

    

    while True:
        speak("Tell me how can I help you Sir?")
        query = tackCommand().lower()


        #skill - 1
        if 'wikipedia' in query:
            print("Searching Wikipedia...")
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("Accoding to Wikipedia")
            print(results)
            speak(results)
            time.sleep(5)

        #skill - 2
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            time.sleep(5)
        elif 'open google' in query:
            webbrowser.open("google.com")
            time.sleep(5)
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
            time.sleep(5)
        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            time.sleep(5)
        elif 'github' in query:
            webbrowser.open("https://github.com")
            time.sleep(5)
        
        #skill - 3
        elif 'current time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"the current time is {strTime}\n")
            speak(f"the current time is {strTime}")
            time.sleep(4)


        #skill - 4
        elif 'open code' in query or 'open vs code' in query:
            vsCodePath = "C:\\Users\\arceu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"            
            os.startfile(vsCodePath)
            time.sleep(5)

        #skill - 5
        elif 'news' in query:
            news1 = webbrowser.open_new("https://timesofindia.indiatimes.com/home/headlines") 
            news2 = webbrowser.open_new("https://www.thehindu.com/latest-news/")
            speak("Here ar some latest headlines from The Times of India & The Hindu.")
            time.sleep(12)
                
         
        
        

        #skill - 6
        elif 'ask' in query:
            speak("I can answer any computational and geographical question.")
            speak("What question do you want to ask?")
            question = tackCommand()
            appID = "R7V94J-GVT6HVHGHP"
            client = wolframalpha.Client('R7V94J-GVT6HVHGHP')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
            time.sleep(10)

        #skill - 7
        elif 'covid' in query or 'corona' in query:
            worldCase = webbrowser.open_new("https://covid19.who.int/")
            indiaCase = webbrowser.open_new("https://www.mohfw.gov.in/")
            speak("Here are some latest update on COVID-19.")
            time.sleep(10)

        #skill - 8
        elif 'log off' in query or 'sign out' in query or 'shutdown' in query:
            speak("OK, Your PC will shutdown in some seconds, make sure you firstly exit from all applications.")
            subprocess.call(["shutdown", "/l"])
       

        #some personal details
        elif 'who are you' in query or 'what can you do' in query or 'tell me about yourself' in query:
            speak("I am Katana. I am your personal degital assistant.")
            speak('I am programed to do task like:'
            'predict current time, search wikipedia, opening youtube, google chrome, gmail, stackoverflow.'
            ' Get top headline news frm times of india & the hindu, get latest update of COVID-19 '
            ' and also you can ask me computational or geographical question too...')
            time.sleep(4)
        
        elif 'who made you' in query or 'who created you' in query:
            speak("I was built by Arceus-SJ7 (Shantanu)")
            time.sleep(4)

         #end of the while loop and stop the compiler & AI 
        if 'good bye' in query or 'ok bye' in query or 'stop' in query:
            speak("Your personal assistant Katana is shutting down, Good bye...")
            print("Your personal assistant Katana is shutting down, Good bye...")
            speak("have a gret day sir.")
            break 
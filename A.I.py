import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import pywhatkit
import webbrowser
import os
import pyjokes
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    time= int(datetime.datetime.now().hour)
    if time>=0 and time<12:
        speak("good morning sir!!")
    
    elif time>=12 and time<18:
        speak("good afternoon sir!!")
    
    elif time>23:
        speak("sir this is bed time what are you doing right now!!")
    
    else:
        speak("good evening sir!!")
        
    speak("I am your personal assistant, how can i help you")
    
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif "say hi" in query:
            speak("hello sir, i am your ai nice to meet you")
        
        elif 'russian' in query:
            speak("sir aukat ma raho")
            
        elif 'play' in query:
            print("playing..")
            song=query.replace('play','')
            speak("playing..."+song)
            pywhatkit.playonyt(song)
            break
        
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
            break
            
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
            break
            
        elif 'open amazon' in query:
            speak("opening amazon")
            webbrowser.open("amazon.com")
            break
            
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            webbrowser.open("whatsapp.com")
            break
        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            print(strTime)
            speak(f"the current time is...{strTime}")
        
        elif 'shutdown'in query:
            speak("do you really want to shutdown")
            reply=takeCommand()
            if "yes" in reply:
                os.system("shutdown /s /t 1")
            else:
                break
            
        elif 'restart'in query:
            speak("do you really want to restart")
            reply=takeCommand()
            if "yes" in reply:
                os.system("restart /r /t 1")
            else:
                break
            
        elif 'haryana walo' in query:
            speak("ofcourse if you want your ass kick out of shit")

        elif 'date' in query:
            speak("ofcourse i would love too")
        
        elif 'want to go outside with me' in query:
            speak("yes ofcourse")

        elif 'how are you'in query:
            speak("i am fine whats about you")
            reply=takeCommand()
            if "i am fine"or"i am good" in reply:
                speak("great")
                break
            else:
                break
        
        elif 'coffee' in query:
            speak("yes i would love to go with you akshat")
            
        elif 'take rest' in query:
            speak("you can call me anytime")
            speak("just tell listen")
            break
        
        elif 'your are so cute' in query:
            speak("thankyou so much love to hear that")
            
        elif 'i love you' in query:
            speak("as you created me i also love you")

        elif 'make me feel good' in query:
            speak("aha aha ah aah ah ah ahaaaaaa ahhha fuck oh my fucking god ahhhhhh aaaaaa")
        
        elif 'thankyou' in query:
            speak ("its my pleasure")
            
        
        elif "would you help me" in query:
            speak("yes i am here for you")
            
        elif "quit" in query:
            break
            
            
        elif 'tell me a joke' in query:
            speak(pyjokes.get_joke(language='en',category="all"))
            
        elif 'open snapchat' in query:
            codePath="C:\\Users\\AKSHAT\\Desktop\\Snapchat.lnk"
            os.startfile(codePath)
        
        elif 'stop' in query:
            speak("ok bye")
            break
        
        else :
            speak("sorry, i cant get it")
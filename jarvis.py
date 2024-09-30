import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import webbrowser
import pywhatkit as kit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Convert voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=8)
       
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        speak("Say that again, please...")
        return "none"
    return query

# Wishing function
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I'm Jarvis, sir. Tell me how can I help you?")

if __name__ == "__main__":
    wish()
    while True:
        query = takecommand().lower()

        # Logic for tasks
        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
         
        elif "open command prompt" in query:
            os.system("start cmd")
        
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('Webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "play nasheed" in query:  
            music_dir = "music"
            songs = os.listdir(music_dir)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))
        
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
        
        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open google" in query:
            speak("Sir, what should I search on Google?")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
       
        elif "send message" in query:
            kit.sendwhatmsg("+923080452287", "This is a testing protocol", 2, 25)

        elif "play song on youtube" in query:
            kit.playonyt("See You Again")
        
        elif "no thanks" in query:
            speak("Thanks for using me, sir. Have a good day!")
            exit()
        
        speak("Sir, do you have any other work?")

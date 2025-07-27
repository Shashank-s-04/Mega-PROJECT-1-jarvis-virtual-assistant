import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import musicLibrary
import requests

newsapi = "785bc13bf3d142aab2c5d18afe0d73d0"
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set voice, rate, and volume
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)


def speak(text):
        engine.say(text)
        engine.runAndWait()
        
def processCommand(c):
        if "open google" in c.lower():
                webbrowser.open("https://google.com")
        elif "open facebook" in c.lower():
                webbrowser.open("https://facebook.com")
        elif  "open linkedin" in c.lower():
                webbrowser.open("https://Linkedin.com")
        elif  "open youtube" in c.lower():
                webbrowser.open("https://Youtube.com")
        elif c.lower().startswith("play"):
                song = c. lower() . split (" ") [1]
                link = musicLibrary.music[song]
                webbrowser.open(link)
        elif "news" in c.lower():
                r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
                if r.status_code == 200:
                        # Parse the JSON response
                        data = r.json()
                        # Extract the articles
                        articles = data.get('articles', [])
                        # Print the headlines
                        for article in articles:
                                print(article['title'])
                                speak(article['title'])
        else:
                # Let OpenAi handle the request
                pass

                        
if __name__== "__main__":
        speak("initializing jarvis......")
        while True:
                # Listen for the wake word 'jarvis'
                # Obtain audio from microphone
                r = sr.Recognizer()
                print("Recognizing...")

                try:
                        with sr.Microphone() as source:
                                print("Listening.....")
                                audio = r.listen(source, timeout=4, phrase_time_limit=2)
                        word = r.recognize_google(audio)
                        
                        if (word.lower() == "jarvis"):
                                speak("Yaa")
                                # LISHEN THE COMMAND 
                                with sr.Microphone() as source:
                                    print("Jarvis Active....")
                                    audio = r.listen(source)
                                command = r.recognize_google(audio)
                                processCommand(command)      
                except Exception as e:
                        print("error: {0}".format(e))

                time.sleep(0.5)  # Loop slow karne ke liye
 
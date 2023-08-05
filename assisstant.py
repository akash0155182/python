import webbrowser#open url
import speech_recognition as sr#user command
import pyttsx3
import pickle as pickle
from googlesearch import search

engine=pyttsx3.init()
voices=engine.getProperty('voices')#tuple
engine.setProperty('voice',voices[1].id)
text=''
def userCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=0.2)
        audio=r.listen(source)
        try:
            global text
            text=r.recognize_google(audio,language='en-in')
        except:
            engine.say('could not get result speak again')
            engine.runAndWait()
            userCommand()
if __name__=='__main__':
    while True:
        engine.say("hello Aakash. how may i help you")
        engine.runAndWait()
        userCommand()
        if 'open whatsapp' in text.lower():
            webbrowser.open('https://chat.openai.com/')
        elif 'play' in text.lower():
            query=text.replace('play','')
            for j in search(query,tld='co.in',num=10,stop=10,pause=2):
                if 'youtube' in j:
                    webbrowser.open(j)
                    break
        elif 'open spotify' in text.lower():
            webbrowser.open('https://open.spotify.com/?')
        elif 'weather' in text.lower():
            url='https://search.yahoo.com/search?fr=mcafee&type=E211US885G0&p=weather'
        elif 'stop' in text.lower()or'cancel' in text.lower() :
            break      
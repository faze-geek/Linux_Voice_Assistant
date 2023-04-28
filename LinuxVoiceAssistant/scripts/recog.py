import speech_recognition as sr
from say import say
import os
def recog():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        # os.system("clear")
        print("Speak Now....")
        r.adjust_for_ambient_noise(source, duration = 1)
        audio_text = r.listen(source)
        
        try:
            print("Recognising.....")
            query =  r.recognize_google(audio_text)
        except:
            print("Say that again please.........")
            return "None"
        return query
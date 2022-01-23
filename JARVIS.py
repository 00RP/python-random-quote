import speech_recognition as sr
import pyaudio

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak..")
    r.pause_threshold
    
    

    while True:
        audio = r.listen(source)
        speech = r.recognize_google(audio, language ='en-in' )

        print(f"User said: {speech}")
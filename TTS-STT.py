import pyttsx3 # pyttsx3 is a text-to-speech conversion library in Python
import speech_recognition as s
eng= pyttsx3.init()

while True:
    answer= input("Type Something: ")
    eng.say(answer)
    eng.runAndWait()

    r=s.Recognizer()
    with s.Microphone() as source:
        audio = r.listen(source)
        print(r.recognize_google(audio))
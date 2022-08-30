import pyttsx3 # pyttsx3 is a text-to-speech conversion library in Python
eng= pyttsx3.init()

while True:
    answer= input("Type Something: ")
    eng.say(answer)
    eng.runAndWait()


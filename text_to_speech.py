import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)

def speak(text):
    print("Speaking:", text)
    engine.say(text)
    engine.runAndWait()

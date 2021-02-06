import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[4].id)
engine.setProperty("rate", 150)


engine.say("12:00PM - 1:00PM")

engine.runAndWait()
engine.stop()


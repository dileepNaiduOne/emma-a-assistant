import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[4].id)
engine.setProperty("rate", 150)

def say_out_loud(text):
    engine.say(text)
    engine.runAndWait()

to_say = input().strip().split()
for i in range(0, len(to_say), 3):
    sentence = " ".join([to_say[i], to_say[i+1], to_say[i+2]])
    engine.setProperty("rate", 120)
    say_out_loud(sentence)
    engine.setProperty("rate", 110)
    say_out_loud(to_say[i])
    say_out_loud(to_say[i+1])
    say_out_loud(to_say[i+2])
    engine.setProperty("rate", 130)
    say_out_loud(sentence)



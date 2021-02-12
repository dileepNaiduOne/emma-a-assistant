import speech_recognition as sr

def listening():
    a = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm listening, tell")
        audio = a.listen(source)
    
    try:
        print("sensing...")
        said = a.recognize_google(audio, language="en-in")
        # print(query)
    except:
        print("I didn't get what you are trying to say")
        return "No"
    return said

    
while True:
    query = listening()
    print("-----", query)
    
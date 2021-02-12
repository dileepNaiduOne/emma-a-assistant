import pandas as pd
from datetime import datetime
import pyttsx3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import webbrowser
from selenium.webdriver.chrome.options import Options
import speech_recognition as sr
from time import sleep


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[4].id)
engine.setProperty("rate", 130)


path = "C:\Program Files (x86)\chromedriver.exe"
WINDOW_SIZE = "1920,1080"

chrome_options = Options()
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

def say_out_loud(text):
    engine.say(text)
    engine.runAndWait()

def listening():
    count = 0
    while count < 3:
        a = sr.Recognizer()
        with sr.Microphone() as source:
            say_out_loud("I'm listening, tell")
            a.pause_threshold = 0.8
            audio = a.listen(source)
            
        
        try:
            say_out_loud("sensing...")
            said = a.recognize_google(audio, language="en-in")
            # print(query)
        except:
            if count == 2:
                say_out_loud("Sorry, I didn't get what you are trying to say. Bye")
                quit()
            say_out_loud("I didn't get what you are trying to say, repeat it once again")
            count += 1
            continue
        return said

def wakeup():
    while True:
        a = sr.Recognizer()
        with sr.Microphone() as source:
            a.pause_threshold = 0.5
            audio = a.listen(source)
            
    
        try:
            said = a.recognize_google(audio, language="en-in")
            if ('emma' in said.lower()) or ('hema' in said.lower()) or ('amma' in said.lower()) or ('imam' in said.lower()) or ('mr' in said.lower()):
                say_out_loud("Yes tell me, {}".format(naame))
                break
            elif ("stop" in said.lower()) or ("bye" in said.lower()) or ("quit" in said.lower()) or ("thank you" in said.lower()) or ("exit" in said.lower()):
                say_out_loud("See you soon {}. Bye".format(naame))
                quit()
        except:
            pass


#----------------------------Get todays day-------------------------------------------
# day = datetime.today().strftime("%A")
day = datetime.today().weekday()
# print(day)
#-------------------------------------------------------------------------------------

#-------------------------------Get Sudent Name by roll Number-----------------------
say_out_loud("Please enter your roll number in the console")
roll_no = input().upper()
student_data = pd.read_csv("students_details.csv")
student_data.set_index("Roll Numbers", inplace = True)
try:
    naame = list(student_data.loc[roll_no])[0].split()[0]
except:
    say_out_loud("Sorry, I don't have your data with me, do check once again what you have typed in")
    quit()
#------------------------------------------------------------------------------------

flag = 0
gap = False
while True:
#---------------------------------Intro-------------------------------------------------------
    if flag == 0:
        say_out_loud("hello {}, i'm, emma. What you what me to do? To know what all I can do, just say, what you can do?".format(naame))
    elif gap:
        say_out_loud("Is there anything else that you what me to do? If so just say, Emma, to wake me up. Till then I will take a nap, or else say, Quit, to stop me")
        wakeup()
    else:
        say_out_loud("Is there anything else that you what me to do? If so just say, or else say, Quit, to stop me")
#----------------------------------------------------------------------------------------------

#---------------------Query input--------------------------------------------------------------
    query = listening().lower()
    # print(query)
    # say_out_loud('I heard, {}'.format(query))
#----------------------------------------------------------------------------------------------

#----------------------------time table data------------------------------------------
    df = pd.read_csv('time table.csv')
    df.set_index("Day", inplace = True)
#-------------------------------------------------------------------------------------

    flag = 1
    if ("stop" in query) or ("bye" in query) or ("quit" in query) or ("thank you" in query):
        say_out_loud("See you soon {}. Bye".format(naame))
        quit()

#----------------------------what emma can do------------------------------------------
    elif (('you' in query) and ('can do' in query)) or ('your features' in query):
        say_out_loud("{} I can do lot of things!. I can say your time table. I can login into your college website and show your all semester marks. I can dictate your record, so that it becomes easy to write down. I can search anything in Google or Youtube. I can open M,L,R,I,T website. And many more... Note this {}, If you want me to saerch in Google or youtube you need to say, Google about, or, Youtube about, after that the keywords that you want me to search".format(naame, naame))
        gap = False
#-------------------------------------------------------------------------------------

    elif ("college" in query) and ("study" in query):
        say_out_loud("You are studying in M,L,R,I,T, college, which means Mallareddy Institute, no no, sorry, Marri Laxman reddy Institute of Technology")
        gap = False

#---------------------------------Say Time Table--------------------------------------
    elif (("say" in query) or ("se" in query) or ("show" in query)) and ("time table" in query):
        if 0<=day<=6:
            todayy = dict(df.iloc[day,:])
            timee = list(todayy.keys())
            classs = list(todayy.values())
            textt = '{}! your time table is, Today from {} you have {} class. After that you have {} class from {}. At last you need to attend {} class from {}'.format(naame, timee[0], classs[0], classs[1],timee[1], classs[2],timee[2])
            say_out_loud(textt)
        else:
            engine.say("I know you are Topper but, Its Holiday!!")
        gap = False
#---------------------------------------------------------------------------------------

    elif ('who are you' in query):
        say_out_loud("I am emma. A virtual assistant for Students. To know what all I can do, ask me...")
        gap = False

#------------------------------------------Info-----------------------------------------
    elif ('what is your name' in query) or ('should i call you' in query) or (('who' in query) and ('created' in query)):
        say_out_loud("Technically I am, emma. You can call me with this name. But, Dileep calls me, May, Srinivas calls me, Sunday, and, Emma, is named by Madhav and Karthik. So majority decided my name as emma. By the way these 4 people, made me.")
        gap = False
#---------------------------------------------------------------------------------------

    elif ((("not" in query) or ("don't" in query) or ("do not" in query) or (("not" in query) and ("intrested" in query))) and (("attend" in query) or ("go to class" in query))) or ("demotivated" in query):
        say_out_loud('I have found something for you, {}'.format(naame))
        webbrowser.open('https://youtu.be/OYYLe268V-Q')
        sleep(66)
        gap = False
#--------------------------------------------------show marks---------------------------------------
    elif ("show" in query) and (("marks" in query) or ("report card" in query) or ("progress card" in query)):
        driver = webdriver.Chrome(executable_path= path, chrome_options=chrome_options)
        say_out_loud("Opening exams website")
        driver.get("https://exams.mlrinstitutions.ac.in/")

        first = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.ID, "lnkLogins"))
        )
        first.click()

        first = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.ID, "lnkStudent"))
        )
        first.click()

        driver.find_element(By.ID, "txtUserId").send_keys(roll_no)
        driver.find_element(By.ID, "txtPwd").send_keys(roll_no)

        first = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.ID, "btnLogin"))
        )
        first.click()
        say_out_loud("Login done".format(naame))

        say_out_loud("Be patient {}, This may take some time. Till then hum your favourite song.".format(naame))

        first = driver.find_element(By.ID, "LinkButton2")
        webdriver.ActionChains(driver).move_to_element(first).perform()

        second = driver.find_element_by_id("lnkOverallMarks")
        second.click()
        gap = True
#----------------------------------------------------------------------------------------------------

#--------------------------------------open college website------------------------------------------
    elif (("open" in query) or ("show" in query)) and (("college website" in query) or ("mlr it" in query) or ("mlrit" in query)):
        webbrowser.open('https://mlrinstitutions.ac.in/')
        say_out_loud('opening M,L,R,I,T website...')
        gap = True
#----------------------------------------------------------------------------------------------------

#----------------------------------------search in google--------------------------------------------
    elif ("google about" in query):
        query = query.replace("google about", "").strip()

        driver = webdriver.Chrome(path)
        driver.get("https://www.google.com/")
        say_out_loud("searching on Google...")
        driver.find_element(By.NAME, "q").send_keys(query)
        driver.find_element_by_name("q").send_keys(Keys.ENTER)
        gap = True
#----------------------------------------------------------------------------------------------------

#----------------------------------------open youtube--------------------------------------------
    elif ("youtube about" in query):
        query = query.replace("youtube about", "").strip()

        driver = webdriver.Chrome(path)
        driver.get("https://www.youtube.com/")
        say_out_loud("searching on youtube...")
        driver.find_element(By.NAME, "search_query").send_keys(query)
        driver.find_element_by_name("search_query").send_keys(Keys.ENTER)
        gap = True
#----------------------------------------------------------------------------------------------------

#---------------------------------------Dictate------------------------------------------------------
    elif ("dictate" in query):
        say_out_loud("Sure, Copy and Paste the text that you want me to dictate")
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
        gap = False
#----------------------------------------------------------------------------------------------------

    else:
        say_out_loud("Sorry, I don't understand what you are asking.")
        gap = False


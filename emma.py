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
    naame = None
    say_out_loud("Sorry, I don't have your data with me, do check once again what you have typed in")
    quit()
#------------------------------------------------------------------------------------

flag = 0
while True:
#---------------------------------Intro-------------------------------------------------------
    if flag == 0:
        say_out_loud("hello {}, What you what me to do?".format(naame))
    else:
        say_out_loud("Is there anything else that you what me to do? If so just type in, or else type, Quit")
#----------------------------------------------------------------------------------------------

#---------------------Query input--------------------------------------------------------------
    query = input().lower()
#----------------------------------------------------------------------------------------------

    flag = 1
    if ("stop" in query) or ("bye" in query) or ("quit" in query):
        say_out_loud("See you soon {}. Bye".format(naame))
        break
    
#----------------------------time table data------------------------------------------
    df = pd.read_csv('time table.csv')
    df.set_index("Day", inplace = True)
#-------------------------------------------------------------------------------------

#---------------------------------Say Time Table--------------------------------------
    if ("say" in query) and ("time table" in query):
        if 0<=day<=6:
            todayy = dict(df.iloc[day,:])
            timee = list(todayy.keys())
            classs = list(todayy.values())
            textt = '{}! your time table is, Today from {} you have {} class. After that you have {} class from {}. At last you need to attend {} class from {}'.format(naame, timee[0], classs[0], classs[1],timee[1], classs[2],timee[2])
            say_out_loud(textt)
        else:
            engine.say("I know you are Topper but, Its Holiday!!")
#---------------------------------------------------------------------------------------

#------------------------------------------Info-----------------------------------------
    elif ('what is your name' in query) or ('who are you' in query) or ('should i call you' in query):
        say_out_loud("Technically I am, emma. You can call me with this name. But, Dileep calls me, May, Srinivas calls me, Sunday, and, Emma, is named by Madhav and Karthik. So majority decided my name as emma. By the way these 4 people, made me.")
#---------------------------------------------------------------------------------------

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
#----------------------------------------------------------------------------------------------------

#--------------------------------------open college website------------------------------------------
    elif ("open" in query) and ("college website" in query):
        webbrowser.open('https://mlrinstitutions.ac.in/')
        say_out_loud('opening M,L,R,I,T website...')
#----------------------------------------------------------------------------------------------------

#----------------------------------------search in google--------------------------------------------
    elif ("google about" in query):
        query = query.replace("google about", "").strip()

        driver = webdriver.Chrome(path)
        driver.get("https://www.google.com/")
        say_out_loud("searching on Google...")
        driver.find_element(By.NAME, "q").send_keys(query)
        driver.find_element_by_name("q").send_keys(Keys.ENTER)
#----------------------------------------------------------------------------------------------------

#---------------------------------------Dictate------------------------------------------------------
    elif ("dictate" in query):
        say_out_loud("Copy and Paste the text that you want me to dictate")
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
#----------------------------------------------------------------------------------------------------

    else:
        say_out_loud("Sorry, I don't understand what you are asking.")


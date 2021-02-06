import pandas as pd
from datetime import datetime
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[4].id)
engine.setProperty("rate", 130)

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
    naame = list(student_data.loc[roll_no])
except:
    naame = None
    say_out_loud("Sorry, I don't have your data with me, do check once again what you have typed in")
    quit()
#------------------------------------------------------------------------------------

#----------------------------time table data------------------------------------------
df = pd.read_csv('time table.csv')
df.set_index("Day", inplace = True)
#-------------------------------------------------------------------------------------

#---------------------------------Say Time Table--------------------------------------
if 0<=day<=6:
    todayy = dict(df.iloc[day,:])
    timee = list(todayy.keys())
    classs = list(todayy.values())
    textt = 'Hello, {}! Today from {} you have {} class. After that you have {} class from {}. At last you need to attend {} class from {}'.format(naame, timee[0], classs[0], classs[1],timee[1], classs[2],timee[2])
    say_out_loud(textt)
else:
    engine.say("I know you are Topper but, Its Holiday!!")
#---------------------------------------------------------------------------------------

engine.runAndWait()
engine.stop()
#print(df[:][day])


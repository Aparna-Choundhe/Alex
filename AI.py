# # Copyright [2024} [Aparna Choundhe]  
# Licensed under the Apache License, Version 2.0 (the "License");  
# you may not use this file except in compliance with the License.  
# You may obtain a copy of the License at:  
# http://www.apache.org/licenses/LICENSE-2.0  

import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import wolframalpha
import os
import os.path
import cv2
import subprocess
import pyjokes
import winshell
import ctypes
import random
import time
import psutil
import PyPDF2
import sys
import pyautogui
import pywhatkit
from requests import get
from keyboard import press_and_release
from keyboard import press
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from untitled import Ui_MainWindow
from ecapture import ecapture as ec

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")   

    else:
        speak("Good Evening sir!")

    speak("Let me Introduce myself . I am alex sir , The virtual desktop Assistant Developed by Miss Aparna.")
    speak("And i'm here to assist you , with a variety of tasks as best i can , 24 hours a day , seven days a week.")
    speak("please Tell me , How may i Help you sir ?")

def YouTubeSearch(term):
        result = "https://www.yotube.com/results?search_query=" + term
        webbrowser.open(result)
        speak("This is what I found for you.")
        pywhatkit.playonyt(term)
        speak("This may also Help you sir.")

def DownloadYoutube():
    from pytube import YouTube
    from pyautogui import click
    from pyautogui import hotkey
    import pyperclip
    from time import sleep
    sleep(2)
    click(x=942, y=59)
    hotkey('ctrl','c')
    value = pyperclip.paste()
    link = str(value)
    def Download(link):
        url = YouTube(link)
        video = url.streams.first()
        video.download("C:\\Users\\dell\\OneDrive\\Desktop\\New folder\\New folder\\")
    Download(link)
    speak("Done sir, I have Downloaded the video.")
    speak("You can go and check it out.")
    os.startfile("C:\\Users\\dell\\OneDrive\\Desktop\\New folder\\New folder\\")

def SpeedTest():
    import speedtest
    speed = speedtest.Speedtest()
    upload = speed.upload()
    correct_Up = int(int(upload)/8000000)
    download = speed.download()
    correct_down = int(int(download)/8000000)
    speak(f"Downloading Speed Is {correct_down} M B Per Second .")
    speak(f"Uploading Speed Is {correct_Up} M B Per Second .")
    exit()

def WolfRam(query):
    api_key = "44KY78-L9GPQAPTTY"
    requester = wolframalpha.Client(api_key)
    requested = requester.query(query)

    try:
        Answer = next(requested.results).text
        return Answer
    except:
        speak("An string value is not anserable.")
#developed by Aparna Choundhe
def Calculate(query):
    Term = str(query)
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("dividedby","/")
    Term = Term.replace("into","*")

    Final = str(Term)

    try:
        result = WolfRam(Final)
        speak(f"answer is {result}")
    except:
        speak("Invalid")

def Temperature(query):
    temp = str(query)
    temp = temp.replace("what","")
    temp = temp.replace("in","")
    temp = temp.replace("is the","")
    temp = temp.replace("temperature","")

    temp_query = str(temp)

    if 'outside' in temp_query:
        var1 = "Temperature in Nanded"
        answer = WolfRam(var1)
        speak(f"{var1} Is {answer} .")
    else:
        var2 = "Tempreature In" + temp_query
        ans = WolfRam(var2)
        speak(f"{var2} Is {ans}")

def Whatsappmsg(name,message):
    from os import startfile
    from pyautogui import click
    from keyboard import press
    from keyboard import write
    from time import sleep
    startfile("C:\\Users\\dell\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(5)
    click(x=260, y=149)
    sleep(1)
    write(name)
    sleep(2)
    click(x=312, y=274)
    sleep(2)
    click(x=843, y=991)
    sleep(2)
    write(message)
    press('enter')

def WhatsappCall(name):
    from os import startfile
    from pyautogui import click
    from keyboard import press
    from keyboard import write
    from time import sleep
    startfile("C:\\Users\\dell\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(5)
    click(x=260, y=149)
    sleep(1)
    write(name)
    sleep(2)
    click(x=312, y=274)
    sleep(2)
    click(x=843, y=991)
    sleep(2)
    click(x=1874, y=74)

def WhatsappChat(name):
    from os import startfile
    from pyautogui import click
    from keyboard import press
    from keyboard import write
    from time import sleep
    startfile("C:\\Users\\dell\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(5)
    click(x=260, y=149)
    sleep(1)
    write(name)
    sleep(2)
    click(x=312, y=274)
    sleep(2)
    click(x=843, y=991)
    sleep(2)

def ChromeAuto(command):
    from keyboard import press_and_release
    query = str(command)

    if 'new tab' in query:
        press_and_release('ctrl + t')

    elif 'close tab' in query:
        press_and_release('ctrl + w')

    elif 'new windew' in query:
        press_and_release('ctrl + n')

    elif 'open history' in query:
        press_and_release('ctrl + h')

    elif 'open bookmarks' in query:
        press_and_release('ctrl + d')

    elif 'open incognito' in query:
        press_and_release('ctrl + Shift + N')
#developed by Aparna Choundhe
def YoutubeAuto(command):
    query = str(command)

    if 'pause' in query:
        press('space bar')


    elif 'resume' in query:
        press('space bar')

    elif 'full screen' in query:
        press('f')
    
    elif 'back' in query:
        press('j')

    elif 'increse' in query:
        press_and_release('shift + >')

    elif 'decrease' in query:
        press('shift + <')

    elif 'previous' in query:
        press('shift + p')

    elif 'next' in query:
        press('shift + n')
        
def Reader():
    book = open('SRS.pdf','rb')
    pdfreader = PyPDF2.PdfReader(book)
    pages = len(pdfreader.pages)
    speak(f"Number of pages in this books are {pages}") 
    speak("From which page i have to start reading?")
    numPage = int(input("Enter the page number:"))
    page = pdfreader.pages[numPage]
    text = page.extract_text()
    speak(text)

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()

    def takeCommand(self):
            #It takes microphone input from the user and returns string output

            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 1
                audio = r.listen(source)

            try:
                print("Recognizing...")    
                self.query = r.recognize_google(audio, language='en-in')
                print(f"User said: {self.query}\n")

            except Exception as e:   
                print("Say that again please...")  
                return "None"
            self.query = self.query.lower()
            return self.query.lower()
#developed by Aparna Choundhe
    def TaskExecution(self):
        speak("Please wait, System Initializing..... ")
        wishMe()
        while True:
            self.query = self.takeCommand()

            if 'how are you' in self.query:
                speak("I am fine, Thank you")
                speak("How are you Sir")
        
            elif 'fine' in self.query or 'good' in self.query:
                speak("It's good to know that your fine")
        
            elif 'change your name' in self.query:
                speak("Okay sir !")
                speak("What would you like to call me, Sir ")
                assname = self.takeCommand()
                speak("Thanks for naming me")
        
            elif 'what is your name' in self.query:
                speak("My friends call me")
                speak(assname)
                print("My friends call me", assname)
                
            elif 'what is the date' in self.query:
                speak(f"Today is {datetime.datetime.now():%A, %B %d, %Y}")
                
            elif 'what is the time' in self.query:
                speak(f"Current Time is {datetime.datetime.now():%I %M %p}")
                
            elif 'tell me a joke' in self.query:
                speak("Okay sir !")
                speak(pyjokes.get_joke())
        
            elif 'reason for you' in self.query:
                speak("I was developed by Miss Aparna to assist the users through Voice Commands")

            elif 'how old are you' in self.query:
                speak("I am a newbie sir ! Version 0.1.1")
            
            elif 'read pdf' in self.query:
                speak("Okay sir !")
                Reader()
            
            elif 'play music' in self.query:
                speak("Okay sir !")
                music_dir = "C:\\Users\\dell\\Music\\"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))

            elif 'wikipedia' in self.query:
                speak('searching wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to wikipedia")
                speak(results)

            elif 'youtube search' in self.query:
                self.query = self.query.replace("hey","")
                YouTubeSearch(self.query)
            
            elif 'stop' in self.query:
                speak("Okay sir !")
                press('space bar')

            elif 'resume' in self.query:
                speak("Okay sir !")
                press('space bar')

            elif 'full screen' in self.query:
                speak("Okay sir !")
                press('f')
            
            elif 'back' in self.query:
                speak("Okay sir !")
                press('j')

            elif 'increase' in self.query:
                speak("Okay sir !")
                press_and_release('shift + >')

            elif 'decrease' in self.query:
                speak("Okay sir !")
                press('shift + <')

            elif 'previous' in self.query:
                speak("Okay sir !")
                press('shift + p')

            elif 'next' in self.query:
                speak("Okay sir !")
                press('shift + n')

            elif 'download' in self.query:
                speak("Okay sir !")
                DownloadYoutube()

            elif 'open google' in self.query:
                speak("Okay sir !")
                speak("Here You go to Google\n")
                webbrowser.open("google.com")

            elif 'new tab' in self.query:
                press_and_release('ctrl + t')

            elif 'close tab' in self.query:
                press_and_release('ctrl + w')

            elif 'new window' in self.query:
                speak("Here You go to new Window\n")
                press_and_release('ctrl + n')

            elif 'open history' in self.query:
                press_and_release('ctrl + h')
                speak("History is opened sir")

            elif 'open bookmarks' in self.query:
                press_and_release('ctrl + Shift + o')
            
            elif 'open incognito' in self.query:
                press_and_release('ctrl + Shift + N')
                speak("incognito mode is started sir")

            elif 'open camera' in self.query:
                speak("Launching Webcam")
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break;
                cap.release()
                cv2.destroyAllWindows()

            elif 'open notepad' in self.query:
                speak('Okay sir!')
                nPath = "C:\\Windows\\system32\\notepad"
                os.startfile(nPath)

            elif 'open command prompt' in self.query or 'open CMD' in self.query:
                speak('Okay sir!')
                os.system('start cmd')

            elif 'take screenshot' in self.query:
                speak("Sir, Please tell me the name for the screenshot file")
                name = self.takeCommand().lower()
                speak("Taking Screenshot...!")
                time.sleep(2)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("ScreenShot Saved...!")
                
            elif 'whatsapp message' in self.query:
                name = self.query.replace("whatsapp message","")
                name = name.replace("to","")
                Name = str(name)
                speak(f"what is the message for {Name}")
                MSG = self.takeCommand()
                Whatsappmsg(Name, MSG)
                speak("Message sent ! ")

            elif 'video call' in self.query:
                name = self.query.replace("video call","")
                name = name.replace("to","")
                name = name.replace("call","")
                name = name.replace("video","")
                Name = str(name)
                WhatsappCall(Name)
                
            elif 'show chat' in self.query:
                speak("with whom ?")
                name = self.takeCommand()
                WhatsappChat(name)
                
            elif 'temperature' in self.query:
                Temperature(self.query)
            
            elif 'calculate' in self.query:
                Calculate(self.query)
            
            elif 'ip address' in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"Your IP Address is {ip}")
            
            elif 'battery remaining' in self.query:
                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f"Our system have {percentage} percent battery sir!")

            elif 'empty recycle bin' in self.query:
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                speak("Recycle Bin Recycled")

            elif 'lock window' in self.query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
            elif 'restart the system' in self.query:
                subprocess.call(["shutdown", "/r"])

            elif 'shutdown system' in self.query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call(["shutdown / p /f"])

            elif 'check internet speed' in self.query:
                speak("Hold on Sir ! It will take Some time")
                SpeedTest()
                
            elif 'bye' in self.query:
                speak("Ok, Bye Sir")

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
        
    def startTask(self):
        self.ui.movie = QtGui.QMovie("../../../Pictures/content/pngtree-abstract-frames-technology-futuristic-interface-streaming-overlay-png-image_2311658.jpg")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../../Pictures/content/Iron_Template_1.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../../Pictures/content/Jarvis_Gui (2).gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../../Pictures/content/dec7zp0-b1f90b09-8dd0-4877-9be1-cf990bad3309.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../../Pictures/content/Aqua.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../../Pictures/content/Aqua.gif")
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer= QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
    
    def showTime(self):
        current_time = QTime.currentTime()
        current_Date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_Date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)
alex = Main()
alex.show()
exit(app.exec_())
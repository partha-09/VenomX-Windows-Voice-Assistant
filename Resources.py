from difflib import get_close_matches
from email.message import EmailMessage
from importstmt import *
import wikipedia
from pynput.keyboard import Key, Controller
import platform
import datetime
import json
import smtplib
import string
import instaloader
import psutil
import os
import random
import time
import webbrowser
import pyautogui
import pyttsx3
import requests
import speech_recognition
import os
from pipes import quote
import sqlite3
import subprocess
import time
import webbrowser
# from playsound import playsound
import pyautogui
import pywhatkit as kit
from time import sleep
from hugchat import hugchat
import clipboard

import time
import random
import datetime
from importstmt import *
import webbrowser
import os
import pyttsx3
import requests
import shutil
# from tkinter import *
import keyboard
import pywhatkit as kit
import cv2
import subprocess
import psutil
import requests
import json
import pyttsx3
import sqlite3
con = sqlite3.connect("venomX.db")
cursor = con.cursor()

keyboard = Controller()








engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)
data = json.load(open('data.json'))
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()

    except speech_recognition.UnknownValueError:
        print("Sorry, I didn't catch that. Please speak again.")
        return "None"
    except speech_recognition.RequestError:
        print("Sorry, the speech service is down. Please speak agin")
        return "None"


import csv
import sqlite3

from Resources import *
# from features import speak

con = sqlite3.connect("venomX.db")
cursor = con.cursor()



def latestnews():
    api_dict = {"business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=3500693d4ade4a2d9ac7ba039b64db76",
                "entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=3500693d4ade4a2d9ac7ba039b64db76",
                "health": "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=3500693d4ade4a2d9ac7ba039b64db76",
                "science": "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=3500693d4ade4a2d9ac7ba039b64db76",
                "sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=3500693d4ade4a2d9ac7ba039b64db76",
                "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=3500693d4ade4a2d9ac7ba039b64db76"
                }

    content = None
    url = None
    speak(
        "Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    field = takeCommand().lower()
    for key, value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            speak("url was found")
            break
        else:
            url = True
    if url is True:
        speak("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")
        speak("Say yes to continue and no to stop")
        a = takeCommand().lower()
        if str(a) == "yes":
            pass
        elif str(a) == "no":
            break

    speak("thats all")


def mute_volume():
    """Simulate pressing the 'mute' key."""
    pyautogui.press('volumemute')
    print("Volume muted/unmuted.")    
def volume_up():
    """Simulate pressing the 'volume up' key."""
    pyautogui.press('volumeup')
    print("Volume increased.")

def volume_down():
    """Simulate pressing the 'volume down' key."""
    pyautogui.press('volumedown')
    print("Volume decreased.")    
def greetMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sir !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sir !")

	else:
		speak("Good Evening Sir !")

	speak("How can i Help you, Sir. Please give your queries")
	

def Instagram_Pro(self):
    speak("sir please enter the user name of Instagram: ")
    name = input("Enter username here: ")
    webbrowser.open(f"www.instagram.com/{name}")
    time.sleep(5)
    speak(
        "Boss would you like to download the profile picture of this account.")
    cond = self.take_Command()
    if ('download' in cond):
        mod = instaloader.Instaloader()
        mod.download_profile(name, profile_pic_only=True)
        speak(
            "I am done boss, profile picture is saved in your main folder. ")
    else:
        pass
def flip():
    speak("flipping coin")
    coin = ['heads', 'tails']
    toss = []
    toss.extend(coin)
    random.shuffle(toss)
    toss = ("".join(toss[0]))
    speak("i flipped the coin and you got .  "+toss)


def cpu():
    usage = str(psutil.cpu_percent())
    speak("cpu is at"+usage)
    battry = psutil.sensors_battery()
    speak("battery is at")
    speak(battry)


def text2speech():
    text = clipboard.paste()
    speak(text)
def take_photo():
    pyautogui.press("win")
    pyautogui.sleep(1)
    pyautogui.typewrite("camera")
    pyautogui.sleep(1)
    pyautogui.press("enter")
    pyautogui.sleep(5)
    speak("SMILE")
    pyautogui.sleep(2)
    pyautogui.click(x=960, y=870)
    pyautogui.sleep(2)
    pyautogui.hotkey("alt", "f4")
    speak("Photo taken.")

def random_alphaNumeric(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def take_screenshot():
   
    timestamp = random_alphaNumeric()
    screenshot_name = f"screenshot_{timestamp}.png"

    screenshot = ImageGrab.grab()


    screenshot_path = os.path.join(
        os.path.expanduser("~"), "Desktop", screenshot_name)
    screenshot.save(screenshot_path)
    print(f"Screenshot saved as {screenshot_name}")


    ctypes.windll.shell32.ShellExecuteW(None, "open", screenshot_path, None, None, 1)
def game_play():
    speak("Let's play Rock Paper Scissors!")
    print("LET'S PLAYYYYYYYYYYYYYY")
    
    i = 0
    Me_score = 0
    User_score = 0
    
    while i < 5:
        choose = ("rock", "paper", "scissors")  
        user_choice = random.choice(choose)  
        query = takeCommand()
        
        if query == "rock":
            if user_choice == "rock":
                speak("Rock")
                print(f"Score: ME: {Me_score} - USER: {User_score}")
            elif user_choice == "paper":
                speak("Paper")
                User_score += 1
                print(f"Score: ME: {Me_score} - USER: {User_score}")
            else:  
                speak("Scissors")
                Me_score += 1
                print(f"Score: ME: {Me_score} - USER: {User_score}")

        elif query == "paper":
            if user_choice == "rock":
                speak("Rock")
                Me_score += 1
                print(f"Score: ME: {Me_score} - USER: {User_score}")
            elif user_choice == "paper":
                speak("Paper")
                print(f"Score: ME: {Me_score} - USER: {User_score}")
            else:  
                speak("Scissors")
                User_score += 1
                print(f"Score: ME: {Me_score} - USER: {User_score}")

        elif query == "scissors" or query == "scissor":
            if user_choice == "rock":
                speak("Rock")
                User_score += 1
                print(f"Score: ME: {Me_score} - USER: {User_score}")
            elif user_choice == "paper":
                speak("Paper")
                Me_score += 1
                print(f"Score: ME: {Me_score} - USER: {User_score}")
            else:  
                speak("Scissors")
                print(f"Score: ME: {Me_score} - USER: {User_score}")

        else:
            speak("Invalid choice. Please choose rock, paper, or scissors.")
        
        i += 1
    
    print(f"FINAL SCORE: ME: {Me_score} - USER: {User_score}")
    speak(f"Final score: ME: {Me_score} - USER: {User_score}")


def schedule_day():
    tasks = [] 

  
    speak("Do you want to clear old tasks? Please say YES or NO.")
    query = takeCommand().lower()

    if "yes" in query:
        # Clear old tasks
        with open("tasks.txt", "w") as file:
            file.write("") 

  
    speak("Enter the number of tasks:")
    no_str = takeCommand().lower()
    no_tasks = int(no_str)  

  
    for i in range(no_tasks):
        speak("Tell me the task:")
        task = takeCommand().lower()
        tasks.append(task)
       
        with open("tasks.txt", "a") as file:
            file.write(f"{i + 1}. {task}\n")

    speak("Tasks have been scheduled.")
def fetch_ipl_score():
    url = "https://www.cricbuzz.com/"
    
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        
       
        team_elements = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")
        score_elements = soup.find_all(class_="cb-ovr-flo")

        if len(team_elements) >= 2 and len(score_elements) >= 12:
            team1 = team_elements[0].get_text()
            team2 = team_elements[1].get_text()
            team1_score = score_elements[8].get_text()
            team2_score = score_elements[10].get_text()

         
            speak(f"{team1}: {team1_score}")
            speak(f"{team2}: {team2_score}")
        else:
            speak("Could not find IPL scores.")
    
    except Exception as e:
        speak("An error occurred: ")   
def show_schedule():
    if os.path.exists("tasks.txt") and os.path.getsize("tasks.txt") > 0:
        with open("tasks.txt", "r") as file:
            content = file.read()
        speak("Here is your schedule.")
        speak(content) 
    else:
        speak("No tasks have been scheduled or the tasks file does not exist.")    
def close_tab():
    pyautogui.hotkey("ctrl", "w")
    speak("Tab closed.")


def show_controls():
    pyautogui.press("c")
    speak("Controls shown.")


def hide_controls():
    pyautogui.press("h")
    speak("Controls hidden.")


def go_forward_10_seconds():
    pyautogui.press("right", presses=10)
    speak("Forwarded 10 seconds.")


def go_backward_10_seconds():
    pyautogui.press("left", presses=10)
    speak("Backwarded 10 seconds.")
def scroll_to_top():
    pyautogui.press('home')


def scroll_to_bottom():
    pyautogui.press('end')


def maximize_window():
    pyautogui.hotkey('win', 'up')


def minimize_window():
    pyautogui.hotkey('win', 'down')


def fullscreen_mode():
    pyautogui.hotkey('F11')
def ring_alarm(alarm_time):
    if alarm_time is None:
        speak("No valid alarm time set.")
        return

    speak("Alarm time set to:"+alarm_time)

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        print(current_time)
        if current_time == alarm_time:
            speak("Alarm ringing, sir")
            os.startfile("music.mp3")  
            break
        time.sleep(30)

def get_time_from_user():
    speak("Please provide the hour for the alarm.")
    speak("say hour (0-23): ")
    hour=takeCommand().lower()
    # hour=14
    speak("Please provide the minute for the alarm.")
    speak("Enter minute (0-59): ")
    minute = takeCommand().lower()
    # minute=1
    # Validate and format time input
    try:
        hour = int(hour)
        minute = int(minute)
        if not (0 <= hour <= 23 and 0 <= minute <= 59):
             speak("Invalid hour or minute")
             return None
        return f"{hour:02}:{minute:02}"
    except ValueError as e:
        speak(f"Error: . Please say valid hour and minute.")
        return None
def alarm():
    alarm_time = get_time_from_user()
    ring_alarm(alarm_time)
    
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(" and today's date is")
    speak(day)
    speak(month)
    speak(year)
    speak("Please tell me, How can I help you ?")
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")

    speak("current time is "+Time)
def temp():
    api_key = "40ccaf76d39ce0e2bd20726a0188f41b" 
    speak("Say your city, sir")
    
    city = takeCommand().lower()

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        weather_desc = data["weather"][0]["description"]
        temp_celsius = data["main"]["temp"]

        speak(f"Current temperature in {city} is {temp_celsius} degree Celsius with {weather_desc}.")
        print(f"Current temperature in {city} is {temp_celsius} degree Celsius with {weather_desc}.")
    else:
        speak("Sorry, I couldn't retrieve the weather information for that location.")
        print("Sorry, I couldn't retrieve the weather information for that location.")
 
def wiki(query):
    try:
        speak("Searching from Wikipedia, sir...")
        query = query.replace("accroding to wikipedia who", "").strip()
        query = query.replace("search wikipedia", "").strip()
        query = query.replace("let me know about", "").strip()
        query = query.replace("in", "").strip()
        query = query.replace("according", "").strip()
        print(f"Query after processing: {query}")
        
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia, sir...")
        print(results)
        speak(results)
    except wikipedia.DisambiguationError as e:
        speak("There are multiple results for this query. Please be more specific, sir.")
        print(f"Disambiguation error: {e.options}")
    except wikipedia.PageError:
        speak("Sorry, sir. I couldn't find any results for that query.")
        print("Page error: No results found.")
    except Exception as e:
        speak("Sorry, sir. Something went wrong while searching Wikipedia.")
        print(f"Exception: {e}")

def searchYoutube():
        speak("what you want to search")
        print("what you want to search")
        query=takeCommand().lower()
        pywhatkit.playonyt(query)
        speak("Done, sir")
def searchGoogle(query):
        import wikipedia as googleScrap
       
        query = query.replace("let me know", "")
        query = query.replace("search in google about", "")
        query = query.replace("find in google about", "")
        query = query.replace("what do you mean by", "")
        query = query.replace("google", "")
    

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query, 1)
            speak(result)

        except:
            speak("No speakable output available")

def update():
    speak("here we go let's start the window upgradation ")
    pyautogui.press("win")
    pyautogui.sleep(0.5)
    pyautogui.typewrite("cmd")
    pyautogui.sleep(0.5)
    pyautogui.press("enter")
    pyautogui.sleep(0.5)
    pyautogui.typewrite("winget update --all")
    pyautogui.sleep(1)
    pyautogui.press('enter')
    speak("Window upgradations started ")
    pyautogui.sleep(1)
    pyautogui.hotkey('win', 'down')
def good_night_setup():
    speak("Good night, sir. Setting up the deep sleep music for your sleep.")

    choices = ['8 hour relaxing music', 'sleepy music 8 hour', 'deep sleep 8 hour',
               'medicine music 8 hour', 'raining deep sleep 8 hour']

    random_choice = random.choice(choices)


    kit.playonyt(random_choice.split())

    speak("Sweet dreams, sir.")






   





def sendmail(reciver, subject, cont):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("", "S")
    email = EmailMessage()
    email['From'] = ""
    email['To'] = reciver
    email['Subject'] = subject
    email.set_content(cont)
    server.send_message(email)
    server.close()
def songOnYoutube():
    speak("which song")
    song_name = takeCommand().lower()

    kit.playonyt(song_name)

def map():
    print("Say your city")
    speak("say you city")
    location = takeCommand().lower()
    
    pyautogui.sleep(0.5)
    webbrowser.open(
    "https://www.google.com/maps/@16.3524328,79.8664982,16196013m/data=!3m1!1e3")
    pyautogui.sleep(8)
    pyautogui.write(location)
    speak("searching.")
    pyautogui.sleep(3)
    pyautogui.press("enter")
    speak(f"here is the {location} in earth")
def is_online(url="http://www.google.com", timeout=5):
    try:
      
        response = requests.get(url, timeout=timeout)
       
        return response.status_code >= 200 and response.status_code < 300
    except requests.ConnectionError:
        return False    
def internet_status():
    if is_online():
        x = "YES SIR ! I AM READY AND ONLINE"
        speak(x)
    else:
        x = "HEY THERE SIR ! , SORRY i am  CURRENTLY NOT ONLINE"
        print(x)
def translate(word):
    word = word.lower()
    if word in data:
        speak(data[word])
    elif len(get_close_matches(word, data.keys())) > 0:
        x = get_close_matches(word, data.keys())[0]
        speak('Did you mean ' + x +
              ' instead,  respond with Yes or No.')
        ans = takeCommand().lower()
        if 'yes' in ans:
            speak(data[x])
        elif 'no' in ans:
            speak("Word doesn't exist. Please make sure you spelled it correctly.")
        else:
            speak("We didn't understand your entry.")

    else:
        speak("Word doesn't exist. Please double check it.")

def set_brightness(level):
    """Set screen brightness to a specific level (0-100)."""
    level = max(0, min(100, level))  
    cmd = f"(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,{level})"
    subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    print(f"Brightness set to {level}%.")


def notepad():
                     
                  
                    pyautogui.hotkey('win', 'r')
                    pyautogui.sleep(0.5)
                   
                    pyautogui.write('notepad')
                    pyautogui.press('enter')  
                    pyautogui.sleep(1)  
                    speak("what you want to write")
                    text = takeCommand().lower()
                    if "close" in text:
                        pyautogui.hotkey("alt", "f4")
                    pyautogui.write(text)
                    pyautogui.sleep(1) 
                    while True:
                        speak("you want to write more say yes or no")
                        op = takeCommand().lower()
                        if "yes" in op :
                            speak("what you want to write")
                            text = takeCommand().lower()
                            
                            pyautogui.write(" "+text)
                            pyautogui.sleep(1)
                        elif "no" in op and op!="none":
                            break
                    
                    speak("what is the file name")
                    file_name = takeCommand().lower()
                    pyautogui.hotkey('ctrl', 's')  
                    pyautogui.sleep(1)  
                    pyautogui.write(file_name)  
                    pyautogui.press('enter')
                   
def decrease_brightness():
    """Decrease brightness by 10%."""
    current_level = get_current_brightness()
    new_level = max(current_level - 10, 0)
    set_brightness(new_level)
    print(f"Decreased brightness to {new_level}%.")

def get_current_brightness():
    """Retrieve current brightness level."""
    cmd = "(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightness).CurrentBrightness"
    result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True)
    try:
        return int(result.stdout.strip())
    except ValueError:
        print("Failed to get current brightness.")
        return 0


def playingMusic():
     speak("if you want to play local music say yes or no")
     op = takeCommand().lower()
    #  op="no"
     if "yes" in op:
        speak("Here you go with music")
        music_dir = "C:\\Users\\Siddappa Godi\\Music\\ENGLISH"
        songs = os.listdir(music_dir)
        print(songs)
        print("")
        random = os.startfile(os.path.join(music_dir, songs[2]))
     else:
         songOnYoutube();
        # speak("Sure. What genre of music would you like to listen to?")
        # genre = takeCommand()
        # # genre="love"
        # speak(f"Playing {genre} music on YouTube.")
        # webbrowser.open(
        # f"https://www.youtube.com/results?search_query={genre}+music")
    


def get_weather_forecast():
    api_key = "40ccaf76d39ce0e2bd20726a0188f41b"  # Replace with your actual API key
    speak("What location would you like to check the weather for?")
    
    # Here, replace the fixed location with user input if you have a function like takeCommand()
    location = takeCommand().lower()
    # location = "belagavi"  # Example location for demonstration

    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        weather_desc = data["weather"][0]["description"]
        temp_celsius = data["main"]["temp"]
        current_pressure = data["main"]["pressure"]
        current_humidity = data["main"]["humidity"]


        speak(f"Sir, the weather in {location} is as follows:")
        speak(f"Temperature: {temp_celsius} degree Celsius")
        speak(f"Weather: {weather_desc}")
        speak(f"Atmospheric pressure: {current_pressure} hPa")
        speak(f"Humidity: {current_humidity}%")

        print(f"Temperature: {temp_celsius} degree Celsius")
        print(f"Weather: {weather_desc}")
        print(f"Atmospheric pressure: {current_pressure} hPa")
        print(f"Humidity: {current_humidity}%")
    else:
        speak("Sorry, I couldn't retrieve the weather information for that location.")
        print("Sorry, I couldn't retrieve the weather information for that location.")
def find_images():
    speak("What would you like to search images of?")
    query = takeCommand().lower()
    speak(f"Searching for images of {query}.")
    webbrowser.open(f"https://www.google.com/search?tbm=isch&q={query}")


from Resources import *
from importstmt import *
def chatBot(query):
    query = query+"provide answer in five lines only"
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response = chatbot.chat(user_input)
    # print(response)
    from Resources import speak
    speak(response)
    return response
def location():
    speak("Wait sir, let me check.")
    try:
        IP_Address = requests.get('https://api.ipify.org').text
        print(IP_Address)
        url = f'https://get.geojs.io/v1/ip/geo/{IP_Address}.json'
        print(url)
        geo_request = requests.get(url)
        geo_data = geo_request.json()
        
        city = geo_data.get('city', 'an unknown city')
        state = geo_data.get('region', 'an unknown region')
        country = geo_data.get('country', 'an unknown country')
        tZ = geo_data.get('timezone', 'an unknown timezone')
        longitude = geo_data.get('longitude', 'an unknown longitude')
        latitude = geo_data.get('latitude', 'an unknown latitude')
        org = geo_data.get('organization_name', 'an unknown organization')

        print(f"{city} {state} {country} {tZ} {longitude} {latitude} {org}")

        # Prepare detailed and specific responses
        if city == 'an unknown city' or state == 'an unknown region' or country == 'an unknown country':
            speak("Sir, I couldn't determine our exact location, but I have some details.")
        else:
            speak(f"Sir, I believe we are in {city}, {state}, {country}.")
        
        speak(f"We are in the {tZ} timezone. The latitude of our location is {latitude}, and the longitude is {longitude}.")
        speak(f"We are using the network of {org}.")
    except requests.RequestException as e:
        speak("Sorry sir, due to a network issue, I am not able to find where we are.")
        print(f"Network Error: {e}")
    except Exception as e:
        speak("Sorry sir, an unexpected error occurred.")
        print(f"Unexpected Error: {e}")



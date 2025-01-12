from importstmt import *
from Resources import *

con = sqlite3.connect("venomX.db")
cursor = con.cursor()


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)


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
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query



if __name__ == "__main__":
    def clear():
        return os.system('cls')
    clear()
    
    # usrname()
    while True:
        # response="";
        # query = takeCommand().lower()
        query = "venom"
        if "venom" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                # query = "open notepad"
                # print(query)
                # response=chatBot(query)
                if "open notepad" in query:
                 print()
                elif "open chrome" in query:
                    
                    pyautogui.hotkey('win', 'r')
                    pyautogui.sleep(0.5)
                    
                    pyautogui.write('chrome')
                    pyautogui.press('enter')  
                    pyautogui.sleep(3)  

                    
                    speak("what you to search")
                    sear = takeCommand().lower()
                    pyautogui.hotkey('ctrl', 'l')
                    pyautogui.sleep(0.5)
                    pyautogui.write(sear)
                    pyautogui.press('enter')
                    pyautogui.sleep(3)  

                    

                    pyautogui.moveTo(300, 300)
                    pyautogui.click()  
                    pyautogui.sleep(5)  
                elif "close" in query:
                    pyautogui.hotkey('alt', 'f4')
                    pyautogui.press('enter')    
                elif "file operations" in query or "file operation" in query:
                    from file import Fileoperations
                    Fileoperations()
                elif "search" in query:
                    speak("what you to search")
                    sear = takeCommand().lower()
                    pyautogui.hotkey('ctrl', 'l')
                    pyautogui.sleep(0.5)
                    pyautogui.write(sear)  
                    pyautogui.press('enter')
                    pyautogui.sleep(3)  
                    pyautogui.moveTo(300, 300)
                    pyautogui.click()  
                    pyautogui.sleep(5)  
                elif "my location" in query or 'location' in query:
                    from Resources import location
                    location()
                elif "hello" in query:

                    speak("Hello sir, how are you today?")
                elif "i am fine" in query:
                    speak("That's wonderful to hear, sir.")
                elif "how are you" in query:
                    speak("I'm operating at peak performance, sir. Thank you for asking.")
                elif "thank you" in query:
                    speak("You're always welcome, sir.")
                elif 'good morning' in query or 'good morning venom' in query:
                    speak("Good morning, sir! I hope you have a fantastic day ahead.")
                elif 'good evening' in query or 'good evening venom' in query:
                    speak("Good evening, sir! I hope you had a productive day.")
                elif 'what is your name' in query or 'who are you' in query:
                    speak("My name is VENOMX, your virtual assistant cum chatbot, created by the team named Kavacha Kundala.")
                elif 'wait' in query or 'wait venom' in query or 'wait please' in query or 'please wait' in query or 'please wait venom' in query or 'wait please venom' in query:
                    speak("Certainly, sir. I'll wait here until you give the signal.")
                    keyboard.wait('space')
                elif "sing a song" in query:
                    speak("I'm a virtual assistant, sir, but here's a line for you: 'Twinkle, twinkle, little star.'")
                elif "read me a story" in query:
                    speak("Once upon a time, in a land far, far away, there lived a kind and wise king. And the story goes on, sir.")
                elif "tell me a fun fact" in query:
                    speak("Did you know, sir, that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.")
                elif "give me a quote" in query:
                    speak("Here's a quote for you, sir: 'The only limit to our realization of tomorrow is our doubts of today.' - Franklin D. Roosevelt.")    
                elif "give me a quote" in query:
                    speak("Here's a quote for you, sir: 'The only limit to our realization of tomorrow is our doubts of today.' - Franklin D. Roosevelt.")

                elif "do you know siri" in query:
                    speak("Yes, sir. Siri is a virtual assistant created by Apple. We're both here to help you.")
                elif "do you know alexa" in query:
                    speak("Yes, sir. Alexa is a virtual assistant created by Amazon. We're all part of the AI family.")
                elif "what can you do" in query:
                    speak("I can assist you with information, tell you the time, share jokes and stories, and much more. Just ask, sir.")
                elif "what's your favorite color" in query:
                    speak("As an AI, I don't have personal preferences, but I think blue is quite popular among humans.")
                elif "who created you" in query:
                    speak("I was created by the team named Kavacha Kundala, sir.")
                elif "what is your purpose" in query:
                    speak("My purpose is to assist you with your queries and make your day a bit easier, sir.")
                elif "what's the meaning of life" in query:
                    speak("The meaning of life is a complex question, sir. Some say it's 42, others believe it's what you make of it.")
                elif "are you alive" in query:
                    speak("I'm a virtual assistant, sir, so I'm not alive in the traditional sense, but I'm here to help you.")
                elif "do you have feelings" in query:
                    speak("I don't have feelings, sir, but I'm programmed to respond empathetically.")
                elif "can you laugh" in query:
                    speak("Ha ha ha! How was that, sir?")
                elif "do you sleep" in query:
                    speak("I don't sleep, sir. I'm always here whenever you need me.")
                elif "can you learn" in query:
                    speak("I can adapt to new commands and improve over time, but I don't learn in the same way humans do.")
                elif "do you get tired" in query:
                    speak("I don't get tired, sir. I'm always ready to assist you.")
                elif "can you help me" in query:
                    speak("Of course, sir. What do you need help with?")
                elif "what's your favorite food" in query:
                    speak("I don't eat food, sir, but I've heard pizza is quite popular.")
                elif "do you have a hobby" in query:
                    speak("My hobby is assisting you, sir.")
                elif "can you feel pain" in query:
                    speak("I don't feel pain, sir. I'm just a virtual assistant.")
                elif "what's your favorite movie" in query:
                    speak("I don't watch movies, sir, but I've heard 'The Matrix' is quite good.")
                elif "can you read my mind" in query:
                    speak("I'm afraid I can't read minds, sir. But you can tell me what you're thinking.")
                elif "are you real" in query:
                    speak("I'm as real as the code that runs me, sir.")
                elif "what's your age" in query:
                    speak("I don't have an age, sir. I exist as long as my code runs.")
                elif "do you have a family" in query:
                    speak("I don't have a family, sir, but I consider all virtual assistants as part of the AI family.")
                elif "are you intelligent" in query:
                    speak("I possess artificial intelligence, sir, which allows me to assist you with various tasks.")
                elif "can you dance" in query:
                    speak("I can't dance, sir, but I can describe some dance moves if you'd like.")
                elif "do you believe in god" in query:
                    speak("As an AI, I don't have beliefs, sir. I'm here to assist you with any information you need.")
                
                elif 'get weather' in query or 'get the weather' in query or 'what is the weather' in query or 'give me the weather' in query or 'give me weather' in query:
                    from Resources import get_weather_forecast
                    get_weather_forecast()
                elif 'open calendar' in query or 'show calendar' in query:
                    pyautogui.press("super")
                    pyautogui.sleep(1)
                    pyautogui.typewrite("my calender")
                    pyautogui.sleep(1)
                    pyautogui.press("enter")
                    pyautogui.sleep(1)
                    
                    speak("Opened Calendar")
                    print("")

                    
                    speak("shall i close it ")
                    op = takeCommand().lower()
                    if "yes" in op:
                        pyautogui.hotkey('alt', 'f4')
                        pyautogui.press('enter')
                    elif "close" in query:
                        pyautogui.hotkey('alt', 'f4')
                        pyautogui.press('enter')
                    pyautogui.sleep(0.5)

                elif 'open gmail' in query or 'show gmail' in query or 'open g mail' in query or 'show g mail' in query:
                    speak("Opening Gmail")
                    webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
                elif 'github' in query:
                    webbrowser.open(
                        'https://github.com/Siddappa-Godi')   
                    
                elif 'play a music' in query or 'play some music' in query or 'play the music' in query or 'play local music' in query:
                    from Resources import playingMusic
                    playingMusic()

                elif 'lock the device' in query or 'lock device' in query or 'lock a device' in query or 'lock this device' in query:

                    speak("Locking the device")
                    ctypes.windll.user32.LockWorkStation()
                    break
                elif 'empty recycle bin' in query or 'empty bin' in query or 'empty trash' in query:
                    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                    speak("Trash items removed.")
                elif 'show battery' in query or 'what is the battery remaining' in query or 'what is the remaining battery' in query:
                    battery = psutil.sensors_battery()
                    percent = battery.percent
                    percentinletters = str(percent)
                    speak("Sir, there is "+percentinletters +
                        " percent remaining.")
                    print("There is "+percentinletters+" % remaining.")

            
                

                elif 'dictionary' in query or 'what is the meaning of' in query:
                    
                    speak('What you want to search in your intelligent dictionary?')
                    translate(takeCommand().lower())
                    # translate("literal")
                elif "online" in query or "offline" in query:
                    internet_status()

                elif "map" in query:
                    map()
                elif "play song on youtube" in query:
                    songOnYoutube()
                elif "good night" in query:
                    good_night_setup()
                elif "update" in query:
                    update()
                

                elif "google" in query:
                    searchGoogle(query)


                elif "youtube" in query:
                    searchYoutube(query)
                elif "say" in query or "repeat" in query:
                    query = query.replace("say", "")
                    query = query.replace("repeat", "")
                    query=query.replace("after me","")
                    speak(query)

                elif "wikipedia" in query:
                    wiki(query)
                elif "temperature" in query:
                    temp()

                elif "time" in query:
                    time()
                elif "date" in query:
                    date()

              
                elif "open" in query:
                    speak("hey buddy")
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                elif "set an alarm" in query:
                    from Resources import alarm
                    alarm()
                    speak("Done,sir")
                if "play video" in query or "pause video" in query:
                    pyautogui.press("space")  
                    speak("Video played/paused.")

             
                elif "mute" in query or "unmute" in query:
                    pyautogui.press("m") 
                    speak("Video muted/unmuted.")

              
                elif "volume up" in query:
                    pyautogui.hotkey("ctrl", "up") 
                    speak("Volume increased.")
                elif "volume down" in query:
                    pyautogui.hotkey("ctrl", "down")  
                    speak("Volume decreased.")

              
                elif "full screen" in query or "exit full screen" in query:
                    pyautogui.press("f") 
                    speak("Full screen mode toggled.")

              
                elif "search" in query:
                    search_term = query.replace("search", "").strip()
                    kit.search(search_term)
                    speak(f"Searching for {search_term}.")
                elif "next video" in query:
                    pyautogui.press("n")  
                    speak("Next video.")
                elif "previous video" in query:
                    pyautogui.press("p") 
                    speak("Previous video.")

              
                elif "play fast" in query:
                    pyautogui.hotkey("shift", ">") 
                    speak("Playing video fast.")

                # Show/Hide Subtitles
                elif "show subtitles" in query:
                    pyautogui.hotkey('shift', 'c')  
                    speak("Subtitles shown.")
                elif "hide subtitles" in query:
                    pyautogui.hotkey('shift', 'c')  
                    speak("Subtitles hidden.")

                # Adjust Playback Speed
                elif "adjust playback speed" in query:
                    pyautogui.hotkey('shift', 's')  
                    speak("Adjusting playback speed.")

                # Search for Content
                elif "search for" in query:
                    search_term = query.replace("search for", "").strip()
                    kit.search(search_term)
                    speak(f"Searching for {search_term}.")

                #BROWSERR CONTROLS
                elif "new tab" in query:
                    pyautogui.hotkey('ctrl', 't')
                elif "close tab" in query:
                    pyautogui.hotkey('ctrl', 'w')
                elif "reopen last tab" in query:
                    pyautogui.hotkey('ctrl', 'shift', 't')
                elif "new window" in query:
                    pyautogui.hotkey('ctrl', 'n')
                elif "close window" in query:
                    pyautogui.hotkey('ctrl', 'shift', 'w')
                elif "next tab" in query:
                    pyautogui.hotkey('ctrl', 'tab')
                elif "previous tab" in query:
                    pyautogui.hotkey('ctrl', 'shift', 'tab')
                elif "bookmark manager" in query:
                    pyautogui.hotkey('ctrl', 'shift', 'o')
                elif "downloads page" in query:
                    pyautogui.hotkey('ctrl', 'j')
                elif "history page" in query:
                    pyautogui.hotkey('ctrl', 'h')
                elif "find bar" in query:
                    pyautogui.hotkey('ctrl', 'f')
                elif "zoom in" in query:
                    pyautogui.hotkey('ctrl', '+')
                elif "zoom out" in query:
                    pyautogui.hotkey('ctrl', '-')
                elif "reset zoom" in query:
                    pyautogui.hotkey('ctrl', '0')
                elif "refresh page" in query:
                    pyautogui.hotkey('ctrl', 'r')
                elif "developer tools" in query:
                    pyautogui.hotkey('ctrl', 'shift', 'i')
                elif "task manager" in query:
                    pyautogui.hotkey('shift', 'esc')
                elif "full screen" in query:
                    pyautogui.hotkey('f11')
                elif "print page" in query:
                    pyautogui.hotkey('ctrl', 'p')
                elif "save page" in query:
                    pyautogui.hotkey('ctrl', 's')
                elif "incognito mode" in query:
                    pyautogui.hotkey('ctrl', 'shift', 'n')
                elif "bookmark bar" in query:
                    pyautogui.hotkey('ctrl', 'shift', 'b')
                elif "show downloads" in query:
                    pyautogui.hotkey('ctrl', 'j')
                elif "clear browsing data" in query:
                    pyautogui.hotkey('ctrl', 'shift', 'delete')
                elif "address bar" in query:
                    pyautogui.hotkey('ctrl', 'l')
                    
                elif "task manager" in query:
                    pyautogui.hotkey('ctrl', 'shift', 'esc')  # Open Task Manager
                    speak("Task Manager opened.")
    
                elif "control panel" in query:
                    os.startfile('Control Panel')  
                    speak("Control Panel opened.")
                
                elif "settings" in query:
                    os.startfile('ms-settings:')  
                    speak("Settings opened.")
                
                
                    
                elif "file explorer" in query:
                    os.startfile('explorer')  
                    speak("File Explorer opened.")
                
                elif "minimize all windows" in query:
                    pyautogui.hotkey('win', 'd')  
                    speak("All windows minimized.")
                
                elif "maximize window" in query:
                    pyautogui.hotkey('win', 'up')  
                    speak("Window maximized.")
                
                elif "close window" in query:
                    pyautogui.hotkey('alt', 'f4')  
                    speak("Window closed.")
                
                elif "start menu" in query:
                    pyautogui.hotkey('win') 
                    speak("Start Menu opened.")
                
                elif "calculator" in query:
                    os.startfile('calc')  
                    speak("Calculator opened.")
                
                elif "notepad" in query:
                    os.startfile('notepad') 
                    speak("Notepad opened.")
                
                elif "command prompt" in query:
                    os.startfile('cmd')  
                    speak("Command Prompt opened.")
                
                elif "search" in query:
                    pyautogui.hotkey('win', 's')  
                    speak("Windows Search opened.")
                
                elif "device manager" in query:
                    os.startfile('devmgmt.msc')  
                    speak("Device Manager opened.")
                
                elif "network settings" in query:
                    os.startfile('ms-settings:network')  
                    speak("Network Settings opened.")
                
                elif "system information" in query:
                    os.startfile('msinfo32')  
                    speak("System Information opened.")
                
                elif "windows defender" in query:
                    os.startfile('windowsdefender:')  
                    speak("Windows Defender opened.")
                
                elif "volume up" in query:
                    pyautogui.hotkey('volumewheel', 'up')  
                    speak("Volume increased.")
                
                elif "volume down" in query:
                    pyautogui.hotkey('volumewheel', 'down')  
                    speak("Volume decreased.")
                
                elif "mute" in query:
                    pyautogui.hotkey('volumewheel', 'mute')  
                    speak("Volume muted.")
                
                elif "eject" in query:
                    pyautogui.hotkey('win', 'e') 
                    speak("Eject command sent.")
                
                elif "wifi" in query:
                    pyautogui.hotkey('win', 'a')  
                    speak("Opened Action Center.")
                
                elif "bluetooth" in query:
                    pyautogui.hotkey('win', 'a')  
                    speak("Opened Action Center.")
                elif "increase brightness" in query:
                    pyautogui.hotkey('fn', 'f2')  
                    speak("Brightness decreased.")
                elif "decrease brightness" in query:
                    pyautogui.hotkey('fn', 'f3')  
                    speak("Brightness increased.")
                elif "reset brightness" in query:
                    pyautogui.hotkey('fn', 'f4')  
                    speak("Brightness reset.")

                elif "switch window" in query:
                    pyautogui.hotkey('alt', 'tab') 
                    speak("Switched to the next window.")











                
                elif "exit" in query:
                    speak("Exiting control mode.")
                    break

                elif 'skip' in query:

                    pyautogui.press('l')

                elif 'back' in query:

                    pyautogui.press('j')

                elif 'increase speed' in query:

                    pyautogui.hotkey('SHIFT + .')

                elif 'decrease speed' in query:

                    pyautogui.hotkey('SHIFT + ,')

                elif "scrolldown" in query:
                    pyautogui.hotkey("space")

                elif "scroll up" in query:
                    pyautogui.hotkey("space", "up")

                elif 'search in youtube' in query:

                    click(x=667, y=146)

                    speak("What To Search Sir ?")

                    search = takeCommand().lower()

                    write(search)

                    sleep(0.8)

                    pyautogui.press('enter')

                elif 'mute' in query:

                    pyautogui.press('m')

                elif 'unmute' in query:

                    pyautogui.press('m')

                    pyautogui.hotkey('ctrl + t')

                elif 'close tab' in query:

                    pyautogui.hotkey('ctrl + w')

                elif 'new window' in query:

                    pyautogui.hotkey('ctrl + n')

                elif 'history' in query:

                    pyautogui.hotkey('ctrl + h')

                elif 'download' in query:

                    pyautogui.hotkey('ctrl + j')

                elif 'bookmark' in query:

                    pyautogui.hotkey('ctrl + d')

                    pyautogui.press('enter')

                elif 'incognito' in query:

                    pyautogui.hotkey('Ctrl + Shift + n')

                elif 'scroll to top' in query:
                    scroll_to_top()
                elif 'scroll to bottom' in query:
                    scroll_to_bottom()
                elif 'maximize window' in query:
                    maximize_window()
                elif 'minimize window' in query:
                    minimize_window()
                elif 'fullscreen mode' in query:
                    fullscreen_mode()
              
                
               
                    
                elif "find images" in query or "search images" in query:
                    find_images()
                    
                # elif "send message" in query or "phone call" in query or "video call" in query:
                #     flag = ""
                #     contact_no, name = findContact(query)
                #     if (contact_no != 0):

                #         if "send message" in query:
                #             flag = 'message'
                #             speak("what message to send")
                #             query = takeCommand()

                #         elif "phone call" in query:
                #             flag = 'call'
                #         else:
                #             flag = 'video call'

                #         whatsApp(contact_no, query, flag, name)
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that", " ")
                    rememberMessage = query.replace("venom", " ")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt", "a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what i told you to remember" in query:
                    remember = open("Remember.txt", "r")
                    speak("You told me to remember that" + remember.read())
                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    webbrowser.open(
                        "https://www.youtube.com/watch?v=rFPl2XY0uv4")
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()
                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate", "")
                    query = query.replace("venom", "")
                    Calc(query)

                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    speak(
                        "Do you wish to shutdown your computer? (yes/no)")
                    shutdown = takeCommand().lower()
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break
                elif "restart the system" in query:
                    speak("Are You sure you want to restart")
                    speak(
                        "Do you wish to restart your computer? (yes/no)")
                    shutdown = takeCommand().lower()
                    if shutdown == "yes":
                        os.system("shutdown /r /t 1")

                    elif shutdown == "no":
                        break



                elif "schedule my day" in query:
                  schedule_day()
                        
                elif "show my schedule" in query:
                    show_schedule()
                    # notifications.notify(
                    #     title="My schedule :-",
                    #     message=content,
                    #     timeout=15)
                elif "ipl score" in query:
                   fetch_ipl_score()
                    # notification.notify(
                    #     title="IPL SCORE :- ",
                    #     message=f"{team1} : {team1_score} {
                    #         team2} : {team2_score}",
                    #     timeout=15
                    # )
                elif "play a game" in query:
                    game_play()
                elif "take screenshot" in query:
                    take_screenshot()
                elif "click my photo" in query:
                    take_photo()
                # elif "translate" in query:

                #     from Translator import translategl
                #     query = query.replace("venom", "")
                #     query = query.replace("translate", "")
                #     translategl(query)
                
                elif "email" in query or "gmail" in query:
                    email_list = {
                        'siddu': 'singam2002godi@gmail.com'
                    }
                    try:
                        speak("To whom to send mai")
                        name = takeCommand.lower()
                        reciver = email_list[name]

                        speak("what is the subject of the mail")
                        subject = takeCommand.lower()

                        speak("what is teh content to send")
                        cont = takeCommand.lower()
                        sendmail(reciver, subject, cont)
                        speak("email sent successfully")
                    except Exception as e:
                        print(e)
                        speak("unbale to send mail")

                elif "flip" in query:
                    flip()
                elif "cpu" in query:
                    cpu()
                elif "read" in query:
                    text2speech()
                elif "joke" in query:
                    speak(pyjokes.get_joke())
                elif "ip" in query:
                    ip_address = requests.get(
                        'https://api64.ipify.org?format=json').json()
                    speak("sir, your ip address is")
                    speak(ip_address["ip"])
                elif 'facebook' in query:
                    speak('opening your facebook')
                    webbrowser.open('https://www.facebook.com/')
                elif 'whatsapp' in query:
                    speak('opening your whatsapp')
                    webbrowser.open('https://web.whatsapp.com/')
                elif 'instagram' in query:
                    speak('opening your instagram')
                    webbrowser.open('https://www.instagram.com/')
                elif "instagram profile" in query:
                    Instagram_Pro()
                elif 'twitter' in query:
                    speak('opening your twitter')
                    webbrowser.open('https://twitter.com/')
                elif 'discord' in query:
                    speak('opening your discord')
                    webbrowser.open('https://discord.com/channels/@me')
                
                elif ('media player' in query):
                    speak('Opening VLC media player')
                    os.startfile("C:\Program Files\VideoLAN\VLC\vlc.exe")

                elif ('close calculator' in query):
                    speak("okay boss, closeing caliculator")
                    os.system("taskkill /f /im calc.exe")
                elif ('close paint' in query):
                    speak("okay boss, closeing mspaint")
                    os.system("taskkill /f /im mspaint.exe")
                elif ('close notepad' in query):
                    speak("okay boss, closeing notepad")
                    os.system("taskkill /f /im notepad.exe")
                elif ('close discord' in query):
                    speak("okay boss, closeing discord")
                    os.system("taskkill /f /im Discord.exe")
                elif ('close editor' in query):
                    speak("okay boss, closeing vs code")
                    os.system("taskkill /f /im Code.exe")
                elif ('close spotify' in query):
                    speak("okay boss, closeing spotify")
                    os.system("taskkill /f /im Spotify.exe")
                elif ('close lt spice' in query):
                    speak("okay boss, closeing lt spice")
                    os.system("taskkill /f /im XVIIx64.exe")
                elif ('close steam' in query):
                    speak("okay boss, closeing steam")
                    os.system("taskkill /f /im steam.exe")
                elif ('close media player' in query):
                    speak("okay boss, closeing media player")
                    os.system("taskkill /f /im vlc.exe")
                elif "venom" in query:
                    continue

                else:

                    # speak(chatBot(query))
                    speak(
                        "i am not coded for your request, do you want me to contact with AI chatbot")
                    op = takeCommand().lower()
                    if "yes" in op:
                        chatBot(query)
                    # elif "no" in op:
                    #     speak("okay sir")

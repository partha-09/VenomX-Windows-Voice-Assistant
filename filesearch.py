import speech_recognition as sr
import pyttsx3
import os
import subprocess
import sys

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Paths to search in
paths = {
    "desktop": os.path.join(os.path.expanduser("~"), "Desktop"),
    "documents": os.path.join(os.path.expanduser("~"), "Documents"),
    "music": os.path.join(os.path.expanduser("~"), "Music"),
    "videos": os.path.join(os.path.expanduser("~"), "Videos"),
    "downloads": os.path.join(os.path.expanduser("~"), "Downloads"),
    "pictures": os.path.join(os.path.expanduser("~"), "Pictures"),
    'videos': os.path.join(os.path.expanduser('~'), 'Videos'),
    'favorites': os.path.join(os.path.expanduser('~'), 'Favorites'),
    'appdata': os.path.join(os.environ['APPDATA']),
    'local_appdata': os.path.join(os.environ['LOCALAPPDATA']),
    'program_files': os.path.join(os.environ['PROGRAMFILES']),
    'program_files_x86': os.path.join(os.environ['PROGRAMFILES(X86)']),
    'start_menu': os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu'),
    'startup': os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup'),
    'system32': os.path.join(os.environ['WINDIR'], 'System32'),
    'windows': os.environ['WINDIR'],
    'new volume d': 'D:\\'
}


def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()


def listen_command():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        print("listening")
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Command received: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
    except sr.RequestError:
        speak("Could not request results from the speech recognition service.")
    return ""


def search_file(directory, filename):
    for root, _, files in os.walk(directory):
        for file in files:
            if filename.lower() in file.lower():
                return os.path.join(root, file)
    return None


def searchfile():
    location_prompt = "Where do you want to search? file "
    speak(location_prompt)
    location = listen_command()

    if location in paths:
        directory = paths[location]
        file_prompt = f"What is the name of the file you are looking for in {location}?"
        speak(file_prompt)
        filename = listen_command()

        if filename:
            speak(f"Searching for {filename} in {location}. Please wait.")
            found_file = search_file(directory, filename)
            if found_file:
                speak(f"Opening {filename}")
                if os.name == 'nt':  # Windows
                    os.startfile(found_file)
                
            else:
                speak("File not found.")
                
        else:
            speak("No file name provided.")
            
    else:
        speak("Invalid location specified.")
        


def search_folder(directory, foldername):
    for root, dirs, _ in os.walk(directory):
        for dir in dirs:
            if foldername.lower() in dir.lower():
                return os.path.join(root, dir)
    return None


def searchfoler():
    while True:

        command = "search folder"

        if "search folder" in command:
            location_prompt = "Where do you want to search? "
            location = listen_command()

            if location in paths:
                directory = paths[location]
            elif os.path.exists(location):
                directory = location
            else:
                speak("Invalid location specified. Please try again.")
                continue

            folder_prompt = f"What is the name of the folder you are looking for in {location}?"
            speak(folder_prompt)
            foldername = listen_command()

            if foldername:
                speak(
                    f"Searching for {foldername} in {location}. Please wait.")
                found_folder = search_folder(directory, foldername)
                if found_folder:
                    speak(f"Opening {foldername}")
                    if os.name == 'nt':  # Windows
                        os.startfile(found_folder)
                    elif os.name == 'posix':  # macOS or Linux
                        subprocess.call(('open', found_folder) if sys.platform == 'darwin' else (
                            'xdg-open', found_folder))
                else:
                    speak("Folder not found.")
            else:
                speak("No folder name provided.")
        else:
            speak("No search command detected. Please say 'search folder' followed by the location and folder name.")

        speak("Do you want to search for another folder? Say 'yes' to continue or 'no' to exit.")
        retry_command = listen_command()
        if 'no' in retry_command:
            speak("okay SiR!")
            break

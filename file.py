
import os
import shutil
import subprocess
import pyautogui
import pyttsx3

import os
import pyautogui
import pyttsx3
import speech_recognition
import os
import time
import webbrowser
import pyautogui
from features import *

import pyttsx3
import speech_recognition
import webbrowser
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)


from Resources import *


def navigate_to_directory(location):
    try:
        os.chdir(location)
        speak(f"Current directory changed ")
    except FileNotFoundError:
        speak(f"Directory not found!")


def open_file_manager():
    speak("Opening file manager...")
    try:
        subprocess.Popen("explorer")
    except Exception as e:
        speak(f"Error occurred while opening file manager: {e}")


def create_folder(folder_name):
    try:
        os.makedirs(folder_name)
        speak(f"Folder {folder_name} created successfully!")
    except FileExistsError:
        speak(f"Folder {folder_name} already exists!")


def create_file(file_name):
    try:
        with open(file_name, 'w') as f:
            f.write('')
        speak(f"File {file_name} created successfully!")
    except Exception as e:
        speak(f"Error occurred while creating {file_name}: ")


def search_file(file_name):
    matches = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file_name in file:
                matches.append(os.path.join(root, file))
    if matches:
        speak(f"Found {len(matches)} matches for {file_name}:")
        for match in matches:
            speak(match)
    else:
        speak(f"No matches found for {file_name}.")


def search_folder(folder_name):
    matches = []
    for root, dirs, files in os.walk('.'):
        for dir in dirs:
            if folder_name in dir:
                matches.append(os.path.join(root, dir))
    if matches:
        speak(f"Found {len(matches)} matches for {folder_name}:")
        for match in matches:
            speak(match)
    else:
        speak(f"No matches found for {folder_name}.")


def delete_file(file_name):
    try:
        os.remove(file_name)
        speak(f"File {file_name} deleted successfully!")
    except FileNotFoundError:
        speak(f"File {file_name} not found!")
    except Exception as e:
        speak(f"Error occurred while deleting {file_name}: {e}")


def delete_folder(folder_name):
    try:
        os.rmdir(folder_name)
        speak(f"Folder {folder_name} deleted successfully!")
    except FileNotFoundError:
        speak(f"Folder {folder_name} not found!")
    except Exception as e:
        speak(f"Error occurred while deleting {folder_name}: {e}")


def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        speak(f"File {source} copied to {destination} successfully!")
    except FileNotFoundError:
        speak(f"File {source} not found!")
    except Exception as e:
        speak(f"Error occurred while copying {source} to {destination}:")


def copy_folder(source, destination):
    try:
        shutil.copytree(source, destination)
        speak(f"Folder {source} copied to {destination} successfully!")
    except FileNotFoundError:
        speak(f"Folder {source} not found!")
    except Exception as e:
        speak(f"Error occurred while copying {source} to {destination}: ")


def move_file(source, destination):
    try:
        shutil.move(source, destination)
        speak(f"File {source} moved to {destination} successfully!")
    except FileNotFoundError:
        speak(f"File {source} not found!")
    except Exception as e:
        speak(f"Error occurred while moving {source} to {destination}: {e}")


def move_folder(source, destination):
    try:
        shutil.move(source, destination)
        speak(f"Folder {source} moved to {destination} successfully!")
    except FileNotFoundError:
        speak(f"Folder {source} not found!")
    except Exception as e:
        speak(f"Error occurred while moving {source} to {destination}: {e}")


def Fileoperations():
    locations = {
        'desktop': os.path.join(os.path.expanduser('~'), 'Desktop'),
        'documents': os.path.join(os.path.expanduser('~'), 'Documents'),
        'downloads': os.path.join(os.path.expanduser('~'), 'Downloads'),
        'music': os.path.join(os.path.expanduser('~'), 'Music'),
        'pictures': os.path.join(os.path.expanduser('~'), 'Pictures'),
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

    speak("Welcome! I can help you with various file operations. Here are the available functionalities:")
    speak("1. Create File")
    speak("2. Create Folder")
    speak("3. open File")
    speak("4. open Folder")
    speak("5. Delete File")
    speak("6. Delete Folder")
    speak("7. Copy File")
    speak("8. Copy Folder")
    speak("9. Move File")
    speak("10. Move Folder")
    speak("11. Navigate through File Manager")
    speak("Please tell me which operation you would like to perform.")
    print("Welcome! I can help you with various file operations. Here are the available functionalities:")
    print("1. Create File")
    print("2. Create Folder")
    print("3. open File")
    print("4. open Folder")
    print("5. Delete File")
    print("6. Delete Folder")
    print("7. Copy File")
    print("8. Copy Folder")
    print("9. Move File")
    print("10. Move Folder")
    # print("11. Navigate through File Manager")
    print("Please tell me which operation you would like to perform.")
    action = takeCommand().lower()
    if 'create file' in action:
            speak("Please specify the location where you want to create the file.")
            location = takeCommand().lower()
            speak("Please specify the name for the new file.")
            file_name = takeCommand().lower()
            navigate_to_directory(locations.get(location.lower(), os.getcwd()))
            create_file(file_name)
    elif 'create folder' in action:
            speak("Please specify the location where you want to create the folder.")
            location =takeCommand().lower()
            speak("Please specify the name for the new folder.")
            folder_name = takeCommand().lower()
            navigate_to_directory(locations.get(location.lower(), os.getcwd()))
            create_folder(folder_name)
    elif 'open file'  in action:
            
            from filesearch import search_file
            search_file()
    elif 'open folder'  in action:
            from filesearch import searchfoler
            searchfoler()
    elif 'delete file'  in action:
            speak("Please specify the location where the file is located.")
            location = takeCommand().lower()
            speak("Please specify the name of the file you want to delete.")
            file_name = takeCommand().lower()
            navigate_to_directory(locations.get(location.lower(), os.getcwd()))
            delete_file(file_name)
    elif 'delete folder'  in action:
            speak("Please specify the location where the folder is located.")
            location = takeCommand().lower()
            speak("Please specify the name of the folder you want to delete.")
            folder_name = takeCommand().lower()
            navigate_to_directory(locations.get(location.lower(), os.getcwd()))
            delete_folder(folder_name)
    elif 'copy file':
            speak("Please specify the source location of the file.")
            source_location = takeCommand().lower()
            speak(
                "Please specify the destination location where you want to copy the file.")
            destination_location = takeCommand().lower()
            speak("Please specify the name of the file you want to copy.")
            source = takeCommand().lower()
            navigate_to_directory(locations.get(
                source_location.lower(), os.getcwd()))
            speak(
                "Please specify the destination folder where you want to copy the file.")
            destination = os.path.join(locations.get(
                destination_location.lower(), os.getcwd()), os.path.basename(source))
            copy_file(source, destination)
    elif 'copy folder'  in action:
            speak("Please specify the source location of the folder.")
            source_location = takeCommand().lower()
            speak(
                "Please specify the destination location where you want to copy the folder.")
            destination_location = takeCommand().lower()
            speak("Please specify the name of the folder you want to copy.")
            source = takeCommand().lower()
            navigate_to_directory(locations.get(
                source_location.lower(), os.getcwd()))
            speak(
                "Please specify the destination folder where you want to copy the folder.")
            destination = os.path.join(locations.get(
                destination_location.lower(), os.getcwd()), os.path.basename(source))
            copy_folder(source, destination)
    elif 'move file'  in action:
            speak("Please specify the source location of the file.")
            source_location = takeCommand().lower()
            speak(
                "Please specify the destination location where you want to move the file.")
            destination_location = takeCommand().lower()
            speak("Please specify the name of the file you want to move.")
            source = takeCommand().lower()
            navigate_to_directory(locations.get(
                source_location.lower(), os.getcwd()))
            speak(
                "Please specify the destination folder where you want to move the file.")
            destination = os.path.join(locations.get(
                destination_location.lower(), os.getcwd()), os.path.basename(source))
            move_file(source, destination)
    elif 'move folder'  in action:
            speak("Please specify the source location of the folder.")
            source_location = takeCommand().lower()
            speak(
                "Please specify the destination location where you want to move the folder.")
            destination_location = takeCommand().lower()
            speak("Please specify the name of the folder you want to move.")
            source = takeCommand().lower()
            navigate_to_directory(locations.get(
                source_location.lower(), os.getcwd()))
            speak(
                "Please specify the destination folder where you want to move the folder.")
            destination = os.path.join(locations.get(
                destination_location.lower(), os.getcwd()), os.path.basename(source))
            move_folder(source, destination)
    elif  'navigate through file manager'  in action:
            open_file_manager()
            speak("File manager opened. What would you like to do?")
            speak("1. Navigate to a folder")
            speak("2. Perform other file operations")
            choice = takeCommand().lower()
            if 'navigate to folder' in choice:
                speak("Please specify the folder you want to navigate to.")
                folder = takeCommand().lower()
                navigate_to_directory(folder)
            elif 'perform other file operations' in choice:
                print()
            elif "close"  in choice:
                pyautogui.hotkey('alt', 'f4')
            else:
                speak("Invalid choice!")

    elif 'exit' in action:
            speak("Exiting file operations. bye!")
            

    else:
            speak("Invalid choice! Please try again.")

        
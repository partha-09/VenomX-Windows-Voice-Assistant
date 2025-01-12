import requests
import json
import pyttsx3

from Resources import *




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
        break

    speak("thats all")

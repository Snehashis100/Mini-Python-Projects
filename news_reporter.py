""" A simple text to speech program"""
import pyttsx3
import requests
import json
def speak(str):
    engine = pyttsx3.init()
    engine.say(str)
    engine.runAndWait()
if __name__ == '__main__':
    url='http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=632d6bec70874cad843839749bbea144'
    content=requests.get(url=url)
    content=content.text
    speach=json.loads(content)
    speak("Today's news")
    articles=speach['articles']
    for article in articles:
        speak(article['title'])
    speak("Thank you")

"""
https://www.youtube.com/watch?v=LzYNWme1W6Q&list=WL&index=9&t=8669s&ab_channel=Amigoscode
"""


# Fetching Jokes from Internet
# # PIP and Requests Module

# """
# PIP is package manager for Python
# """

import requests
import json # to read json object

# text to speech
import pyttsx3
engine = pyttsx3.init() # oject creation
voices = engine.getProperty('voices') #get voice detail
engine.setProperty('voice', voices[1].id) # change voice [0] for male and [1] for female
engine.runAndWait()

url = 'http://official-joke-api.appspot.com/random_ten'

response = requests.get(url)
#print(r.getcode())

jsonData = json.loads(response.text)
#print(jsonData)

class Joke:
    def __init__(self, setup, punchline):
        self.setup = setup
        self.punchline = punchline
    def __str__(self):
        return f'setup: {self.setup}.\nPunchline: {self.punchline}'
    
jokes =[]
        
for j in jsonData:
    setup = j['setup']
    punchline = j['punchline']
    joke = Joke(setup, punchline)
    jokes.append(joke)
    
    
print(f' Got {len(jokes)} jokes')

for j in jokes:
    print(j)
    pyttsx3.speak(j.setup)
    pyttsx3.speak(j.punchline)

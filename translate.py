# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 21:22:46 2020

@author: JellyIss
"""

from googletrans import Translator
import requests
import json

def googletrans():
    translator = Translator()
    result = translator.translate('How do you do?',dest='pl')
    print(result.text)

def piratetrans(text):
    url = 'https://api.funtranslations.com/translate/pirate.json'
    data = {'text': text}
    requests.post(url, data=data)
    
    response = requests.post(url, data=data)
    json_data= json.loads(response.text)
    print(type(json_data))
    print(json_data['contents']['translated'])
    
piratetrans('hello, sir')
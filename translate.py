# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 21:22:46 2020

@author: JellyIss
"""

from googletrans import Translator

def main():
    translator = Translator()
    result = translator.translate('Jak się masz?',dest='de')
    print(result.text)
    
main()
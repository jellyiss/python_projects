# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:00:06 2020

@author: JellyIss
"""

import urllib.request
from bs4 import BeautifulSoup

def extract(url):
    
    site = urllib.request.urlopen(url)
    html = BeautifulSoup(site.read(), 'html.parser')
    ol_anc = html.find_all('ol')
    anc = []
    
    for ollist in ol_anc:
        anc.append(ollist.findChildren())
    return anc

def main():
    
    url = input("Place your url here: ")
    print( "Extracting...")
    
    thelist = extract(url)
    
    for li_anc in thelist:
        print()
        for nr, li in enumerate(li_anc, 1):
            print(f"{nr}. {li.text}")

if __name__ == "__main__":
    main()
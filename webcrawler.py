# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:31:53 2020

@author: JellyIss
"""

import urllib.request
from bs4 import BeautifulSoup
import urllib.parse

def main():
    print('Getting staff urls...')
    
    staff_url = 'http://wa.amu.edu.pl/wa/pl/staff_list'
    staff_content = get_content(staff_url)
     
    links = staff_content.find_all('a')
    
    urls = []
    
    for link in links:
        if len(link.get_text()) > 1:
            base_url = 'http://wa.amu.edu.pl'
            url = urllib.parse.urljoin(base_url,link['href'])
            encoded_url = fix_encoding(url)
            urls.append(url)
    
    print('Staff emails found:')
    for url in urls:
        print(get_details(url))
      
    
def fix_encoding(url):
    compoments = urllib.parse.urlsplit(url)
    compoments = list(compoments)
    compoments[2] = urllib.parse.quote(compoments[2])
    return urllib.parse.urlunsplit(compoments)
    
    
def get_content(url):
    response = urllib.request.urlopen(url)
    data = response.read()
    doc = BeautifulSoup(data, 'html.parser')
    return doc.find(id='tresc_wlasciwa')


def get_details(url):
    try:
        content = get_content(url)
    except:
        print('Error getting detail from', url)
        return 'No content'
    header = content.find('h1')
    links = content.find_all('a')
    for link in links:
        if link.has_attr('href') and link['href'].startswith('mailto:'):
            email = link.get_text()
            return header.get_text() + ': ' + email
    return header.get_text() + ' (no email found)'

main()
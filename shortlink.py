#!/usr/bin/env python3

# Shortlink terbaru
# Don't not recode !!
# Hanya untuk di pelajari

import os
import sys

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Please install module requests and bs4!")
    exit()


def shortlink(url):
    data = {
        'url': url
    }
    req = requests.post(url='http://www.portchecker.us/short_link.php', data=data).text
    hasil = BeautifulSoup(req, features='html.parser').find('input', {'id': 'myInput'})
    if (hasil == None):
        link = 'None'
    else:
        link = hasil.get('value')
    return link
try:
    web = input("Masukan nama web : ")
    link = shortlink(web)
    print("Link short : " + link)
except KeyboardInterrupt:
    print("CTRL + C Detect!!")
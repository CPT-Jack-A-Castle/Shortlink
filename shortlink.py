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
    print("Module urllib3 belom di instal!!")
    print("Tolong install module terlebih dahulu")
    exit()


def shortlink(url):
    data = {
        'url': url
    }
    req = requests.post(url='http://www.portchecker.us/short_link.php', data=data).text
    hasil = BeautifulSoup(req, 'html.parser').find('input', {'id': 'myInput'})
    link = hasil.get('value')
    return link
try:
    web = input("Masukan nama web : ")
    link = shortlink(web)
    print("Link short : " + link)
except KeyboardInterrupt:
    print("CTRL + C Detect!!")

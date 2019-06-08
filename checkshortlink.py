#!/usr/bin/python
# -*- encoding: utf-8 -*-

import os, sys, time

# example shortlink : https://tinyurl.com/y3rltmq9
try:
    import requests
    from bs4 import BeautifulSoup
except ImportError as e:
    print("Module requests dan bs4 belom di install !!")
    print("Tolong install dahulu sebelum menggunakan tools ini!!")

class checkShortlink:
    def __init__(self, url):
        self.url = 'http://checkshorturl.com/expand.php'
        self.session = requests.Session()
        self.data = {
            'u': url
        }
        try:
            self.req = self.session.post(self.url, data=self.data, allow_redirects=True)
        except:
            print("ERROR: Jalankan ulang ini program!")
            sys.exit(0)
        self.soup = BeautifulSoup(self.req.text, features='html.parser')
        self.author = self.soup.find_all('td')[19].get_text()
        self.longURL = self.soup.find_all('td')[1].find('a').get('href')
        self.shortURL = self.soup.find_all('td')[5].get_text()
        self.delay = self.soup.find_all('td')[3].get_text()
        self.title = self.soup.find_all('td')[13].get_text()
        self.description = self.soup.find_all('td')[15].get_text()
        self.keywords = self.soup.find_all('td')[17].get_text()
        print("Author : {}".format(self.author))
        print("Long URL : {}".format(self.longURL))
        print("Short URL : {}".format(self.shortURL))
        print("Delay : {}".format(self.delay))
        print("Title : {}".format(self.title))
        print("Description : {}".format(self.description))
        print("Keywords : {}".format(self.keywords))

web = input(str('Masukan website : '))
if 'tinyurl.com' in web:
    checkShortlink(web)
elif 't.co' in web:
    checkShortlink(web)
elif 'bit.ly' in web:
    checkShortlink(web)
elif 'goo.gl' in web:
    checkShortlink(web)
elif 'amzn.to' in web:
    checkShortlink(web)
elif 'ow.ly' in web:
    checkShortlink(web)
elif 'youtu.be' in web:
    checkShortlink(web)
else:
    print("Masukan shortlink yang benar!!")
    print("Shortlink yang di support : t.co, goo.gl, bit.ly, amzn.to, tinyurl.com, ow.ly, youtu.be")

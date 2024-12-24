#!/usr/bin/python
# coding: utf-8
#“De Quincey describes using the stars to guide him home. Having no knowledge of celestial navigation he finds himself in unfamiliar territories, discovering what he believes are streets anonymous to maps, thus reimagining the city in his own eyes.” (http://www.thedoublenegative.co.uk/2014/12/an-introduction-to-psychogeography/)

import string
import random
import decimal
import textwrap
import sys
import time
from random import randint
import webbrowser

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering
        time.sleep(random.random() * 0.1)


# Just alphanumeric characters
chars = string.letters + string.digits

# Alphanumeric + special characters
chars = string.letters + string.digits + string.punctuation

routeLength = 10

slowprint('\n' + "Dear flaneur/flaneuse, interpret the following string as a pathway:" + '\n' + ''.join((random.choice(chars)) for x in range(routeLength)) + '\n')

urls = ['https://www.google.com/maps']

for url in urls:
    webbrowser.open_new_tab(url)


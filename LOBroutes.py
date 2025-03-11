#!/usr/bin/python
# coding: utf-8
#“This much is already known: for every sensible line of straightforward statement, there are leagues of senseless cacophonies, verbal jumbles and incoherences. (I know of an uncouth region whose librarians repudiate the vain and superstitious custom of finding a meaning in books and equate it with that of finding a meaning in dreams or in the chaotic lines of one’s palm.” 
#“De Quincey describes using the stars to guide him home. Having no knowledge of celestial navigation he finds himself in unfamiliar territories, discovering what he believes are streets anonymous to maps, thus reimagining the city in his own eyes.” 

import string
import random
import decimal
import sys
import time
import textwrap
from random import randint
import webbrowser


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering
        time.sleep(random.random() * 0.1)


# Just alphanumeric characters
chars = string.ascii_letters + string.digits

# Alphanumeric + special characters
chars = string.ascii_letters + string.digits + string.punctuation

routeLength = 410

slowprint('\n' + "Dear flaneurial inhabitant of the Library, interpret the following string, or parts of the string, as a pathway:" + '\n' + '\n' + ''.join((random.choice(chars)) for x in range(routeLength)) + '\n')

urls = ['https://www.google.com/maps']

for url in urls:
    webbrowser.open_new_tab(url)





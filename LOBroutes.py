#!/usr/bin/python
# coding: utf-8
#“Like all men of the Library, I have traveled in my youth. I have journeyed in search of a book, perhaps of the catalogue of catalogues; now that my eyes can scarcely decipher what I write, I am preparing to die a few leagues from the hexagon in which I was born. Once dead, there will not lack pious hands to hurl me over the banister; my sepulchre shall be the unfathomable air: my body will sink lengthily and will corrupt and dissolve in the wind engendered by the fall, which is infinite.” 
#“De Quincey describes using the stars to guide him home. Having no knowledge of celestial navigation he finds himself in unfamiliar territories, discovering what he believes are streets anonymous to maps, thus reimagining the city in his own eyes.” 

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

routeLength = 410

slowprint('\n' + "Dear flaneurial inhabitant of the Library, interpret the following string, or parts of the string, as a pathway:" + '\n' + ''.join((random.choice(chars)) for x in range(routeLength)) + '\n')

urls = ['https://www.google.com/maps']

for url in urls:
    webbrowser.open_new_tab(url)



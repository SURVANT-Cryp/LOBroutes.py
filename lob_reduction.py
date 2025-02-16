#! /usr/bin/pythonw
# coding: utf-8

import random
import sys
import time

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering
        time.sleep(random.random() * 0.01)

import string
from random import randint

# Just alphanumeric characters
chars = '-' '.'

routeLength = 410

slowprint(('\n' + "LOB — Quine's Reduction:" + '\n' + ''.join((random.choice(chars)) for x in range(routeLength)) + '\n'))

#!/usr/python

#Python challenge 3

import re

mess = open("p003.txt").read()
print ''.join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', mess))


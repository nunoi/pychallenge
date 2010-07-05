#!/usr/python

#Python challenge 4

import urllib

val = 46059
for i in range(200):
	params = urllib.urlencode({'nothing': val})
	f = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?%s" % params)
	s = f.read()
	val = s.split()[-1:][0]
	print s


#!/usr/python

#Python challenge 5

import pickle, pprint

pkl_file = open('p005_banner.p', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

pkl_file.close()

for l in data1:
	s = ''
	for t in l:
		c = t[0]
		if c == ' ':
			c = '.'
		n = t[1]
		for i in range(n):
			s += c
	print s


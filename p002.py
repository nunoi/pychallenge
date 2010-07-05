#!/usr/python

#Python challenge 2

f = open('p002.txt', 'r')

s = ''
for line in f:
    for c in line:
	if c.isalpha():
		s += c
print s

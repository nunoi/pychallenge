#!/usr/python

# Python challenge 6
# URL channel.html

import os

nothing = '90052'
##
##filelist = os.listdir('p006_zip')
##
##while True:
##    f = open('p006_zip/' + str(nothing) + '.txt', 'r')
##    s = f.read()
##    nothing = s.split()[len(s.split()) - 1]
##    print s
##    f.close()

# "Collect the comments."

import zipfile

zfile = zipfile.ZipFile('channel.zip', 'r')

end = False
text = ''
while not end:
    zinfo = zfile.getinfo(nothing + '.txt')
    text += zinfo.comment
    f = zfile.open(nothing + '.txt')
    s = f.read()
    nothing = s.split()[len(s.split()) - 1]
    if nothing == 'comments.':
        end = True
    f.close()
    
print text



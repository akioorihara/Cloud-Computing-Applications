#!/usr/bin/env python3

from os import sep
import sys
import string
import re 

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

delimeters = [] 
stopWords = []

# TODO
with open(stopWordsPath) as f:
    # TODO
    for word in f:
        stopWords.extend(word.splitlines()) 

#TODO 
with open(delimitersPath) as f:
    # TODO
    for line in f:
        delimeters.extend(line)

def splitter(line, delimeters):
    for sep in delimeters:
        line = line.replace(sep, " ")
    return [i.strip().lower() for i in line.split()]

i = 0
for line in sys.stdin:
    # TODO
    line = line.strip()
    token = splitter(line, delimeters)
    token = [word for word in token if word not in stopWords]
    token = [word for word in token if word not in '']
    
    for word in token:
        print ("{}\t{}".format(word , 1))
        # print('%s\t%s' % (  ,  )) # pass this output to reducer


# print(line)
#!/usr/bin/env python3
import sys
import re 

mydict = {}
for line in sys.stdin:
  # TODO
    line = line.strip()
    fromPage, count = line.split('\t')
    
    fromPage = int(fromPage) 
#     if fromPage not in mydict:
#        mydict[fromPage] = []

    count = int(count)
    if fromPage not in mydict: 
       mydict[fromPage] = 0
       
    mydict[fromPage] = mydict[fromPage] + count            
      
for key in mydict:
    print('%s\t%s' % (key, mydict[key])) #key = webpage # 
  # (child) 90: (parent)421957 
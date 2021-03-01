#!/usr/bin/env python3
import sys

count = {}
for line in sys.stdin:
  #TODO
  fromPage, toPage = line.split(':')
  toPage = toPage.strip().split(" ")
  
  for value in toPage:
    if value not in count:
      count[value] = 1
    else:
      count[value] += 1

for i in count: 
  print('%s\t%s' % (i, count[i])) #pass this output to reducer

# 385744: 421957 3250680 3446893 5166549
#!/usr/bin/env python3
import sys


for line in sys.stdin:
  #TODO
  fromPage, toPage = line.split(':')
  toPage = toPage.strip().split(" ")

  for i in toPage: 
      print('%s\t%s' % (i, 1)) #pass this output to reducer

# 385744: 421957 3250680 3446893 5166549
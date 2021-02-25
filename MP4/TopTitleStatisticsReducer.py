#!/usr/bin/env python3
import sys
import math


#TODO
sum = 0
mean = 0
min = 0 #I have to fix this later 
max = 0 
var = 0
count = 0 
data = {}

def check_max(x):
    global max 
    if int(max) <= int(x):
        max = int(x) 

def check_min(x):
    global min, count 
    if count == 1: 
        min = x
    if int(min) >= int(x):
        min = int(x)

def check_ver(x,y):
    
    return x 

for line in sys.stdin:
    # TODO
    line = line.strip()
    word, number = line.split('\t')
    check_max(number)
    check_min(number)
    # var = check_ver()
    
    sum += int(number) 
    count += 1

mean = sum / count
print(min, max, mean, sum)

#TODO
# print('%s\t%s' % (  ,  )) print as final output

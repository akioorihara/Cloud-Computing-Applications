#!/usr/bin/env python3
import sys
import math


#TODO
sum = 0
mean = 0
min = 0 
max = 0 
var = 0
count = 0 
data = []

def check_max(x):
    global max 
    if int(max) <= int(x):
        max = int(x) 

def check_min(x):
    global min, count 
    if count == 0: 
        min = x
    if int(min) > int(x):
        min = int(x)

for line in sys.stdin:
    # TODO
    line = line.strip()
    word, number = line.split('\t')
    data.append(number)
    check_max(number)
    check_min(number)
    # var = check_ver()
    
    sum += int(number) 
    count += 1

mean = math.floor(sum / count)
for d in data: 
    # print(int(mean) - int(d), "This is var")
    var = var + (int(mean) - int(d))**2
var = math.floor(var / count)

x = [mean, sum, min, max, var]
y = ["Mean", "Sum", "Min", "Max", "Var"]
# print(mean, sum, min, max, var)

#TODO
for index in range(5): 
    print('%s\t%s' % (y[index],x[index])) #print as final output

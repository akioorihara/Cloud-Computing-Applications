#!/usr/bin/env python3
import sys

leaguePath = sys.argv[1]
#TODO
league = []
mydict = {}

with open(leaguePath) as f:
    #TODO      
    for line in f: 
       league.extend([int(x) for x in line.split()]) #int can be read like this 

for line in sys.stdin:
    line.strip()
    page, count = line.split('\t')
 
    page = int(page)
    count = int(count)
    if page not in mydict: 
       mydict[page] = 0
    mydict[page] = mydict[page] + count    


for key in mydict:
    if key in league:
       print('%s\t%s' % (key , mydict[key]))
       # pass

       #TODO
       # print('%s\t%s' % (  ,  )) pass this output to reducer



#compare the only stuff we need to compare and then pass this on to reducer side 
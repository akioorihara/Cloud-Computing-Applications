#!/usr/bin/env python3
import sys

mydict = {}
# input comes from STDIN
for line in sys.stdin:
    # TODO
    line = line.strip()
    fromPage, count = line.split('\t')

    # print(fromPage, count, "<----This is the output")
    count = int(count)
    fromPage = int(fromPage)
    if fromPage not in mydict:
      mydict[fromPage] = count
    else:
      mydict[fromPage] += count
    
popular = sorted(mydict.items(), key = lambda x: x[1], reverse=True)
# swords = sorted(total.items(), key = lambda x: (x[1],x[0]), reverse=True)

# print(popular)
popular = popular[:10] 
for link in popular[::-1]:
   print('%s\t%s' % (link[0], link[1] )) #print as final output

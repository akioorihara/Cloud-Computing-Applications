#!/usr/bin/env python3
import sys
#TODO

mydict = {}
rank = []
small = 0 

# input comes from STDIN
for line in sys.stdin:
    # TODO
    line = line.strip()
    page, count = line.split('\t')
    page = int(page)
    count = int(count)
    mydict[page] = count

popular = sorted(mydict.items(), key = lambda x: (x[0], x[1]), reverse=True)

keys, counts = zip(*popular) #unzip and keys and counts will contain all values 
counts = sorted(counts) 

r = 0
skip = 0
for i in range(len(counts)-1):
    if skip:
        skip -= 1
        continue
    if counts[i] < counts[i+1]:
        rank.append((r, counts[i]))
        r += 1
    else:
        for j in range(i,len(counts)-1):
            if counts[j] == counts[j+1]:
                rank.append((r, counts[j]))
                skip += 1
            else:
                # r += 1
                break
        r += skip 
        # skip = 0 
rank.append((r+1, counts[len(counts)-1])) # last element is len(array) -1  


# #TODO
for link in popular:
    for z in rank:  
        if z[1] == link[1]:
            print('%s\t%s' % (link[0], z[0] )) #print as final output
            break 
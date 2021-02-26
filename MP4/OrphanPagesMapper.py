#!/usr/bin/env python3
import sys
from collections import defaultdict

pID = {}
for line in sys.stdin:
  # TODO
    line = line.strip()
    parent, child = line.split(':')
    child = child.strip().split(" ")
    # pID['parent'] = parent
    # pID['child'] = child
    # print(pID)
    print('%s\t%s' % (parent, child))


  # print('%s\t%s' % ( , )) #pass this output to reducer

# 385744: 421957 3250680 3446893 5166549 #this is a test purpose

#!/usr/bin/env python3
from operator import itemgetter
import sys
# from typing import DefaultDict

#TODO
current_word = None
total = {}
# input comes from STDIN
for line in sys.stdin:
    # TODO
    line.strip()
    word, count = line.split('\t', 1)

    if word not in total:
        total[word] = 0
    total[word] = total[word] + int(count)
    

# TODO
for word in total: 
    print('%s\t%s' % (word, total[word]))

# print('%s\t%s' % (  ,  )) print as final output
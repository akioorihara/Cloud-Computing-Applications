#!/usr/bin/env python3
import sys



total = {}
# input comes from STDIN
for line in sys.stdin:
    # TODO
    line.strip()
    word, count = line.split('\t')
    
    if word not in total:
        total[word] = int(count)
    
    # # TODO
swords = sorted(total.items(), key = lambda x: (x[1],x[0]), reverse=True)
# swords = sorted(total.items(), key = lambda x: (-x[1], x[0]), reverse=True)

x = swords[:10] 
for word in x[::-1]:
    print('%s\t%s' % (word[0], word[1]))
    # print ("{}\t{}".format(word, word[1]))

    # # print('%s\t%s' % (  ,  )) print as final output

    #top 10 count from Mapper   
    #sort 
    
#!/usr/bin/env python2
import random 
import os
import string
import sys
import re
from collections import defaultdict
from operator import itemgetter

stopWordsList = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
            "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
            "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
            "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
            "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
            "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
            "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
            "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
            "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
            "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

delimiters = " \t,;.?!-:@[](){}_*/"

def getIndexes(seed):
    random.seed(seed)
    n = 10000
    number_of_lines = 50000
    ret = []
    for i in range(0,n):
        ret.append(random.randint(0, 50000-1))
    return ret

def process(userID):
    indexes = getIndexes(userID)
    ret = defaultdict(int)
    # TODO

    
    #with open("input.txt","r") as f:
    with sys.stdin as f:
        lines = f.readlines() 
        
        for i in indexes: #take one line and split into words based on delimiters above
            line = lines[i]
            line = filter(lambda x: ord(x) < 128, line)
            line = [l.lower().strip() for l in re.split(' |\t|,|;|\.|\?|!|-|:|@|\[|\]|\(|\)|\{|\}|_|\*|\/', line)]
            for w in line: #use a dictionary to count each word
                #if '&' in w:
                #    print (i, line, w)
                if w not in stopWordsList and w != '':
                    ret[w] += 1


    #sort by words then numbers
    #swords = sorted(ret.items(), key = itemgetter(1,0), reverse=True)
    swords = sorted(ret.items(), key = lambda x: (-x[1], x[0]))

    for word, i in swords[:20]:
        print(word, i)

                    

process(sys.argv[1])

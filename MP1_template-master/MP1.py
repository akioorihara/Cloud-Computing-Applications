# Akio. O CS 498 CCA
import random
import os
import string
import sys
import re
from collections import Counter

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
    # n = 10000 #actual int
    n = 100  # test int

    number_of_lines = 50000
    ret = []
    for i in range(0, n):
        # ret.append(random.randint(0, 50000-1))
        ret.append(random.randint(0, 50-1))
        # print(ret[i])
    return ret


def process(userID):
    indexes = getIndexes(userID)  # original code
    ret = []
    # TODO

    lines = []
    f = open(os.path.join(sys.path[0], "input1.txt"), "r")
    # f = sys.stdin.readlines()
    # lines = [x.strip('\n') for x in f]
    print(lines)
    lines = f.readlines()  # needs to read line by line since it will be replaced with another text file 

    i = 0
    for line in lines:
        ret.append(line.strip().lower().split('_'))
        ret[i] = (re.split(r"['[' \t |\\|/|,|;|.|?|!|-|:|@|{|}|(|)|\[|*|-|\]|-]", str(ret[i])))
        # ret[i] = (re.split(r"['[' \t,();:!-@.{}_*/\\\]]", str(ret[i])))  #& is removed, gotta find out 
        # encode? not sure what to do ....

        while '' in ret[i]:
            ret[i].remove('')
        i += 1

    counts = Counter()

   
    finalRet = []
    countNum = Counter()
    for index in indexes: 
        finalRet.append(ret[index])
        countNum[index] += 1

    for sentense in finalRet:   
        for word in sentense:
            if word not in stopWordsList:
                counts[word] += 1

    print(sorted(counts.most_common(), key=lambda x: (-x[1],[0])))
    print(counts)
    

    # for word in ret:
    #     print(word)

    f.close()


# process(sys.argv[1])   #the original code
process(0)

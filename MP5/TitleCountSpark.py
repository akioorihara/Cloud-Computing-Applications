#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Exectuion Command: spark-submit TitleCountSpark.py stopwords.txt delimiters.txt dataset/titles/ dataset/output'''

import sys, re
from pyspark import SparkConf, SparkContext

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]
# inputFile = sys.argv[3]

delimeters = [] 
stopWords = []

with open(stopWordsPath) as f:
	#TODO
    for word in f:
        stopWords.extend(word.splitlines()) 
        # allstop = f.read().splitlines()

with open(delimitersPath) as f:
    #TODO
    for line in f: 
        delimeters.extend(line)

def splitter(line, delimeters):
    for sep in delimeters:
        line = line.replace(sep, " ")
    return [i.strip().lower() for i in line.split()]


conf = SparkConf().setMaster("local").setAppName("TitleCount")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf = conf)

lines = sc.textFile(sys.argv[3],1)

# e = lines.take(20)
# for i in e:
#     print(i.encode('ascii', 'ignore').decode('ascii'))

# counts = lines.flatMap(lambda line: line.split()) \
counts = lines.flatMap(lambda line: splitter(line, delimeters).strip().split()) \
             .map(lambda word: (word.lower(), 1)) \
             .reduceByKey(lambda a, b: a + b)

output = lines.collect()

total = {}
for line in output:
    line.strip()
    token = splitter(line, delimeters)
    # print(token[0].encode('utf-8'))
    # if (len(token) == 0):
    #     print(line.encode('utf-8').decode(),len(token))
    token = [word for word in token if word not in stopWords]
    token = [word for word in token if word not in '']
    
    for each in token:
        if each not in total:
            total[each] = 1
        else:   
            total[each] += 1 
        # print("%s: %i" % (each.encode('ascii', 'ignore').decode('ascii'), count))


# output.saveAsTextFile(sys.argv[4])
outputFile = open(sys.argv[4],"w")  #probably this way to save in a one file 
swords = sorted(total.items(), key = lambda x: (x[1], x[0]), reverse=True)

x = swords[:5] 
x = sorted(x)
for word in x:
    # print('%s\t%s' % (word[0].encode('utf-8').decode(), word[1]))
    outputFile.write(str(word[0].encode('utf-8').decode()) + '\t' + str(word[1]) + '\n')



# x.saveAsTextFile(sys.argv[4])
# counts.saveAsTextFile(sys.argv[4])   #This will print "mapper side" of the code
#TODO
# print(line.encode('ascii', 'ignore').decode('ascii')) #prints line by line 
# print(inputfile.encode('ascii', 'ignore').decode('ascii'))  #If I print like this and i will get an error since list does not have encoding 

#TODO
#write results to output file. Foramt for each line: (line +"\n")

sc.stop()


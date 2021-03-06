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

counts = lines.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)

### From here
punc = []
def lower_clean(x):
    punc = delimeters
    lowered = x.lower()
    for i in punc:
        lowered = lowered.replace(i, '')
    return lowered

lines = lines.map(lower_clean)
lines.take(100)
lines = lines.flatMap(lambda x: x.split(" "))
lines.take(10)
lines = lines.filter(lambda x: x !='')
lines.take(4)
word_count = lines.map(lambda word: (word, 1))
word_count.take(10)
word_count = word_count.reduceByKey(lambda x, y: (x+y)).sortByKey()
word_count.take(50)
word_count = word_count.map(lambda x : (x[1], x[0]))
word_count.take(30)

###


output = counts.collect()
# print(output)

total = {}
for (line, count) in output:
    line.strip()
    token = splitter(line, delimeters)
    token = [word for word in token if word not in stopWords]
    token = [word for word in token if word not in '']
    
    for each in token: 
        total[each] = int(count)
        # print("%s: %i" % (each.encode('utf-8'), count))


# counts.saveAsTextFile(sys.argv[4])
outputFile = open(sys.argv[4],"w")
swords = sorted(total.items(), key = lambda x: (x[1], x[0]), reverse=True)
x = swords[:10] 
for word in x[::-1]:
    # print('%s\t%s' % (word[0].encode('utf-8'), word[1]))
    outputFile.write(str(word[0].encode('utf-8')) + '\t' + str(word[1]) + '\n')
    



# x.saveAsTextFile(sys.argv[4])
# counts.saveAsTextFile(sys.argv[4])   #This will print "mapper side" of the code
#TODO
# print(line.encode('ascii', 'ignore').decode('ascii')) #prints line by line 
# print(inputfile.encode('ascii', 'ignore').decode('ascii'))  #If I print like this and i will get an error since list does not have encoding 

#TODO
#write results to output file. Foramt for each line: (line +"\n")

sc.stop()


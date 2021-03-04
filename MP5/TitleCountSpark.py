#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Exectuion Command: spark-submit TitleCountSpark.py stopwords.txt delimiters.txt dataset/titles/ dataset/output'''

import sys
from pyspark import SparkConf, SparkContext

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]
# inputFile = sys.argv[3]

delimeters = [] 
stopWords = []
inputfile = [] 

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

counts.saveAsTextFile(sys.argv[4])
# counts.saveAsTextFile()

#TODO
# with open(inputfile) as f:
# with open(inputFile, 'r', encoding="utf-8") as f: 
#     for line in f: 
#         line.strip()
#         inputfile.extend(line)
#         # print(line.encode('ascii', 'ignore').decode('ascii')) #prints line by line 
# # print(inputfile.encode('ascii', 'ignore').decode('ascii'))  #If I print like this and i will get an error since list does not have encoding 

# for i in inputfile:
#     print(i.encode('utf-8'))

# print(lines)
    # line = line.strip()
    # token = splitter(line, delimeters)
    # token = [word for word in token if word not in stopWords]
    # token = [word for word in token if word not in '']




# outputFile = open(sys.argv[4],"w")
#TODO
#write results to output file. Foramt for each line: (line +"\n")

sc.stop()


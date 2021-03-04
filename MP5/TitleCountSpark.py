#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Exectuion Command: spark-submit TitleCountSpark.py stopwords.txt delimiters.txt dataset/titles/ dataset/output'''

import sys
from pyspark import SparkConf, SparkContext
# reload(sys)
# sys.setdefaultencoding('utf-8')

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]
inputFile = sys.argv[3]

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

inputF = [] 
with open(inputFile, 'r', encoding="utf-8") as f: 
    for line in f: 
        inputF.extend(line)
        print(line.encode('ascii', 'ignore').decode('ascii'))

conf = SparkConf().setMaster("local").setAppName("TitleCount")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf = conf)

# lines = sc.textFile(sys.argv[3],1)
#TODO

outputFile = open(sys.argv[4],"w")

#TODO
#write results to output file. Foramt for each line: (line +"\n")

sc.stop()
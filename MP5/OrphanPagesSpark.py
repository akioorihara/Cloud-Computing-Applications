#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("OrphanPages")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf = conf)

lines = sc.textFile(sys.argv[1], 1)
# lines = lines.flatMap(lambda line: ((line.split(":")[0],0), splits((line.split(":")[1])) ))
split_lines = lines.map(lambda x: x.split(":"))
fromPages = split_lines.map(lambda x: (x[0], 0))
toPages = split_lines.flatMap(lambda x: x[1].strip().split())
toPages = toPages.map(lambda x: (x, 1))
allPages =  fromPages.union(toPages)  
allPages = allPages.reduceByKey(lambda x, y: x+y)
text = allPages.filter(lambda x: x[1] == 0).collect()

# print(fromPages.take(20))
# print(toPages.take(20))
# print(allPages.take(3000))

text = sorted(text)

# split_line = lines.map(lambda x: x.split(":"))
# parent = split_line.map(lambda x:x[0])
# children = split_line.map(lambda x:x[1])
output = open(sys.argv[2], "w")
for i in text:
    output.write(str(i[0]) + '\n')

#   # TODO
#     line = line.strip()
#     print(line, "<= LINE")
#     fromPage, toPage = line.split(':')
#     print(toPage.encode('utf-8').decode(), "<= ToPage", fromPage.encode('utf-8').decode(), "<=From page" )
#     # fromPage, toPage = 
#     toPage = toPage.strip().split(" ")
#     print(toPage, "Split toPages <<<<")
#     print(toPage.encode('utf-8').decode(), "<= ToPage", fromPage.encode('utf-8').decode(), "<=From page" )
    #convert everything to ints
#     # fromPage = int(fromPage)
#     toPage = [int(x) for x in toPage]

#     if fromPage in toPage: #self link check 
#         toPage.remove(fromPage)

#     toPages.update(set(toPage)) #holds non orphan 
#     fromPages.add(fromPage)

# for nonorphan in toPages:
#     output.append("n:"+str(nonorphan))

# for potential_orphan in fromPages:
#     output.append("p:"+str(potential_orphan))

# for line in output:
#     print(line)


# #-------End of Mapper 
# #reduce side 
# mydict = {}
# non_orphans = set()
# potential_orphans= set()
# for line in sys.stdin:
#   # TODO
#     line = line.strip()
#     bucket, candidate= line.split(':')

#     candidate = candidate.strip()

#     if bucket is 'n':
#         non_orphans.add(candidate)
#     if bucket is 'p':
#         potential_orphans.add(candidate)

# for x in non_orphans:
#     if x in potential_orphans:
#         potential_orphans.remove(x)

# orphans = [int(x) for x in potential_orphans]

# for key in sorted(orphans):
#   print('%s' % (key))
#-----------------------------

# output = open(sys.argv[2], "w")

#TODO
#write results to output file. Foramt for each line: (line+"\n")

sc.stop()


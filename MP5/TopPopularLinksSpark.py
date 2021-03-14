#!/usr/bin/env python
import sys
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("TopPopularLinks")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf = conf)

lines = sc.textFile(sys.argv[1], 1) 

#TODO 
split_lines = lines.map(lambda x: x.split(":"))
fromPages = split_lines.map(lambda x: (x[0], 0))
toPages = split_lines.flatMap(lambda x: x[1].strip().split())
toPages = toPages.map(lambda x: (x, 1))
allPages =  fromPages.union(toPages)  
allPages = allPages.reduceByKey(lambda x, y: x+y)
# text = allPages.filter(lambda x: x[1] == 0).collect()
PopularPages = allPages.collect()


PopularPages = sorted(PopularPages, key= lambda x: x[1], reverse=True)
PopularPages = PopularPages[:10] 
PopularPages = sorted(PopularPages)
# PopularPages = sorted(PopularPages.items(), key = lambda x: x[1], reverse=True)



output = open(sys.argv[2], "w") #Write output to files 
for link in PopularPages:
  #  print('%s\t%s' % (link[0], link[1]))
  output.write(str(link[0]) + '\t' + str(link[1]) + '\n')

sc.stop()


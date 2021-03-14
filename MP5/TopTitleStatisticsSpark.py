#!/usr/bin/env python
import sys
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("TopPopularLinks")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf = conf)

lines = sc.textFile(sys.argv[1], 1) 

#TODO

output = open(sys.argv[2], "w")

#TODO
#write results to output file. Foramt for each line: (key + \t + value +"\n")

sc.stop()
#!/usr/bin/env python
import sys, math
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("TopTitleStatistics")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf = conf)

lines = sc.textFile(sys.argv[1],1).map(lambda line:( int(line.strip().split('\t')[1])))
# rdd = sc.parallelize(lines)
# sum = rdd.map(lambda x: x + x)
# print(sum)

#TODO  
sum = sc.accumulator(0)
def mysum(x):
    sum.add(x)
# min = sc.accumulator(1000000)
min = lines.min()
max = lines.max()
mean = int(lines.mean())
var = math.ceil(lines.variance())
# print("Min : ", min, "Max : ", max, "Mean :", mean, "Var :", var)

lines.foreach(mysum)

outputFile = open(sys.argv[2],"w")

#TODO write your output here'''
#write results to output file. Format
outputFile.write('Mean\t%s\n' % mean)
outputFile.write('Sum\t%s\n' % sum)
outputFile.write('Min\t%s\n' % min)
outputFile.write('Max\t%s\n' % max)
outputFile.write('Var\t%s\n' % var)

sc.stop()
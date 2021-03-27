#!/usr/bin/env python

#Execution Command: spark-submit PopularityLeagueSpark.py dataset/links/ dataset/league.txt
import sys
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("PopularityLeague")
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
pagesCollected = allPages.collect()


leagueIds = sc.textFile(sys.argv[2], 1)
#TODO
leagueText = leagueIds.flatMap(lambda x: x.split('\n'))
leagueText = leagueText.collect()

mydict = {}
rank = []
small = 0 

for key in pagesCollected:
    if key[0] in leagueText:
        # print(key[0], key[1])
        mydict[key] = key[1]

# for i in mydict:
#     print(i, "<<<")

popular = sorted(mydict.items(), key = lambda x: (x[0], x[1]), reverse=False)

keys, counts = zip(*popular) #unzip and keys and counts will contain all values 
counts = sorted(counts) 
# print(counts, "<<<<<<<<<")

r = 0
skip = 0
for i in range(len(counts)-1):
    if skip:
        skip -= 1
        continue
    if counts[i] < counts[i+1]:
        rank.append((r, counts[i]))
        r += 1
    else:
        for j in range(i,len(counts)-1):
            if counts[j] == counts[j+1]:
                rank.append((r, counts[j]))
                skip += 1
            else:
                # r += 1
                break
        r += skip 
        # skip = 0 
rank.append((r+1, counts[len(counts)-1])) # last element is len(array) -1  


output = open(sys.argv[3], "w")
# #TODO
for link in popular:
    for z in rank:  
        if z[1] == link[1]:
            # print('%s\t%s' % (link[0][0], z[0] )) #print as final output
            output.write(str(link[0][0]) + '\t' + str(z[0]) + '\n')
            break 



# output = open(sys.argv[3], "w")
    # output.write(str(link[0]) + '\t' + str(link[1]) + '\n')
#TODO

#write results to output file. Foramt for each line: (key + \t + value +"\n")

sc.stop()


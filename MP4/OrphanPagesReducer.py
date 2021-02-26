#!/usr/bin/env python3
import sys


#TODO
count = 0 
pages = {}

for line in sys.stdin:
  # TODO
  line = line.strip()
  parent, child = line.split('\t')
  if parent not in child: 
    count += 1 
  # child = child.strip().split(" ")  
  # print(line)


#TODO
# print(xx) print as final output



#  graph = defaultdict(list)
#     nodes = graph_dict["graph"].split(',')
#     for node in nodes:
#       source, dest = node.split('->')
#       graph[source].append(dest)
    


# 385744: 421957 3250680 3446893 5166549

#!/usr/bin/env python3
import sys
from collections import defaultdict #added this 

#TODO
count = 0 
pages = defaultdict(list)
id = {}
orphan = []
for line in sys.stdin:
  # TODO
  line = line.strip()
  parent, child = line.split('\t')
  # pages['parent'] = parent
  # pages['child'] = child
  pages[parent].append(child)

for parent, child in pages.items():
  pass
  
# print(pages)
# for page in pages:
  # print(type(page))
#TODO
# print(xx) print as final output



#  graph = defaultdict(list)
#     nodes = graph_dict["graph"].split(',')
#     for node in nodes:
#       source, dest = node.split('->')
#       graph[source].append(dest)
    


# 385744: 421957 3250680 3446893 5166549

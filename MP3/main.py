import json
from collections import deque
import re

input = '{"graph": "Chicago->Urbana,Urbana->Springfield,Chicago->Lafayette"}'

graph = re.split(r"['['  \"|\t|,|;|:|{|}|\->]", input)
while "" in graph:
    graph.remove("")
source = {}
destination = {}
count = 0
for index in graph:
    print(index)
    if count == 0:
        pass 
    if count % 1 == 0:
        source = index 
    if count % 2 == 0:
        destination = index
    count += 1

print(graph, source, destination)


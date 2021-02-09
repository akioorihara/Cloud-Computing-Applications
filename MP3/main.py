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
    if count == 0:
        count += 1
        continue
    if count % 2 != 0:
        source[count] = index
        print(source, "This is count != 0")
    else: 
        destination [count]= index
        print(destination, "This is dest")
    count += 1

print(graph)
print("This is source", source)
print("This is the Dist", destination)


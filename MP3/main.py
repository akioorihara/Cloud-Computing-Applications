import json
from collections import deque
import re

input = '{"graph": "Chicago->Urbana,Urbana->Springfield,Chicago->Lafayette"}'

graph = re.split(r"['['  \"|\t|,|;|:|{|}|\->]", input)
while "" in graph:
    graph.remove("")

print(graph)


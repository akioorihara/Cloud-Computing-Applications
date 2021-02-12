import json
from collections import deque, defaultdict
import re
from io import StringIO

def bfs(graph, vertex):
    queue = deque([vertex])
    level = {vertex: 0}
    parent = {vertex: None}
    while queue:
        v = queue.popleft()
        for n in graph[v]:
            if n not in level:            
                queue.append(n)
                level[n] = level[v] + 1
                parent[n] = v
    return level

input = '{"graph": "Chicago->Urbana,Urbana->Springfield,Chicago->Lafayette"}'
graph_dict = json.loads(input) 

graph = defaultdict(list)
nodes = graph_dict["graph"].split(',')
for node in nodes:
  source, dest = node.split('->')
  graph[source].append(dest)

print(bfs(graph,"Chicago"))
for key in graph.keys():
    node_dist = bfs(graph,key)
    #insert val to table 


# print()
# print(parser(input))
# print(bfs(parser(input),"Chicago"))      
# print(parser(input))


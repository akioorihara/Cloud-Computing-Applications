import json
from collections import deque, defaultdict


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
            
            if (level[n]): #print the positive dist 
                print(v) #itrating source 
                print(graph[v])

    return level



input = {"graph": "Chicago->Urbana,Urbana->Springfield,Chicago->Lafayette"}
json_dump = json.dumps(input)
graph_dict = json.loads(json_dump) 

graph = defaultdict(list)
nodes = graph_dict["graph"].split(',')
for node in nodes:
    source, dest = node.split('->')
    graph[source].append(dest)

(bfs(graph,"Chicago"))

for key in graph.keys():
    node_dist = bfs(graph,key)
    # print(node_dist)

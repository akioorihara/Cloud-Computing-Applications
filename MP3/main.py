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
    return level

input = '{"graph": "Chicago->Urbana,Urbana->Springfield,Chicago->Lafayette"}'
json_graph = {"graph": "Chicago->Urbana,Urbana->Springfield,Chicago->Lafayette"}
graph_dict_dump = json.dumps(json_graph)
print(type(graph_dict_dump))

graph_dict = json.loads(input) 
print(type(graph_dict))

graph = defaultdict(list)
nodes = graph_dict["graph"].split(',')
for node in nodes:
  source, dest = node.split('->')
  graph[source].append(dest)

(bfs(graph,"Chicago"))
for key in graph.keys():
    node_dist = bfs(graph,key)
    # print(node_dist)
    #insert val to table 


#   "errorMessage": "the JSON object must be str, bytes or bytearray, not dict",
#   "errorType": "TypeError",
#   "stackTrace": [
#     "  File \"/var/task/lambda_function.py\", line 24, in lambda_handler\n    graph_dict = json.loads(event)\n",
#     "  File \"/var/lang/lib/python3.8/json/__init__.py\", line 341, in loads\n    raise TypeError(f'the JSON object must be str, bytes or bytearray, '\n"
#   ]
# }

# print()
# print(parser(input))   
# print(parser(input))


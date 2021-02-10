import json
from collections import deque
import re

input = '{"graph": "Chicago->Urbana,Urbana->Springfield,Chicago->Lafayette"}'


def bfs(graph, vertex):
    queue = deque([vertex])
    level = {vertex: 0}
    parent = {vertex: None}
    while queue:
        v = queue.popleft()
        for n in graph[v]:
            queue.append(n)
            level[n] = level[v] + 1
            parent[n] = v
    return level, parent


def parser(input):
    graph = re.split(r"['[' |\"|\|,|;|:|{|}|\->]", input)
    while "" in graph:
        graph.remove("")
    source = []
    destination = []
    i = 0
    for index in graph:
        if i == 0:
            i += 1
            continue
        if i % 2 != 0:
            source.append(index)
            # print(source, "This is count != 2")
        else:
            destination.append(index)
            # print(destination, "This is dest")
        i += 1
    # graph.pop(0)
    return graph
print(parser(input))
print(bfs(parser(input),1))

# print(graph)
# print("This is source", source)
# print("This is the Dist", destination)

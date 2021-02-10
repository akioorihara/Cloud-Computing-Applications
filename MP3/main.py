import json
from collections import deque
import re

input = '{"graph": "Chicago->Urbana,Urbana->Springfield,Chicago->Lafayette"}'

test = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['B', 'D']
}

def bfs(graph, vertex):
    queue = deque([vertex])
    # print(queue)
    level = {vertex: 0}
    # print(level)
    parent = {vertex: None}
    # print(parent)
    while queue:
        v = queue.popleft()
        # print(v)
        for n in graph[v]:
            print(queue.append(n))
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
# print(parser(input))


def buildGraph(string):
    graph = {}
    for edge in string.split(','):
        source, destination = edge.split("->")
        source = source.strip(" ")
        destination = destination.strip(" ")
        if source not in graph:
            graph[source] = []
        if destination not in graph:
            graph[destination] = []
        graph[source].append(destination)
    return graph 

print(type(test))
print(buildGraph(input))


# print(bfs(test, 'A'))

# print(graph)
# print("This is source", source)
# print("This is the Dist", destination)

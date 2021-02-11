import json
from collections import deque
import re

input = '{"graph": "Chicago->Urbana,Urbana->Springfield,Chicago->Lafayette"}'

def parser(input):
    graph = {}
    s = re.split(r"['[' |\"|\|,|;|:|{|}|\->]", input)
    while "" in s:
        s.remove("")

    print(s)
    source = []
    destination = []
    i = 0
    for index in s:
        if i == 0:
            i += 1
            continue
        if i % 2 != 0:
            source.append(index)
            # graph[i] = source
            print(source, "-- This is source val")
        else:
            destination.append(index)
            # print(destination, "This is dest")
        i += 1
    
    for edge in s:
        if source not in s:
            graph[source]
        if destination not in s:
            graph[destination] 

    return graph
# print(parser(input))

# def bfs(graph, root):
    # print(graph)
    # visited, queue = set(), deque([root])
    # visited.add(root)
    # # print(visited)
    # while queue:
    #     vertex = queue.popleft()
    #     # print(vertex)
    #     print(str(vertex) + " ", end="")
    #     # If not visited, mark it as visited, and
    #     for neighbour in graph[vertex]:
    #         if neighbour not in visited:
    #             visited.add(neighbour)
    #             queue.append(neighbour)


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
    return level, parent

def parser(input):
    graph = {}
    for x in input.split(','):
        source, destination = x.split("->")
        if source not in graph:
            graph[source] = []
        if destination not in graph:
            graph[destination] = []
        # print(source, "-source ")
        # print(destination, "-dest")
        graph[source].append(destination)
    return graph 


# if __name__ == '__main__':
#     graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
#     print("Following is Breadth First Traversal: ")
#     bfs(graph, 0)

print(bfs(parser(input),"Springfield"))      
# print(parser(input))


import re

input = '{"graph": "Chicago->Urbana,Urbana->Springfield,Chicago->Lafayette"}'

graph = {}
s = re.split(r"['[' |\"|\|,|;|:|{|}|\->]", input)
while "" in s:
    s.remove("")

source = []
destination = []
i = 0
for index in s:
    if i == 0:
        i += 1
        continue
    if i % 2 != 0:
        source.append(index)
        graph[i] = source
        # print(source, "-- This is source val")
    else:
        destination.append(index)
        # print(destination, "This is dest")
    i += 1

# print(s)
# print(source)
# print(destination)

for index in range(len(source)):
    
    graph[index] = source[index]
    graph[index] = destination[index]
    
print(graph)

    # for x in input.split(','):
    #     source, destination = x.split("->")
    #     # print(graph)

    #     if source not in graph:
    #         graph[source] = []
    #     if destination not in graph:
    #         graph[destination] = []
    #     # print(source, "-source ")
    #     # print(destination, "-dest")
    #     graph[source].append(destination)
    # return graph 



# def parser(input):
#     graph = {}
    
#     for x in input.split(','):
#         source, dest = x.split("->")
        
#         if source not in graph:
#             graph[source] = []
#         if dest not in graph:
#             graph[dest] = []
#         graph[source].append(dest)
    
#     return graph 
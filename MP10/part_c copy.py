from pyspark import *
from pyspark.sql import SparkSession, Row
from graphframes import *
from graphframes.examples import Graphs

sc = SparkContext()
spark = SparkSession.builder.appName('fun').getOrCreate()


def get_shortest_distances(graphframe, dst_id):
    # TODO
    # Find shortest distances in the given graphframe to the vertex which has id `dst_id`
    # The result is a dictionary where key is a vertex id and the corresponding value is
    # the distance of this node to vertex `dst_id`.
    result = graphframe.shortestPaths(landmarks=[dst_id]).orderBy("id")
    #[Row(id='0', distances={'1': 1}), Row(id='1', distances={'1': 0}), Row(id='2', distances={'1': 1}), Row(id='3', distances={'1': 2}), Row(id='4', distances={}), Row(id='5', distances={})]

    mydict = {} 
    mydict = [ids['distances'] for ids in result.collect()] #[{'1': 1}, {'1': 0}, {'1': 1}, {'1': 2}, {}, {}]
    ids = {ids['id'] for ids in result.collect()}

    newdict = {} 
    count = 0 
    for row in result.collect():
        if row[1].values():
            for val in row[1].values(): 
                newdict[count] = val 
        else: 
            newdict[count] = -1
            
        count += 1

    # print(ids)
    # print(newdict, 'newdict')
    return newdict

if __name__ == "__main__":
    vertex_list = []
    edge_list = []
    with open('dataset/graph.data') as f:
        for line in f:
            # TODO: Parse line to get vertex id
            line_arr = line.split("\n")[0].split(" ")
            src = line[0]
            # TODO: Parse line to get ids of vertices that src is connected to
            if len(line_arr) >= 1:
                dst_list = line_arr[1:]
                #  print(dst_list)
            else:   
                dst_list = []  # TODO: Parse dst_list from line
            vertex_list.append((src,))
            edge_list += [(src, dst) for dst in dst_list]

    vertices = spark.createDataFrame(vertex_list).toDF("id")  # TODO: Create dataframe for vertices
    edges = spark.createDataFrame(edge_list).toDF("src", "dst")  # TODO: Create dataframe for edges

    g = GraphFrame(vertices, edges)
    # g.outDegrees.show()
    sc.setCheckpointDir("/tmp/shortest-paths")

    # We want the shortest distance from every vertex to vertex 1
    for k, v in get_shortest_distances(g, '1').items():
        print(k, v)

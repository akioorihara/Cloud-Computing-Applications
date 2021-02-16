import json
import boto3
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

def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    table = dynamodb.Table('MP3')

    # existing_tables = client.list_tables()['TableNames']
    # if 'MP3' in existing_tables:
    #     table.delete()
   
    # try:   
    #     response = client.create_table(
    #         AttributeDefinitions=[
    #             {
    #                 'AttributeName': 'Source',
    #                 'AttributeType': 'S',
    #             },
    
    #         ],
    #         KeySchema=[
    #             {
    #                 'AttributeName': 'Source',
    #                 'KeyType': 'HASH',
    #             },
    #         ],
    #         ProvisionedThroughput={
    #             'ReadCapacityUnits': 5,
    #             'WriteCapacityUnits': 5,
    #         },
    #         TableName='MP3',
    #     )
    # except:
    #     pass
    # table = dynamodb.Table('MP3')


    # input = '{"graph": "Chicago->Urbana,Urbana->Springfield,Chicago->Lafayette"}'
    json_dump = json.dumps(event)
    graph_dict = json.loads(json_dump) 
    
    graph = defaultdict(list)
    nodes = graph_dict["graph"].split(',')
    for node in nodes:
      source, dest = node.split('->')
      graph[source].append(dest)
    
    # ((bfs(graph,"Chicago")))
    # for key in graph.keys():
    #     node_dist = bfs(graph,key)
    #     print(node_dist)

    for source in list(graph):
        node_dist = bfs(graph,source)
        print(node_dist)
        for dest in node_dist:
            print(source, dest, node_dist[dest])
            table.put_item(
                Item={
                    'Source': source,
                    'Destination': dest,
                    'Distance': node_dist[dest]
                    
                }
            )

    try:
        
        return {
            'statusCode': 200,
            'body': json.dumps('Success!')
        }
    except: 
        print("Close lambad")
        return{
            'statusCode':400,
            'body':json.dumps('Error saving graph')
        }
        
        
        
    
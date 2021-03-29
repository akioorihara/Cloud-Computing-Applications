#not completed but the logis seems to make sense 
import json
import boto3
import pymysql
import os 
import redis
import sys 
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


#Redis Connection 
cache = redis.Redis.from_url('redis://mp6elasticachev2.wcjbfk.ng.0001.use2.cache.amazonaws.com:6379')
cache.ping()


#Aurora DB Connection 
endpoint = 'mp6auroradb.cluster-cxaqiqzybsep.us-east-2.rds.amazonaws.com'
username = 'admin'
password = 'Fivestar1'
database_name = 'MP6'
port = 3306 

TTL = 10

try: 
    conn = pymysql.connect(host=endpoint, user=username, passwd=password, db=database_name)
except: 
    logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
    sys.exit()


def fetch(sql):
    result = cache.get(sql)
    if result:
        return deserialize(result)
    else:
        result = db.query(sql)
        cache.setex(sql, ttl, serialize(result))
        return result


def lambda_handler(event, context):
    
    json_dump = json.dumps(event)
    mydict = json.loads(json_dump)
    return_rec = []

    with conn.cursor() as cur:
        if mydict["REQUEST"] == "read":
            for id in mydict['SQLS']:
                query = "select id, hero, power, name, xp, color from heros where id={}".format(id)
                if mydict['USE_CACHE'] == "True":
                    record = cache.get(id)
                    
                    if record == None:
                        record = cur.execute(query)
                        conn.commit()
                        cache.set(id, record, TTL)  #added TTL
                    
                    #Here is the print 

                else: 
                    record = cur.execute(query)
                    conn.commit()
                return_rec.append(record) 
                
                return{
                       'statusCode': 200,
                       'body': return_rec
                }
                
                #try to print here of what returns 
                
                    
        if mydict["REQUEST"] == "write":    
            for hero in mydict['SQLS']:
                
                findId = 'select last_insert_id()'
                cur.execute(findId)
                print(cur.execute(findId))
                
                query = 'insert into heros (hero, name, power, color, xp) VALUES (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')'.format(hero['hero'], hero['name'], hero['power'], hero['color'], hero['xp'])
                # query = 'insert into heros (id, hero, name, power, color, xp) VALUES (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')'.format(findId, hero['hero'], hero['name'], hero['power'], hero['color'], hero['xp'])
                if mydict['USE_CACHE'] == 'True':
                    # id = cur.execute('SELECT LAST_INSERT_ID()')
                    # id = cur.execute('SELECT MAX(id) from heros')
                    # result = cur.fetchall()
                    # print(id)
                    # print(result)
                    cur.execute(query)
                    conn.commit()
                    # record = cur.execute(query)
                    # id = cur.execute('SELECT LAST_INSERT_ID()')
                    # print(cur.rowcount, "This is rowcount") 
                    # conn.commit()
                    # print(cur.fetchone(), "This is fetchall ")
                    # hero['id'] = id 
                    # cache.set(id, json.dumps(hero), TTL)
                
                    #{
                    #   "USE_CACHE": "True",
                    #   "REQUEST": "write",
                    #   "SQLS": [
                    #     {
                    #       "hero": "yes",
                    #       "name": "fireman",
                    #       "power": "fire",
                    #       "color": "red",
                    #       "xp": "10"
                    #     },
                    #     {
                    #       "hero": "no",
                    #       "name": "dogman",
                    #       "power": "bark",
                    #       "color": "brown",
                    #       "xp": "50"
                    #     }
                    #   ]
                    # }
                                    
# r = redis.Redis()
# r.flushall()
    
    try:    
        return {
            'statusCode': 200,
            # 'headers': {
            #     'Access-Control-Allow-Origin': '*',
            #     'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            #     'Access-Control-Allow-Credentials': 'true',
            #     'Content-Type': 'application/json'
    
            'body': json.dumps('Success!')
        }
    except: 
        print("Close lambad")
        return{
            'statusCode':400,
            'body':json.dumps('Error saving graph')
        }

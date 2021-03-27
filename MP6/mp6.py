#This is from AWS lambda 

import os
import json
import redis
import pymysql

class DB:
    def __init__(self, **params):
        params.setdefault("charset", "utf8mb4")
        params.setdefault("cursorclass", pymysql.cursors.DictCursor)
        self.mysql = pymysql.connect(**params)
    def query(self, sql):
        with self.mysql.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
    def record(self, sql, values):
        with self.mysql.cursor() as cursor:
            cursor.execute(sql, values)
            return cursor.fetchone()
    def save(self, sql):
        with self.mysql.cursor() as cursor:
            cursor.execute(sql)
            return self.mysql.commit()

TTL = 10  # Time to live for cached data

REDIS_URL='redis://mp6elasticachev2.wcjbfk.ng.0001.use2.cache.amazonaws.com:6379'
DB_HOST='mp6auroradb.cluster-cxaqiqzybsep.us-east-2.rds.amazonaws.com'
DB_USER='admin'
DB_PASS='Fivestar1'
DB_NAME='MP6'

Database = DB(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DB_NAME)
Cache = redis.Redis.from_url(REDIS_URL)   # Initialize the cache

def search_by_id(id, usecache):
    key = f"heroes:{id}"
    res = Cache.hgetall(key)
    if (res != {}) & (usecache):
        return res
    else:
        sql = "SELECT id, hero, power, name, xp, color FROM heros WHERE id=%s"
        res = Database.record(sql, (id,))
        if res:
            if usecache:
                Cache.hmset(key, res)
                Cache.expire(key, TTL)
            return res

def write_values(value, id, usecache):
    h = value["hero"]
    n = value["name"]
    p = value["power"]
    c = value["color"]
    x = int(value["xp"])
    sql = f"INSERT INTO heros (id,hero,name,power,color,xp) VALUES ({id},'{h}','{n}','{p}','{c}',{x})"
    Database.save(sql)
    if usecache:
        key = f"heroes:{id}"
        res2 = {}
        res2['id'] = id
        res2.update(value)
        Cache.hmset(key, res2)
        Cache.expire(key, TTL)
    
def lambda_handler(event, context):
    print('starting to handle')
    USE_CACHE = event["USE_CACHE"]
    usecache = (USE_CACHE == "True")
    REQUEST = event["REQUEST"]
    SQLS = event["SQLS"]
    result = []
    if REQUEST == "read":
        
        for id in SQLS:
            result.append(search_by_id(id, usecache))
        return {
            "statusCode": 200,
            "body": result
        }
    elif REQUEST == "write":
        
        count = Database.query("SELECT MAX(id) AS Max_Id FROM heros")[0]["Max_Id"]
        for value in SQLS:
            count += 1
            write_values(value, count, usecache)
        return {
            "statusCode": 200,
            "body": "write success"
        }
    else:
        return {
            "statusCode": 400,
            "body": "error"
        }
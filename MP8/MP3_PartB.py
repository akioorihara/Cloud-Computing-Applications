from pyspark import SparkContext, SQLContext
from pyspark import Row
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType, IntegerType

sc = SparkContext()
sqlContext = SQLContext(sc)

####
# 1. Setup (10 points): Download the gbook file and write a function to load it in an RDD & DataFrame
####

# RDD API
# Columns:
# 0: place (string), 1: count1 (int), 2: count2 (int), 3: count3 (int)

textFile = sc.textFile('gbooks')
lines = textFile.map(lambda x: x.split('\t'))
lines = lines.map(lambda x: (x[0], int(x[1]), int(x[2]), int(x[3]) ))

schema = StructType([
    StructField('word', StringType(), True),
    StructField('count1', IntegerType(), True),
    StructField('count2', IntegerType(), True),
    StructField('count3', IntegerType(), True)
    ])
df = sqlContext.createDataFrame(lines, schema) 

df.createOrReplaceTempView('dframe')
sqlContext.sql("SELECT count(*) from dframe").show()
# result.count().show()

# df.show()

# Spark SQL - DataFrame API

####
# 2. Counting (10 points): How many lines does the file contains? Answer this question via both RDD api & #Spark SQL
####

# Spark SQL 


# +--------+                                                                              
# |count(1)|
# +--------+
# |86618505|
# +--------+



from pyspark import SparkContext, SQLContext
from pyspark import Row
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType, IntegerType
from pyspark.sql.types import *

sc = SparkContext()
sqlContext = SQLContext(sc)

####
# 1. Setup (10 points): Download the gbook file and write a function to load it in an RDD & DataFrame
####

textFile = sc.textFile('gbooks')
split_lines = textFile.map(lambda x: x.split('\t'))
# line = split_lines.map(lambda x: Row(word=x[0], count1=int(x[1]),count2=int(x[2]), count3=int(x[3])))
schema = StructType([
    StructField('word', StringType(), True),
    StructField('count1', IntegerType(), True),
    StructField('count2', IntegerType(), True),
    StructField('count3', IntegerType(), True)
    ])
df = sqlContext.createDataFrame(split_lines, schema) 
df.printSchema()
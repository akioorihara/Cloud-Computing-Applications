from pyspark import SparkContext, SQLContext
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


# Spark SQL - DataFrame API

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
sqlContext.sql("SELECT word, count(*) FROM dframe group by word Order by count(word) desc").show(3)


####
# 4. MapReduce (10 points): List the three most frequent 'word' with their count of appearances
####

# Spark SQL

# There are 18 items with count = 425, so could be different 
# +---------+--------+
# |     word|count(1)|
# +---------+--------+
# |  all_DET|     425|
# | are_VERB|     425|
# |about_ADP|     425|
# +---------+--------+


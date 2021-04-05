from pyspark import SparkContext, SQLContext
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType, IntegerType

sc = SparkContext()
sqlContext = SQLContext(sc)

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

# Spark SQL - DataFrame API
####
# 5. Joining (10 points): The following program construct a new dataframe out of 'df' with a much smaller size.
####
sqlContext.setConf("spark.sql.broadcastTimeout",1800)
df2 = df.select("word", "count1").distinct().limit(100)
df2.createOrReplaceTempView('gbooks2')  # Register table name for SQL

# Now we are going to perform a JOIN operation on 'df2'. Do a self-join on 'df2' in lines with the same #'count1' values and see how many lines this JOIN could produce. Answer this question via DataFrame API and #Spark SQL API
# Spark SQL API

# output: 210
x = sqlContext.sql("SELECT * FROM gbooks2 g1 JOIN gbooks2 g2 ON g1.count1 = g2.count1")
print(x.count())
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.ml.clustering import KMeans
from pyspark.ml.linalg import Vectors
import pyspark.sql.functions as F
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType
from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler
############################################
#### PLEASE USE THE GIVEN PARAMETERS     ###
#### FOR TRAINING YOUR KMEANS CLUSTERING ###
#### MODEL                               ###
############################################

NUM_CLUSTERS = 4
SEED = 0
MAX_ITERATIONS = 100
INITIALIZATION_MODE = "random"

sc = SparkContext()
sqlContext = SQLContext(sc)


def get_clusters(df, num_clusters, max_iterations, initialization_mode,
                 seed):
    # TODO:
    # Use the given data and the cluster pparameters to train a K-Means model
    # Find the cluster id corresponding to data point (a car)
    # Return a list of lists of the titles which belong to the same cluster
    # For example, if the output is [["Mercedes", "Audi"], ["Honda", "Hyundai"]]
    # Then "Mercedes" and "Audi" should have the same cluster id, and "Honda" and
    # "Hyundai" should have the same cluster id
    F_Col = ['1', '2', '3', '4', '5','7', '8', '9', '10', '11']
    vecAssembler = VectorAssembler(inputCols=F_Col, outputCol="features")
    new_df = vecAssembler.transform(df)

    kmeans = KMeans(k = num_clusters, seed = seed, maxIter = max_iterations, initMode = initialization_mode)
    model = kmeans.fit(new_df.select('features'))
    transformed = model.transform(new_df)

    output = []
    rdd1 = transformed.rdd.map(tuple)
    rdd2 = rdd1.map(lambda x : (x[13], x[0])).reduceByKey(lambda  a, b : (a+','+b)).collect()

    # print(rdd2)
    for i, j in rdd2:       
        output.append(j.split(","))
    return output 


def parse_line(line):
    # TODO: Parse data from line into an RDD
    # Hint: Look at the data format and columns required by the KMeans fit and
    # transform functions
    
    return line.split(",")


if __name__ == "__main__":
    f = sc.textFile("dataset/cars.data")

    rdd = f.map(parse_line)

    # TODO: Convert RDD into a dataframe
    schema = StructType([StructField(str(i), StringType(), True) for i in range(12)])
    df = sqlContext.createDataFrame(rdd, schema)
    # df.show()
    F_Col = ['1', '2', '3', '4', '5','7', '8', '9', '10', '11']
    # print(type(df))
    for col in df.columns:
        if col in F_Col:
            df = df.withColumn(col, df[col].cast('float'))
            # df.show()

    clusters = get_clusters(df, NUM_CLUSTERS, MAX_ITERATIONS,
                            INITIALIZATION_MODE, SEED)

    # print("C starts")    
    # print(clusters)
    # print("C ends")

    for cluster in clusters:
        # print(cluster)
        print(','.join(cluster))
        # pass
from pyspark.ml.classification import RandomForestClassifier
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorIndexer
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.regression import RandomForestRegressor
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType
from pyspark.sql.types import IntegerType

sc = SparkContext()
sqlContext = SQLContext(sc)

def predict(df_train, df_test):
    # TODO: Train random forest classifier

    # Hint: Column names in the given dataframes need to match the column names
    # expected by the random forest classifier `train` and `transform` functions.
    # Or you can alternatively specify which columns the `train` and `transform`
    # functions should use

    # Result: Result should be a list with the trained model's predictions
    # for all the test data points
    fcols = ['0','1','2','3','4','5','6','7']
    lcols = ['8']
    assembler = VectorAssembler(inputCols=fcols, outputCol="features")
    new_df = assembler.transform(df_train)
    new_df.show()
    model = assembler.fit(df_train)


    # kmeans = KMeans(k = num_clusters, seed = seed, maxIter = max_iterations, initMode = initialization_mode)
    # model = kmeans.fit(new_df.select('features'))
    # transformed = model.transform(new_df)

     
    return []


def main():
    raw_training_data = sc.textFile("dataset/training.data")

    # TODO: Convert text file into an RDD which can be converted to a DataFrame
    # Hint: For types and format look at what the format required by the
    # `train` method for the random forest classifier
    # Hint 2: Look at the imports above
    rdd_train = raw_training_data.map(lambda x : x.split(','))
    # print('train', rdd_train.collect())

    # TODO: Create dataframe from the RDD
    schema = StructType([StructField(str(i), StringType(), True) for i in range(9)])
    df_train = sqlContext.createDataFrame(rdd_train, schema)
    cols = ['5','6']
    for col in df_train.columns:
        if col in cols:
            df_train = df_train.withColumn(col, df_train[col].cast('float'))
        else:   
            df_train = df_train.withColumn(col, df_train[col].cast('integer'))
    # df_train = rdd_train.toDF()
    # df_train.show()
    # df_train.printSchema()

    raw_test_data = sc.textFile("dataset/test-features.data")

    # TODO: Convert text file lines into an RDD we can use later
    rdd_test = raw_test_data.map(lambda x : x.split(','))
    # print(rdd_test.collect())

    # TODO:Create dataframe from RDD
    # df_test = rdd_test.toDF()
    schemaV2 = StructType([StructField(str(i), StringType(), True) for i in range(8)])
    df_test = sqlContext.createDataFrame(rdd_test, schemaV2)
    cols = ['5','6']
    for col in df_test.columns:
        if col in cols:
            df_test = df_test.withColumn(col, df_test[col].cast('float'))
        else:   
            df_test = df_test.withColumn(col, df_test[col].cast('integer'))
    # df_test.show()
    # df_test.printSchema()

    predictions = predict(df_train, df_test)

    # You can take a look at dataset/test-labels.data to see if your
    # predictions were right

    for pred in predictions:
        print(int(pred))


if __name__ == "__main__":
    main()

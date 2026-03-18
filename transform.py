from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Demo").getOrCreate()

data = [("Alice", 25), ("Bob", 30)]
columns = ["name", "age"]

df = spark.createDataFrame(data, columns)

df.show()
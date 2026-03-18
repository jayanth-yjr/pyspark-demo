from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("Demo").getOrCreate()

data = [("Alice", 25), ("Bob", 30)]
columns = ["name", "age"]

df = spark.createDataFrame(data, columns)

df.show()

df_filtered = df.filter(col("age") > 26)

df_filtered.show()
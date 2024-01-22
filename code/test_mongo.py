from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

spark = SparkSession.builder.appName("MongoDBIntegration").config("spark.mongodb.input.uri", "mongodb://mongo/grandes_volumenes.test").config("spark.mongodb.input.uri", "mongodb://mongo/grandes_volumenes.test").config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:10.2.1").getOrCreate()

df = spark.createDataFrame(
    [
    ("Bilbo Baggins", 50),
    ("Gandalf", 1000),
    ("Thorin", 195),
    ("Balin", 178),
    ("Kili", 77),
    ("Dwalin", 169),
    ("Oin", 167),
    ("Gloin", 158),
    ("Fili", 82),
    ("Bombur", None)
    ],
    ["name", "age"]
)

df.select(avg("age")).show()

df.write.format("mongodb").mode("append").option("connection.uri", "mongodb://mongo:27017").option("database", "grandes_volumenes").option("collection", "spark").save()
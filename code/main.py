from pyspark.sql import SparkSession
from pyspark.sql.functions import avg
import os

DATASET_PATH = "." + os.sep + "dataset" + os.sep

spark = SparkSession.builder.appName("Spark&Mongo") \
    .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:10.2.1") \
    .getOrCreate()


for file in os.listdir(DATASET_PATH):
    # Importamos el csv
    df = spark.read.csv(DATASET_PATH + file, header='true')
    
    # Quitamos los valores nulos
    nulls = df.na.drop()

    # Mostramos el dataset
    df.select("*").show()
    #df.select(avg("weight")).show()

    # Obtenemos el nombre del fichero
    filename = file.split(".")[0]

    # Guardamos en MongoDB los datos procesados
    df.write.format("mongodb").mode("append").option("connection.uri", "mongodb://root:example@mongo:27017/").option("database", "nfl").option("collection", filename).save()




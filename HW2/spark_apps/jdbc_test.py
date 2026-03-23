import time
from pyspark.sql import SparkSession

time.sleep(30)

print("Spark session started successfully")

spark = SparkSession.builder \
    .appName("PostgreSQL Connection Test") \
    .config("spark.driver.memory", "2g")\
    .config("spark.executor.memory", "2g")\
    .config("spark.ui.enabled", "false")\
    .getOrCreate()

df = spark.read.csv(
    "/opt/spark/apps/data/",
    header=True,
    inferSchema=True
)
df.show(5)
df.printSchema()
df.show(5)

print("Read csv")

print("Trying to read table:", "mock_data")
spark = (SparkSession.builder.appName("etl_to_marts").getOrCreate())

PG_URL = "jdbc:postgresql://postgres:5432/my_db"
PG_PROPS = {
    "user": "my_user",
    "password": "12345",
    "driver": "org.postgresql.Driver"
}

CH_URL = "jdbc:clickhouse://clickhouse:8123/default"
CH_PROPS = {
    "user": "click",
    "password": "click",
    "driver": "com.clickhouse.jdbc.ClickHouseDriver"
}
PG_URL = "jdbc:postgresql://postgres:5432/my_db"
PG_PROPS = {
    "user": "my_user",
    "password": "12345",
    "driver": "org.postgresql.Driver"
}
print("PG connection OK")
mock1 = spark.read.jdbc(PG_URL, "mock_data1", properties=PG_PROPS)

mock1.show(3)

mock1.write.jdbc(PG_URL, "mock_data2" , "append", properties=PG_PROPS)

print("Pg-write ok")

mock1.write.jdbc(CH_URL, "mock_datach2", "append", properties=CH_PROPS)

print("ClickHouse-write ok")

spark.stop()
print("Spark session stopped")
from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .appName("WaterLakehouseParquet") \
    .getOrCreate()

df = spark.read.csv(
    "/mnt/c/Water_Monitoring_System/data/brisbane_water_quality.csv",
    header=True,
    inferSchema=True
)

print("Original Data:")
df.show(20)

df.write.mode("overwrite").parquet("/tmp/water_lake_v0")
print("Version 0 saved")


df_v1 = df.filter(df["Temperature"] > 25)

df_v1.write.mode("overwrite").parquet("/tmp/water_lake_v1")
print("Version 1 saved")


print("Reading Version 0:")
v0 = spark.read.parquet("/tmp/water_lake_v0")
v0.show(20)


print("Reading Version 1:")
v1 = spark.read.parquet("/tmp/water_lake_v1")
v1.show(20)

print("Average Temperature:")
df.groupBy().avg("Temperature").show()
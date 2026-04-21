from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Spark session
spark = SparkSession.builder.appName("WaterPipeline").getOrCreate()

# =========================
# INGESTION
# =========================
df = spark.read.csv(
    "/mnt/c/Water_Monitoring_System/data/brisbane_water_quality.csv",
    header=True,
    inferSchema=True
)

# =========================
# PROCESSING
# =========================
df_processed = df.select(
    "Timestamp",
    "pH",
    "Dissolved Oxygen",
    "Turbidity"
)

# Simple cleaning
df_clean = df_processed.filter(
    (col("pH") >= 0) & (col("pH") <= 14)
)

# =========================
# STORAGE
# =========================
df_clean.write.mode("overwrite").csv(
    "final_water_data",
    header=True
)

print("Pipeline Completed")
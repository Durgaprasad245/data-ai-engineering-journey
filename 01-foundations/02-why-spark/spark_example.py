from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum

# Start Spark
spark = (
    SparkSession.builder
    .appName("WhySparkExists")
    .getOrCreate()
)

# Sample customer transactions
data = [
    ("Alice", 100),
    ("Bob", 200),
    ("Alice", 150),
    ("Bob", 50),
    ("Charlie", 300)
]

columns = ["customer", "amount"]

# Create a Spark DataFrame
df = spark.createDataFrame(data, columns)

print("Original Data:")
df.show()

# Calculate total spending for each customer
customer_totals = (
    df.groupBy("customer")
      .agg(sum("amount").alias("total_amount"))
      .orderBy(col("total_amount").desc())
)

print("Customer Totals:")
customer_totals.show()

# Show number of partitions
print("Number of partitions:", df.rdd.getNumPartitions())

spark.stop()

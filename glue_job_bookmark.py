import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, TimestampType


# Initialize Glue context and job
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Define the source and target paths
source_path = "s3://edp-source/source_files/"
target_path = "s3://edp-target/target/orders/"

# Define the schema
schema = StructType([
    StructField("order_id", IntegerType(), True),
    StructField("order_date", TimestampType(), True),
    StructField("order_customer_id", IntegerType(), True),
    StructField("order_status", StringType(), True)
])

# Read the data from the source path
source_GDF = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [source_path]},
    format="csv",
    format_options={"withHeader": True},
    transformation_ctx="source_GDF",
    schema=schema
)

# # Convert DynamicFrame to DataFrame
# df = source_GDF.toDF()

# # Apply the schema to the DataFrame
# df = spark.createDataFrame(df.rdd, schema)

# # Convert DataFrame back to DynamicFrame
# dynamic_frame = DynamicFrame.fromDF(df, glueContext, "dynamic_frame")

# Write the data to the target path in Parquet format
datasink = glueContext.write_dynamic_frame.from_options(
    frame=source_GDF,           #dynamic_frame,
    connection_type="s3",
    connection_options={"path": target_path},
    format="parquet"
)

# Commit the job
job.commit()

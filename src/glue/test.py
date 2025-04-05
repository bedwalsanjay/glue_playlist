from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Initialize Glue context and Spark context
sc = SparkContext.getOrCreate() #get or create, important for jupyter.
glueContext = GlueContext(sc)
spark = glueContext.spark_session
df=spark.read.csv("s3://edp-source/source_files/part-00000_orders_1.csv")
df.show()

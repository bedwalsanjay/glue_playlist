import pandas as pd
from datetime import datetime
# Get the current date and time
now = datetime.now()
# Format the date and time as yyyymmddhhmmss and convert it to an integer
formatted_date_time = int(now.strftime("%Y%m%d%H%M%S"))

target_file_name="s3://youtube-demo-15082023/target/orders/"+str(formatted_date_time)+'.parquet'
print(target_file_name)

df = pd.read_csv("s3://youtube-demo-15082023/original_files/part-00000_orders_1.csv")
print(df)
#droping duplicate columns
df.drop_duplicates(inplace = True) 
#writing dataframe into parquet format
df = df.reset_index(drop=True)
df.to_parquet(target_file_name)

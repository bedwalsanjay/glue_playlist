# glue_playlist
This repository contains the code which I am going to use in my youtube playlist

## Run AWS Glue code from local docker container in Windows machine
Read this article for your reference :
https://aws.amazon.com/blogs/big-data/develop-and-test-aws-glue-version-3-0-jobs-locally-using-a-docker-container/

### Download the aws glue image
`docker pull amazon/aws-glue-libs:glue_libs_4.0.0_image_01`

### Run the container

replace C:\Users\Sanjay Bedwal\Desktop\repos\youtube\glue_playlist with your local path . 

```
docker run -it ^
  -v "%USERPROFILE%\.aws:/home/glue_user/.aws" ^`
  -v "C:\Users\Sanjay Bedwal\Desktop\repos\youtube\glue_playlist:/home/glue_user/workspace" ^
  -e AWS_PROFILE=default ^
  -e DISABLE_SSL=true ^
  --rm ^
  -p 4040:4040 ^
  -p 18080:18080 ^
  -p 8888:8888 ^
  --name glue_pyspark ^
  amazon/aws-glue-libs:glue_libs_4.0.0_image_01
```

OR if you dont want to bind your local folder in your docker container and then you can run below command 

`docker run -it -v "%USERPROFILE%\.aws:/home/glue_user/.aws" -e AWS_PROFILE=default -e DISABLE_SSL=true --rm -p 4040:4040 -p 18080:18080 -p 8888:8888 --name glue_pyspark amazon/aws-glue-libs:glue_libs_4.0.0_image_01`

#### Explanation of Each Option

| Option                      | Description                                                                                                                                                                                                                   |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker run`                | Starts a new Docker container.                                                                                                                                                                                               |
| `-it`                        | Runs the container in interactive mode (`-i`) with a terminal (`-t`).                                                                                                                                                         |
| `-v "%USERPROFILE%\.aws:/home/glue_user/.aws"` | Mounts your local AWS credentials (`.aws` folder) into the container so it can access AWS services. Replace `%USERPROFILE%` with `$HOME` on linux/mac.                                                                                                            |
| `-e AWS_PROFILE=default`    | Sets an environment variable inside the container to use the default AWS profile.                                                                                                                                            |
| `-e DISABLE_SSL=true`       | Disables SSL verification (useful in certain corporate networks or debugging scenarios). **Use with caution in production.** |
| `--rm`                      | Automatically removes the container when it stops (prevents clutter).                                                                                                                                                        |
| `-p 4040:4040`              | Maps Spark UI (port 4040) from the container to your host machine. This allows you to view the Spark UI in your browser at http://localhost:4040                                                                        |
| `-p 18080:18080`            | Maps Spark History Server (port 18080) for monitoring past jobs. This allows you to view the Spark History Server in your browser at http://localhost:18080                                                             |
| `-p 8888:8888`              | Maps Jupyter Notebook (port 8888) for coding in a browser. This allows you to access Jupyter Notebook in your browser at http://localhost:8888                                                                            |
| `--name glue_pyspark`       | Names the container `glue_pyspark` for easier reference. This allows you to refer to the container by name instead of its ID.                                                                                                |
| `amazon/aws-glue-libs:glue_libs_4.0.0_image_01` | Specifies the Docker image to use (AWS Glue 4.0 libraries). This image provides the necessary libraries and dependencies for running AWS Glue PySpark jobs locally. Replace `4.0.0_image_01` with your desired glue version. |


#### What Happens When You Run This Command?
1. A new Docker container starts using the AWS Glue 4.0 image.
2. The container gets access to your local AWS credentials (~/.aws/ folder).
3. Spark UI (4040), Spark History Server (18080), and Jupyter Notebook (8888) are exposed to your machine.
4. SSL is disabled for AWS connections inside the container.
5. When you stop the container, it gets automatically deleted (--rm flag).


### Inside the container, manually start a shell

`sh`

### Once Inside the Container, Start Jupyter

`jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root --NotebookApp.token=''`

You will see a screen like below 

![image](https://github.com/user-attachments/assets/4c565212-1917-43ae-b00b-944527b986d3)

### Run jupyter notebook
Then open http://localhost:8888/ in your browser

### How to Stop the Container?
Since --rm removes the container after stopping, just press:

`Ctrl + C`
or in a new terminal:
`docker stop glue_pyspark`


### Run some sample code to test everything

Create a file in Jupyter Notebook and run below sample code

```import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Initialize Glue context and Spark context
sc = SparkContext.getOrCreate() #get or create, important for jupyter.
glueContext = GlueContext(sc)
spark = glueContext.spark_session
df=spark.read.csv("<**sample file from your s3 account**>")
df = spark.read.csv(" <sample file from your s3 account >", header=True)
df.show()


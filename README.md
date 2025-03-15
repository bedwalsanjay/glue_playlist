# glue_playlist
This repository contains the code which I am going to use in my youtube playlist

## Run AWS Glue code from local docker container 
Read this article for your reference :
https://aws.amazon.com/blogs/big-data/develop-and-test-aws-glue-version-3-0-jobs-locally-using-a-docker-container/

### Download the aws glue image
`docker pull amazon/aws-glue-libs:glue_libs_3.0.0_image_01`

### Run the container
`docker run -it -v "%USERPROFILE%\.aws:/home/glue_user/.aws" -e AWS_PROFILE=default -e DISABLE_SSL=true --rm -p 4040:4040 -p 18080:18080 -p 8888:8888 --name glue_pyspark amazon/aws-glue-libs:glue_libs_3.0.0_image_01`

### Inside the container, manually start a shell

`sh`

### Once Inside the Container, Start Jupyter

`jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root --NotebookApp.token=''`

### Run jupyter notebook
Then open http://localhost:8888/ in your browser


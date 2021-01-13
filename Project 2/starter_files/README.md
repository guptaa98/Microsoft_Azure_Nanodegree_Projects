# Operationalizing Machine Learning
This project is part of the Udacity Azure ML Nanodegree. In this project, I've worked with the Bank Marketing dataset which contains 21 features and we had to predict whether a person will take a loan or not. The was our target column y. 
Microsft Azure was used to configure a cloud-based machine learning production model, deploy it, and consume it. We will also create, publish, and consume a pipeline using Azure Python SDK.
The dataset can be downloaded from here
https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv

## Architectural Diagram
![blk diagram](https://user-images.githubusercontent.com/46073909/104422247-820ec100-55a2-11eb-84d6-830246ab2612.png)

## Key Steps
### Step 1: Authenication

Used the lab provided by udacity so this step was skipped.

### Step 2: Create and run Auto ML Experiment
1. Uploaded the bank marketing dataset to Azure.
2. A new Compute Cluster was made with Standard_DS12_v2 as the vm and 1 as the minimum number of nodes. Max number of nodes were 5.
3. Used the above dataset to create an automl run experiment using classification with target column as 'y'.The Exit Criteria was 1 hour and concurrency was set to 5. 

**Screenshots**

Registered Dataset showing that the dataset is available
![registered dataset](https://user-images.githubusercontent.com/46073909/104363813-bd29d980-553b-11eb-8516-5ebdcdf1003c.jpg)

Experiment is completed
![run completed](https://user-images.githubusercontent.com/46073909/104363821-bf8c3380-553b-11eb-9542-2196a7b40bad.jpg)

Best model details
![best model run](https://user-images.githubusercontent.com/46073909/104363826-c024ca00-553b-11eb-9510-cf1fe99e36fe.jpg)

### Step 3: Create and run Auto ML Experiment

After the experiment run completes, a summary of all the models and their metrics are shown, including explanations. 
1. The Best Model was Voting Ensemble Model and hence selected for deployment. Deploying the Best Model will allow to interact with the HTTP API service and interact with the model by sending data over POST requests.
2. The *Authentication* was enabled and the model was deployed using *Azure Container Instances*

### Step 4: Enable Application Insights

Now that the Best Model is deployed, in this step we will enable Application Insights and retrieve logs. Although this was configurable at deploy time with a check-box, but we used logs.py for this purpose.
1. Download the config.json file and stored it into the same directory of logs.py.
2. Replaced the default model name in the script with our deployed model name and then ran *python logs.py* in git-bash. 
3. We are going to see some results in the terminal and when we go back to our Azure studio we'll see that the application insights were enabled (True). 
   Application Insight URL was available which gave all the information regarding Server Requests, Server Response Time, Failed Requests and availability.
   
**Screenshots**

logs.py running
![logs py result 1](https://user-images.githubusercontent.com/46073909/104364490-ae8ff200-553c-11eb-8402-5ac28fc2ecba.jpg)
![logs py result 2](https://user-images.githubusercontent.com/46073909/104364495-b059b580-553c-11eb-8c3f-64759895283a.jpg)

Application Insights Enabled
![app insight enabled](https://user-images.githubusercontent.com/46073909/104364497-b0f24c00-553c-11eb-9cf0-458c088e5327.jpg)

### Step 5: Swagger Documentation

In this step, we will consume the deployed model using Swagger.
1. Downloaded the swagger.json file fro swagger URI. *Remember to keep this file in the same directory as of swagger.sh and serve.py files.*
2. swagger.sh will download the latest Swagger container, and it will run it on port 80 by default. Since permission for port 80 on your computer wasn't granted, updated the port to 9000.
3. Used gitbash to run the Serve.py and Swagger.sh files.
4. Observed the contents of the API for the model using HTTP API responses and methods.

**Screenshots**

Screenshot showing swagger runs on locahost showing HTTP API methods and responses for the model
![swagger response](https://user-images.githubusercontent.com/46073909/104364697-fca4f580-553c-11eb-90dc-87bd9f207e47.jpg)
![swagger response 2](https://user-images.githubusercontent.com/46073909/104364691-fadb3200-553c-11eb-9067-1267244a1a90.jpg)
![swagger ui](https://user-images.githubusercontent.com/46073909/104364699-fd3d8c00-553c-11eb-96c4-16bb1421f821.jpg)
![localhost9000](https://user-images.githubusercontent.com/46073909/104364703-fdd62280-553c-11eb-83e2-2e64ec32db87.jpg)
![locl2](https://user-images.githubusercontent.com/46073909/104364705-fe6eb900-553c-11eb-9b8d-aaf2e14e38bd.jpg)

### Step 6: Consume Model Endpoints

Since the model is deployed, we'll use the endpoint.py script provided to interact with the trained model.
1. Updated the scoring_uri with REST endpoint URL and key with primary key of the deployed model.
2. Executed *python endpoint.py* and the results were similar to {results : ["yes","no"]}.
3. data.json file was also downloaded

**Screenshots**

endpoint.py runs 
![endpoint resp](https://user-images.githubusercontent.com/46073909/104365081-8d7bd100-553d-11eb-9d4b-8aad09968a7d.jpg)

data.json file is produced as an output from the model
![data json file](https://user-images.githubusercontent.com/46073909/104365087-8eacfe00-553d-11eb-82ef-fd1dc963238d.jpg)

### Step 7: Create, Publish and Consume a Pipeline

1. Uploaded the provided notebook to azure.
2. All the variables were updated to match our environment.
3. config.json file was downloaded and was available in the current working directory.
4. Pipeline was created and scheduled to run. 

**Screenshots**

Pipeline section of azure studio showing that the pipeline was created
![pipeline is created](https://user-images.githubusercontent.com/46073909/104365302-d895e400-553d-11eb-9dc4-8075d0509b57.jpg)

Pipeline section showing pipeline endpoint
![pipeline endpoint section](https://user-images.githubusercontent.com/46073909/104365312-da5fa780-553d-11eb-8ad7-145c362a0b6a.jpg)

Bankmarketing dataset with automl module
![data with automl module](https://user-images.githubusercontent.com/46073909/104365311-d9c71100-553d-11eb-8d4c-0ddf8a6aff30.jpg)

Published pipeline overview showing REST endpoint and status as active
![pipeline endpt published pipeline overview](https://user-images.githubusercontent.com/46073909/104365295-d6338a00-553d-11eb-85ff-c83fe8ad87d9.jpg)

ML studio showing scheduled run
![scheduled runs](https://user-images.githubusercontent.com/46073909/104365308-d9c71100-553d-11eb-9c26-b6a38c24f109.png)
![scheduled run completed](https://user-images.githubusercontent.com/46073909/104365304-d92e7a80-553d-11eb-91dc-58bbbad01d28.png)

Use RunDetailsWidget showing step runs
![run details](https://user-images.githubusercontent.com/46073909/104365998-bfd9fe00-553e-11eb-9361-06d8fa544c71.png)

## Screen Recording
The screencast of my project can be found here.
https://drive.google.com/file/d/1c6d4M0sbfU1MmNNYyCqlXicq2EtS-w2y/view?usp=sharing

## Future Improvements
There are few areas which according to me can be improved
1. We can increase the experiment_timeout_minutes. In this code it is set to 15 minutes but can be increased to a higher number like 20-30 minutes.
2. We can use different primary metric and can observe if the accuracy of the model changes or not.
3. Since here we have a lot of features (20 in number to  predict target) we can perform some feature engineering and remove the unecessary features. This in turn would prevent overfitting i.e. the model would generalise itself more and hence will give a high accuracy when it sees test data.

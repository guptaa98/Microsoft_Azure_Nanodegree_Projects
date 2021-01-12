# Operationalizing Machine Learning
This project is part of the Udacity Azure ML Nanodegree. In this project, I've worked with the Bank Marketing dataset which contains 21 features and we had to predict whether a person will take a loan or not. The was our target column y. 
Microsft Azure was used to configure a cloud-based machine learning production model, deploy it, and consume it. We will also create, publish, and consume a pipeline using Azure Python SDK.

## Architectural Diagram
*TODO*: Provide an architectual diagram of the project and give an introduction of each step.

## Key Steps
**Step 1: Authenication**

Used the lab provided by udacity so this step was skipped.

**Step 2: Create and run Auto ML Experiment**

1. Uploaded the bank marketing dataset to Azure.
2. A new Compute Cluster was made with Standard_DS12_v2 as the vm and 1 as the minimum number of nodes. Max number of nodes were 5.
3. Used the above dataset to create an automl run experiment using classification with target column as 'y'. The Exit Criteria was 1 hour and concurrency was set to 5. 

**Step 3: Create and run Auto ML Experiment**

After the experiment run completes, a summary of all the models and their metrics are shown, including explanations. 
1. The Best Model was Voting Ensemble Model and hence selected for deployment. Deploying the Best Model will allow to interact with the HTTP API service and interact with the model by sending data over POST requests.
2. The *Authentication* was enabled and the model was deployed using *Azure Container Instances*

**Step 4: Enable Application Insights**

Now that the Best Model is deployed, in this step we will enable Application Insights and retrieve logs. Although this was configurable at deploy time with a check-box, but we used logs.py for this purpose.
1. Download the config.json file and stored it into the same directory of logs.py.
2. Replaced the default model name in the script with our deployed model name and then ran *python logs.py* in git-bash. 
3. We are going to see some results in the terminal and when we go back to our Azure studio we'll see that the application insights were enabled (True). 
   Application Insight URL was available which gave all the information regarding Server Requests, Server Response Time, Failed Requests and availability.

**Step 5: Swagger Documentation**

In this step, we will consume the deployed model using Swagger.
1. Downloaded the swagger.json file fro swagger URI. *Remember to keep this file in the same directory as of swagger.sh and serve.py files.*
2. swagger.sh will download the latest Swagger container, and it will run it on port 80 by default. Since permission for port 80 on your computer wasn't granted, updated the port to 9000.
3. Used gitbash to run the Serve.py and Swagger.sh files.
4. Observed the contents of the API for the model using HTTP API responses and methods.

**Step 6: Consume Model Endpoints**

Since the model is deployed, we'll use the endpoint.py script provided to interact with the trained model.
1. Updated the scoring_uri with REST endpoint URL and key with primary key of the deployed model.
2. Executed *python endpoint.py* and the results were similar to {results : ["yes","no"]}.

**Step 7: Create, Publish and Consume a Pipeline**

1. Uploaded the provided notebook to azure.
2. All the variables were updated to match our environment.
3. config.json file was downloaded and was available in the current working directory.
4. Pipeline was created and scheduled to run. 

## Screen Recording
The screencast of my project can be found here.



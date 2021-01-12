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

After the experiment run completes, a summary of all the models and their metrics are shown, including explanations. The Best Model was Voting Ensemble Model and was selected for deployment.
Deploying the Best Model will allow to interact with the HTTP API service and interact with the model by sending data over POST requests.
The *Authentication* was enabled and the model was deployed using *Azure Container Instances*

**Step 4: Enable Application Insights**

Now that the Best Model is deployed, in this step we will enable Application Insights and retrieve logs. Although this was configurable at deploy time with a check-box, but we are going to use logs.py for this purpose.
Replace the default model name in the script with our deployed model name and then run *python logs.py* in git-bash. We are going to see some results in the terminal and when we go back to our Azure studio we'll see that the application insights were enabled (True). 
There you'll see an Application Insight URL which will give us all the information regarding Service time, Response Time, Failed Requests and availability.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.

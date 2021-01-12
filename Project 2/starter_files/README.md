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
2. Used the above dataset to create an automl run experiment using classification with target column as 'y'. The Exit Criteria was 1 hour and concurrency was set to 5.  

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.

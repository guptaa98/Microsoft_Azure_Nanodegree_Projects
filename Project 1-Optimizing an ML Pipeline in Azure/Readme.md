# Optimizing an ML Pipeline in Azure

## Overview
This project is part of the Udacity Azure ML Nanodegree.
In this project, we build and optimize an Azure ML pipeline using the Python SDK and a provided Scikit-learn model.
This model is then compared to an Azure AutoML run.

## Summary
The data is related with direct marketing campaigns of a Portuguese banking institution. Our goal is to predict if the client will subscribe to a fixed term deposit with a financial institution or not which is given by feature named y.
The total number of instances are 45211 and total number of features are 17

The best performing model was VotingEnsemble model obtained from AutoML which outperforms Logistic Regression Model with an accuracy of 0.91692288 whereas the accuracy of Logistic Regression Model was only 0.9111785533636824.

## Scikit-learn Pipeline
**Explain the pipeline architecture, including data, hyperparameter tuning, and classification algorithm.**
## Architecture of train.py file 
Following are the operations performed by train.py script
1. First, the important libraries are imported.
2. Used TabularDatasetFactory to import the data.
3. clean_data function is used to clean and one hot encode the data. It returns the x and y data where x is containing the whole data on which training and testing needs to be      done,whereas y contains the labels.
4. x_train, x_test, y_train, y_test are made by splitting x and y where test_size = 0.3 and random_state = 42
5. Another function is 'main', where LogisticRegression model fits the data and is returned to model variable and the accuracy is calculated.The results are stored in the          outputs folder.
## HyperDrive and Hyperparameter tuning
hyperdrive_config = HyperDriveConfig (estimator = est,
                             hyperparameter_sampling = ps,
                             policy = policy,
                             primary_metric_name = "Accuracy",
                             primary_metric_goal = PrimaryMetricGoal.MAXIMIZE,
                             max_total_runs = 50,
                             max_concurrent_runs = 3
                             )
The description of hyperdrive configuration are as follows - 
1. A sklearn estimator is created for interacting with train.py file. The source directory, the entry script and compute target are passed to the variable est.
2. Random Parameter Sampler is chosen to be used and is stored in ps variable.
   **Benefits**
   The main benefits include its support for termination of low-performance runs and the other one is that it supports both continuos and discrete parameters.
   There were two parameters passed, one was continuos that is regularization parameter '--C' where a uniformly distributed value distributed between (-.-5,0.1) will be chosen      at every iteration and a discrete parameter '--max_iter' which had a choice of value between (16,32,64,128).
3. Bandit Policy is used as an early stopping policy which terminates runs where the primary metric is not within the specified slack factor compared to the best performing run.
   The runs which have the primary metric value less than (best performing run metric/(1+slack_factor)) are terminated.
   **Benefits**
   Choosing an Early Termination Policy helps to automatically terminate poorly performing runs. This early termination gives us computational efficiency.
   Bandit Policy helps in aggressive saving of the computational power more than other.
4. primary_metric_goal can be either PrimaryMetricGoal.MAXIMIZE or PrimaryMetricGoal.MINIMIZE determining if the primary metric will be maximized or minimized when evaluating      the runs.
5. The name of the primary metric needs to exactly match the name of the metric logged by the training script i.e. train.py and here it is Accuracy.
6. max_total_runs contains the value maximum training runs that are to be run. The value should be between 1-1000.
7. max_concurrent_runs contains the maximum number of runs that can run concurrently i.e at the same time. If not specified, all runs launch in parallel. The value must be an      integer between 1 and 100.
**The best model obtained from using hyperdrive gave and accuracy of 0.9111785533636824.**
**Logistic Regression**
## Logistic Regression 
This model is used when the value to be predicted is categorical. 
The problem we solved here was a binary classification problem having 2 categories with values 0 and 1.

## AutoML
1. In AutoML, the data is imported to a dataframe ds using TabularDatasetFactory.
2. Clean data function is called to clean the data returning x(data used for prediction) and y(target variables).
3. AutoML config is prepared as shown below
   automl_config = AutoMLConfig(
    experiment_timeout_minutes=30,
    task="classification",
    primary_metric="accuracy",
    training_data=dataset,
    label_column_name='y',
    n_cross_validations=5)
4. The AutoML run is submitted and the best model is retrived and saved.
   The snippets of output are shown below.
   ![Screenshot 2020-12-16 013859](https://user-images.githubusercontent.com/46073909/102267243-a2197900-3f3f-11eb-8e64-b174ad4b7c3f.jpg)
   ![acc](https://user-images.githubusercontent.com/46073909/102267367-cb3a0980-3f3f-11eb-8d8b-ec2a5ac04709.jpg)
   ![best run](https://user-images.githubusercontent.com/46073909/102267468-f45a9a00-3f3f-11eb-92a8-85c9f80ae0c6.jpg)

## Pipeline comparison
**Compare the two models and their performance. What are the differences in accuracy? In architecture? If there was a difference, why do you think there was one?**
The approach using hyperdrive only uses the machine learning model that has been provided to it. Hyperdrive recieves parameters to perform hyperparameter tuning which is the process of finding the configuration of hyperparameters that results in the best performance.
AutoML on the other hand runs a lot of different machine learning algorithms and returns the one which gives the highest primary metric i.e., the best model.

In this project it was found that AutoML approach outperformed the HyperDrive approach.
**Accuracy of Hyperdrive** - 0.9111785533636824.
**Accuracy of AutoML** - 0.91692288 , Best Model - VotingEnsemble model

## Future work
**In hyperdrive** - 1. Different Early Termination Policy can be used. Experiments can be done with max total runs and concurrent runs.                                                               2. If computational expense is not an issue one can avoid early termination policy.                                                                           **In AutoML** - 1. Experiment timeout minutes can be increased or avoided. One can choose to use different primary metric too.


# Prediction of Heart Disease

In this project, two models are created: one using Automated ML and one customized model whose hyperparameters are tuned using HyperDrive. The performance of both the models is compared and the best performing model is deployed.

## Dataset

### Overview
The description of the attributes is as follows - 
1. *age* -  age
2. *sex* - sex (1 = male; 0 = female)
3. *cp* - chest pain type (4 values)
4. *trestbps* - resting blood pressure
5. *chol* - serum cholestoral in mg/dl
6. *fbs* - fasting blood sugar > 120 mg/dl
7. *restecg* - resting electrocardiographic results (values 0,1,2)
8. *thalach* - maximum heart rate achieved
9. *exang* - exercise induced angina
10. *oldpeak* - ST depression induced by exercise relative to rest 
11. *slope* - the slope of the peak exercise ST segment 
12. *ca* - number of major vessels (0-3) colored by flourosopy
13. *thal* - 3 = normal; 6 = fixed defect; 7 = reversable defect
14. *target* - 0 or 1

### Task
Our target is to predict if a person has heart disease or not. The target 0 refers to the absence of disease and 1 refers to its presence.
This goal will be achieved by going through the other 13 attributes described above. 

**The dataset can be downloaded from here - https://www.kaggle.com/ronitf/heart-disease-uci**

### Access
The dataset is accessed by creating a TabularDataset using TabularDatasetFactory.
Following is the code to achieve this.

URL = "https://raw.githubusercontent.com/guptaa98/Microsoft_Azure_Nanodegree_Projects/main/Capstone%20Project/heart.csv"

ds = TabularDatasetFactory.from_delimited_files(path=URL)

## Automated ML

**automated ml settings** 
1. experiment_timeout_minutes: 20. This is the setting which states that if an experiment doesn't conclude in 20 minutes then it will be cancelled.
2. primary_metric: "accuracy". Since the primary metric is set as accuracy, so the models will be prioritised on the accuracy. The model with the highest accuracy will be termed as best model.

**auto ml configuration**
1. task - Since we have to predict if a person has a heart disease or not, this narrows down to classification task. So the task set here is Classification.
2. training_data = The training data set here is 'dataset' which is x_train + y_train
3. label_column_name='target'. This is the column which is to be predicted.
4. n_cross_validations=5 . This is the number of cross fold validations to perform. 
 
### Results
The best model through auto ml was VotingEnsemble model which had an accuracy score of 0.8766183574879227

**Improvements in Auto ML**
1. The experiment timeout minutes could be increased.
2. We can also increase cross validation number if we want higher accuracy.

**RunDetails of Auto ML**
![auto ml run details](https://user-images.githubusercontent.com/46073909/105363854-7fefd680-5c22-11eb-8e15-7df35bf0bce5.png)

![auto ml acc chart](https://user-images.githubusercontent.com/46073909/105363847-7e261300-5c22-11eb-8c16-b0475a37adc1.png)

**Auto ml Best Model**
![auto ml best model](https://user-images.githubusercontent.com/46073909/105365030-d90c3a00-5c23-11eb-828b-e97b3fa5a53b.png)


![automl best metric](https://user-images.githubusercontent.com/46073909/105363858-80886d00-5c22-11eb-893b-070bdd62195f.png)

## Hyperparameter Tuning
### Logistic Regression
This model is used when the value to be predicted is categorical. The problem we solved here was a binary classification problem having 2 categories with values 0 and 1 indicating absence and presence of disease hence this model was chosen.
hyperdrive_run_config = HyperDriveConfig (estimator = estimator,
                             hyperparameter_sampling = param_sampling,
                             policy = early_termination_policy,
                             primary_metric_name = "Accuracy",
                             primary_metric_goal = PrimaryMetricGoal.MAXIMIZE,
                             max_total_runs = 25,
                             max_concurrent_runs = 3
                             ).
The description of hyperdrive configuration are as follows -
1. A sklearn estimator is created for interacting with train.py file. The source directory, the entry script and compute target are passed to the variable estimator.

2. Random Parameter Sampler is chosen to be used and is stored in param_sampling variable.The main benefits include its support for termination of low-performance runs and the other one is that it supports both continuos and discrete parameters.

3. There were two parameters passed, one was continuos that is regularization parameter '--C' where a uniformly distributed value distributed between (0.05,0.1) will be chosen at every iteration and a discrete parameter '--max_iter' which had a choice of value between (16,32,64,128).

4. Bandit Policy is used as an early stopping policy which terminates runs where the primary metric is not within the specified slack factor compared to the best performing run. The runs which have the primary metric value less than (best performing run metric/(1+slack_factor)) are terminated. Benefits of Choosing an Early Termination Policy helps to automatically terminate poorly performing runs. This early termination gives us computational efficiency. Bandit Policy helps in aggressive saving of the computational power more than other.
It's parameters were
 4.1 slack_factor = 0.1
 4.2 evaluation_interval=2
 4.3 delay_evaluation=5 
5. primary_metric_goal can be either PrimaryMetricGoal.MAXIMIZE or PrimaryMetricGoal.MINIMIZE determining if the primary metric will be maximized or minimized when evaluating the runs.The name of the primary metric needs to exactly match the name of the metric logged by the training script i.e. train.py and here it is Accuracy.

6. max_total_runs contains the value maximum training runs that are to be run. The value should be between 1-1000. 
here max_total_runs were 25. 
7. max_concurrent_runs contains the maximum number of runs that can run concurrently i.e at the same time. If not specified, all runs launch in parallel. The value must be an integer between 1 and 100.
Here the value chosen was 3. 

**Improvements**
1. The number of runs were only 25. These could have been increased to a higher number which could lead to a possibility of higher accuracy.
2. We can also use some other primary metric and observe if that helps in improving our model.

### Results 
The best model obtained from using hyperdrive gave and accuracy of 0.8571428571428571. Have a look at the run details and scatter charts and its parameters.

**RunDetails Widget**
![hd run details 1](https://user-images.githubusercontent.com/46073909/105368137-36ee5100-5c27-11eb-9275-00c7c80a68e7.png)

![Acc chart ](https://user-images.githubusercontent.com/46073909/105368133-35bd2400-5c27-11eb-99f1-1adb44b5bc94.png)

![scatter chart](https://user-images.githubusercontent.com/46073909/105368139-381f7e00-5c27-11eb-87d9-5ce7dab355cc.png)

## Model Deployment
Below steps are to be followed for model deployment.
1. Save the best fitted model using joblib.dump
joblib.dump(fitted_model, "best_automl_model.pkl") 
The above code will save your best auto ml model to be deployed as best_automl_model.pkl

2. Register the best model.
We'll now register our model using Model.register from azureml.core.model. We'll pass our model path, model name and the workspace as the attributes. to Model.register. This can be achieved by Model.register(model_path="best_automl_model.pkl", model_name="best_automl_model", workspace = ws).

3. Now for our Inference Configuration we'll need two files named as score.py and env.yml file. These files can be downloaded by using these two lines of code.
   3.1. best_run.download_file('outputs/scoring_file_v_1_0_0.py', 'score.py')
   3.2. best_run.download_file('outputs/conda_env_v_1_0_0.yml', 'myenv.yml')
3. Since the files have been downloaded, define the inference_config by passing score.py and environment.
![inf_config](https://user-images.githubusercontent.com/46073909/105370887-0f4cb800-5c2a-11eb-81cc-6a2c73046658.png)

4. Define the deployment_conf. Deploy the model on AciWebservice. Refer to the screenshot below 
![healthy dep state](https://user-images.githubusercontent.com/46073909/105371096-46bb6480-5c2a-11eb-9d56-a1c7dae40c40.png)

5. In the above screenshot we can see that the model is successfully deployed.

6. Now let's test our deployed model by sending a request and see if the model gives a reponse in the desired format. We can achieve this by using the following code in which we send two sets of data and in the response we'll get the target values.
![req1](https://user-images.githubusercontent.com/46073909/105372805-ffce6e80-5c2b-11eb-9e9a-4047453c52ab.png)
![resp](https://user-images.githubusercontent.com/46073909/105372814-00ff9b80-5c2c-11eb-85c6-b72350740040.png)

From the above screenshots we can see that our deployed model gives us a response back which is [0,0] . This is the target value for our dataset values which we sent as a request to the model. 

**Hence, it can be concluded that our model is succesfully deployed and also gives a desired response back when a request is sent to it** 

## Screen Recording
**The link to the screencast is**
https://drive.google.com/file/d/1KgQOEjzV_XhzYJWa6FslQv75Rvgf2qiv/view?usp=sharing

*Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response*

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
*TODO*: Give an overview of the `automl` settings and configuration you used for this experiment

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.

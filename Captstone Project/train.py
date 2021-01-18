Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
from sklearn.linear_model import LogisticRegression
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory

from azureml.data.dataset_factory import TabularDatasetFactory
URL = "https://www.kaggle.com/ronitf/heart-disease-uci"
ds = TabularDatasetFactory.from_delimited_files(path=URL)### YOUR CODE HERE ###

y = pd.DataFrame()
y['target'] = ds['target']
x = pd.DataFrame()
x = ds
x.drop('target',axis = 1, inplace=True)


#x, y = clean_data(ds)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

run = Run.get_context()

import joblib
def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")

    args = parser.parse_args()

    run.log("Regularization Strength:", np.float(args.C))
    run.log("Max iterations:", np.int(args.max_iter))

    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)
    
    os.makedirs('outputs', exist_ok=True)
    joblib.dump(model, 'outputs/model.joblib')

    accuracy = model.score(x_test, y_test)
    run.log("Accuracy", np.float(accuracy))


if __name__ == '__main__':
    main()

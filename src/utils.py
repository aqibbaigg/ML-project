import os 
import sys

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql


#for data transformation
import numpy as np
import pickle

load_dotenv()

host = os.getenv('host')
user = os.getenv('user')
password=os.getenv('Password')
db=os.getenv('db')

def read_sql_data():
    logging.info("Reading data from SQL database")
    try:
        mydb=pymysql.connect(host=host, user=user, password=password, db=db)
        logging.info("Successfully connected to the database",mydb)
        df=pd.read_sql_query("SELECT * FROM students", mydb)
        print(df.head())

        return df
    except Exception as ex:
        raise CustomException(ex)
    


#data transformation utility functions
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(X_train, y_train, X_test, y_test, models, params):
    try:
        report = {}

        for i in range(len(models)):
            model = list(models.values())[i]
            para = params[list(models.keys())[i]]

            gs = GridSearchCV(model, para, cv=5)
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)




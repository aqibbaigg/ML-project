import os 
import sys
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




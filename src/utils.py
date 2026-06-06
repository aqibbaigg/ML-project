import os 
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql
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
    
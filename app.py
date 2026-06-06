from src.exception import CustomException
from src.logger import logging
from src.components.Data_Ingestion import Data_Ingestion, Data_IngestionConfig
import sys

if __name__ == "__main__":
    logging.info("the execution has started")

    try:
        #data_ingestion_config = Data_IngestionConfig()
        Data_Ingestion = Data_Ingestion()
        Data_Ingestion.initiate_data_ingestion() 

    except Exception as e:
        logging.info("custom exception ")
        raise CustomException(e, sys)
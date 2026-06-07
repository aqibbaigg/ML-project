from src.components.Data_Transformation import Data_Transformation, Data_TransformationConfig
from src.exception import CustomException
from src.logger import logging
from src.components.Data_Ingestion import Data_Ingestion, Data_IngestionConfig
import sys

if __name__ == "__main__":
    logging.info("the execution has started")

    try:
        #data_ingestion_config = Data_IngestionConfig()
        Data_Ingestion = Data_Ingestion()
        train_data_path, test_data_path = Data_Ingestion.initiate_data_ingestion() 
        #data_transformation_config = Data_TransformationConfig()
        data_transformation = Data_Transformation()
        data_transformation.initiate_data_transformation(train_data_path,test_data_path)
           
    except Exception as e:
        logging.info("custom exception ")
        raise CustomException(e, sys)
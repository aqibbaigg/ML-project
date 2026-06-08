from src.components.Data_Transformation import Data_Transformation, Data_TransformationConfig  
from src.exception import CustomException
from src.logger import logging
from src.components.Data_Ingestion import Data_Ingestion, Data_IngestionConfig
from src.components.Model_Trainer import ModelTrainer, ModelTrainerConfig
import sys


if __name__ == "__main__":
    logging.info("the execution has started")

    try:
        #data_ingestion_config = Data_IngestionConfig()
        Data_Ingestion = Data_Ingestion()
        train_data_path, test_data_path = Data_Ingestion.initiate_data_ingestion() 

        #data_transformation_config = Data_TransformationConfig()
        data_transformation = Data_Transformation()
        train_array, test_array, preprocessor = data_transformation.initiate_data_transformation( train_data_path,test_data_path)

        #model_trainer_config = ModelTrainerConfig()
        model_trainer = ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_array, test_array))
           
    except Exception as e:
        logging.info("custom exception ")
        raise CustomException(e, sys)
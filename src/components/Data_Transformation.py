import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from src.exception import CustomException
from src.logger import logging
import os
from src.utils import save_object



@dataclass
class Data_TransformationConfig:
    preprocessor_obj_file_path: str = os.path.join('artifacts', 'preprocessor.pkl')

class Data_Transformation: 
    def __init__(self):
        self.data_transformation_config = Data_TransformationConfig()

    def get_data_transformer_object(self, X: pd.DataFrame):
        try:
            num_features = X.select_dtypes(exclude="object").columns.tolist()
            cat_features = X.select_dtypes(include="object").columns.tolist()

            num_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())
            ])

            cat_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder", OneHotEncoder(drop='first')),
                ("scaler", StandardScaler(with_mean=False))
            ])

            logging.info(f"Numerical columns: {num_features}")
            logging.info(f"Categorical columns: {cat_features}")


            preprocessor = ColumnTransformer(
                transformers=[
                    ("num_pipeline", num_pipeline, num_features),
                    ("cat_pipeline", cat_pipeline, cat_features)
                ]
            )
            return preprocessor
        

        except Exception as e:
            raise CustomException(e, sys)
        

    def initiate_data_transformation(self, train_path: str, test_path: str):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")
    
            preprocessing_obj = self.get_data_transformer_object(X=train_df.drop(columns=['math_score']))  

            X_train = train_df.drop(columns=['math_score'])
            y_train = train_df['math_score']

            X_test = test_df.drop(columns=['math_score'])
            y_test = test_df['math_score']

            logging.info("Separated input features and target feature from train and test dataframe")

            X_train_transformed =preprocessing_obj.fit_transform(X_train)
            X_test_transformed = preprocessing_obj.transform(X_test)


            train_arr = np.c_[X_train_transformed, y_train.to_numpy()]
            test_arr = np.c_[X_test_transformed, y_test.to_numpy()]

            logging.info("Applied preprocessing object on train and test data")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return (train_arr, test_arr, self.data_transformation_config.preprocessor_obj_file_path)

        except Exception as e:
            raise CustomException(e, sys)
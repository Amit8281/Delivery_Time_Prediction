from src.constants import *
from src.logger import logging
from src.exception import CustomException
from src.utils import save_obj
import os,sys
from src.config.configuration import *
from src.utils import load_model
import pandas as pd

class PredictionPipeline():
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path= PREPROCESSING_OBJ_FILE
            model_path = MODEL_FILE_PATH

            preprocessor = load_model(preprocessor_path)
            model = load_model(model_path)

            data_scaled = preprocessor.transform(features)

            pred = model.predict(data_scaled)
            return pred
        

        except Exception as e:
            logging.info("error accured in prediction pipeline")
            CustomException(e,sys)
        '''
            categorical_columns = ['Type_of_order','Type_of_vehicle','Festival','City']
            ordinal_encoder = ['Road_traffic_density', 'Weather_conditions']
            numerical_column=['Delivery_person_Age','Delivery_person_Ratings','Vehicle_condition',
                              'multiple_deliveries','distance']
        '''

class CustomData:
    def __init__(self,
                Delivery_person_Age:int,
                Delivery_person_Ratings:float,
                Weather_conditions:str,
                Vehicle_condition:int,
                multiple_deliveries:int,
                Road_traffic_density:str,
                distance:float,
                Type_of_order:str,
                Type_of_vehicle:str,
                Festival:str,
                City:str):
        self.Delivery_person_Age=Delivery_person_Age
        self.Delivery_person_Ratings=Delivery_person_Ratings
        self.Weather_conditions=Weather_conditions
        self.Vehicle_condition=Vehicle_condition
        self.multiple_deliveries=multiple_deliveries
        self.Road_traffic_density=Road_traffic_density
        self.distance=distance
        self.Type_of_order=Type_of_order
        self.Type_of_vehicle=Type_of_vehicle
        self.Festival=Festival
        self.City=City

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'Delivery_person_Age':[self.Delivery_person_Age],
                'Delivery_person_Ratings':[self.Delivery_person_Ratings],
                'Weather_conditions':[self.Weather_conditions],
                'Vehicle_condition':[self.Vehicle_condition],
                'multiple_deliveries':[self.multiple_deliveries],
                'Road_traffic_density':[self.Road_traffic_density],
                'distance':[self.distance],
                'Type_of_order':[self.Type_of_order],
                'Type_of_vehicle':[self.Type_of_vehicle],
                'Festival':[self.Festival],
                'City':[self.City]

            }

            df = pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            logging.info("error accured in prediction pipeline")
            CustomException(e,sys)






                     
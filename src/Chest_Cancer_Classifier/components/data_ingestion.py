import os
import zipfile
import gdown 
from Chest_Cancer_Classifier import logger
from Chest_Cancer_Classifier.utils.common import get_size
from Chest_Cancer_Classifier.constants import *
from Chest_Cancer_Classifier.utils.common import  read_yaml,create_directories
from Chest_Cancer_Classifier.entity.config_entity import (DataIngestionConfig)

class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config
    
    def download_file(self) -> str:
        ''' 
        fetch data from the url
        '''

        try:
            dataset_url = self.config.source_url
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion",exist_ok=True)
            logger.info("Downloading data from {dataset_url} into file {zip_download_dir}")
            
            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id,zip_download_dir)

            logger.info("Downloaded data from {dataset_url} into file {zip_download_dir}")
        
        except Exception as e:
            raise e

    def extract_zip_file(self):
        '''
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns none
        
        '''

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)

    
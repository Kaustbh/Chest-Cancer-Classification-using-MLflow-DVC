from Chest_Cancer_Classifier import logger
from Chest_Cancer_Classifier.pipline.stage_01_data_ingestion import DataIngestionTrainingPipline
 

STAGE_NAME = 'Data Ingestion stage'

try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<< \n\n")
     
except Exception as e:
         logger.exception(e)
         raise e

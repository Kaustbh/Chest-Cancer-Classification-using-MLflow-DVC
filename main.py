from Chest_Cancer_Classifier import logger
from Chest_Cancer_Classifier.pipline.stage_01_data_ingestion import DataIngestionTrainingPipline
from Chest_Cancer_Classifier.pipline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipline
from Chest_Cancer_Classifier.pipline.stage_03_model_trainer import ModelTrainingPipeline
from Chest_Cancer_Classifier.pipline.stage_04_model_evaluation import EvaluationPipeline
STAGE_NAME = 'Data Ingestion stage'

try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<< \n\n")
     
except Exception as e:
         logger.exception(e)
         raise e


STAGE_NAME = 'Prepare Base Model'

try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelTrainingPipline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<< \n\n")
     
except Exception as e:
         logger.exception(e)
         raise e 


STAGE_NAME = 'Training'

try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<< \n\n")
     
except Exception as e:
         logger.exception(e)
         raise e


STAGE_NAME = 'Evaluation'

try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<< \n\n")
     
except Exception as e:
         logger.exception(e)
         raise e
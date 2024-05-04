from Chest_Cancer_Classifier.config.configuration import ConfigurationManager
from Chest_Cancer_Classifier.components.model_trainer import Training
from Chest_Cancer_Classifier import logger


STAGE_NAME = 'Training'

class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()

if __name__=='__main__':
     try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<< \n\n")
     
     except Exception as e:
         logger.exception(e)
         raise e
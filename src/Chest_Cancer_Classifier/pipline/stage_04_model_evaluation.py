from Chest_Cancer_Classifier.config.configuration import ConfigurationManager
from Chest_Cancer_Classifier.components.model_evaluation import Evaluation
from Chest_Cancer_Classifier import logger


STAGE_NAME = 'Evaluation'

class EvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.ger_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()

if __name__=='__main__':
     try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<< \n\n")
     
     except Exception as e:
         logger.exception(e)
         raise e
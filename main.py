
from cnnClassification import logger
from cnnClassification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
if __name__ == "__main__":
    try:
        print(f"{'>>'*20} {STAGE_NAME} started {'<<'*20}")
        pipeline = DataIngestionTrainingPipeline()
        pipeline.main()
        print(f"{'>>'*20} {STAGE_NAME} completed {'<<'*20}")
    except Exception as e:
        print(e)
        raise e
    
STAGE_NAME = "Prepare Base Model stage"
if __name__ == "__main__":
    try:
        logger.info(f"{'>>'*20} {STAGE_NAME} started {'<<'*20}")
        pipeline = PrepareBaseModelTrainingPipeline()
        pipeline.main()
        logger.info(f"{'>>'*20} {STAGE_NAME} completed {'<<'*20}")
    except Exception as e:
        logger.exception(e)
        raise e

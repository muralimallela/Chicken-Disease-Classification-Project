
from cnnClassification import logger
from cnnClassification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


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
from cnnClassification.config.configuration import ConfigurationManager
from cnnClassification.components.data_ingestion import DataIngestion


STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        print(f"{'>>'*20} {STAGE_NAME} started {'<<'*20}")
        pipeline = DataIngestionTrainingPipeline()
        pipeline.main()
        print(f"{'>>'*20} {STAGE_NAME} completed {'<<'*20}")
    except Exception as e:
        print(e)
        raise e

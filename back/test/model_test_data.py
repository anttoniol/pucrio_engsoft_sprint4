from back.loader import Loader

# Classe com dados que são utilizados pelo pytest
class ModelTestData:
    def __init__(self, model_name, model_file_path, csv_file_path):
        loader = Loader()
        self.__model = loader.load_model(model_name, model_file_path)
        self.__dataframe = loader.load_csv(csv_file_path)

    def get_model(self):
        return self.__model

    def get_dataframe(self):
        return self.__dataframe
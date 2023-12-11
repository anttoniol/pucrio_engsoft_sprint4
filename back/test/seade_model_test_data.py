import os

from back.test.model_test_data import ModelTestData

dir = os.path.dirname(__file__)

# Classe com dados do dataset da Fundação Seade e que são utilizados pelo pytest
class SeadeModelTestData(ModelTestData):
    __model_name = "Logistic Regression"
    __model_file_path = os.path.join(dir, '..', '..', 'classificador.pkl')
    __csv_file_path = os.path.join(dir, '..', '..', 'csvs', 'casos_obitos_raca_cor.csv')
    __target_column = "obito"

    # Valores obtidos no notebook
    __metrics = {
        "accuracy": 0.9708,
        "precision": 0.5625,
        "jaccard": 0.1978021978021978,
        "recall": 0.23376623376623376
    }

    def __init__(self):
        super().__init__(self.__model_name, self.__model_file_path, self.__csv_file_path)

    def get_metrics(self):
        return self.__metrics

    def get_target_column(self):
        return self.__target_column
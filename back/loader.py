import pickle

import pandas as pd

from back.model import Model


# Classe responsável pelo carregamento de arquivos pkl (com dados de um modelo) e arquivos csv (com o dataset)
class Loader:
    def load_model(self, model_name, model_file_path):
        pickle_in = open(model_file_path, 'rb')
        model = Model(model_name, pickle.load(pickle_in))
        pickle_in.close()
        return model

    def load_csv(self, csv_file_path, sep = ";"):
        return pd.read_csv(csv_file_path, sep = sep)
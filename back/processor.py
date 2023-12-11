import random

import pandas as pd

# Classe para processamento de um dataset
class Processor:
    def remove_columns(self, dataframe, columns_to_remove):
        return dataframe.loc[:, ~dataframe.columns.isin(columns_to_remove)]

    def get_sample(self, dataframe, seed = 7, sample_size = 10000):
        random.seed(seed)
        population = list(range(len(dataframe.index)))
        sample = random.sample(population, k = sample_size)
        return dataframe.loc[sample, :]

    def replace_na_values(self, dataframe, column_name, new_value):
        new_dataframe = dataframe.copy()
        new_column = new_dataframe[column_name].fillna(new_value)
        new_dataframe[column_name] = new_column
        return new_dataframe

    def apply_dummy_encoding(self, data, columns=None, prefix_sep='_'):
        return pd.get_dummies(data=data, columns=columns, prefix_sep=prefix_sep)

    def prepare_to_dummy_encoding(self, dataframe, columns):
        encoded_dataframe = pd.DataFrame(columns=columns)
        encoded_dataframe = pd.concat([encoded_dataframe, dataframe[columns]])
        return self.apply_dummy_encoding(encoded_dataframe)

    def replace_string_values(self, dataframe, column_name, replacement_dict):
        new_dataframe = dataframe.copy()
        for key in replacement_dict:
            column = new_dataframe[column_name].str.replace(key, replacement_dict[key], regex=True)
            new_dataframe[column_name] = column
        return new_dataframe

    def replace_na_values_with_median(self, dataframe, column_name):
        new_dataframe = dataframe.copy()
        median = new_dataframe[column_name].median()
        new_dataframe = self.replace_na_values(new_dataframe, column_name, median)
        return new_dataframe

    def replace_na_values_with_median_in_multiple_columns(self, dataframe, columns):
        new_dataframe = dataframe.copy()
        for column in columns:
            new_dataframe = self.replace_na_values_with_median(new_dataframe, column)
        return new_dataframe

    def get_X_and_y(self, dataframe, target_column_name):
        array = dataframe.values
        column_names = dataframe.columns.values.tolist()

        columns = list(range(len(column_names)))
        target_index = column_names.index(target_column_name)

        columns.remove(target_index)

        X = array[:, columns]
        raw_y = array[:, target_index].reshape(-1, 1).tolist()  # Coluna alvo

        y = list()
        for element in raw_y:
            y += element
        y = [int(element) for element in y]

        return X, y
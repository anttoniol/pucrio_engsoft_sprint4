from back.processor import Processor

# Classe para processamento do dataset da Fundação Seade, com o auxílio da classe Processor
class SeadeProcessor(Processor):
    def remove_irrelevant_columns(self, dataframe):
        columns_to_remove = ["codigo_ibge", "nome_munic", "nome_drs"]
        return self.remove_columns(dataframe, columns_to_remove)

    def format_obito_column(self, dataframe):
        return self.replace_na_values(dataframe, "obito", -1)

    def format_racacor_column(self, dataframe):
        new_dataframe = self.replace_na_values(dataframe, "raca_cor", "DESCONHECIDA")
        encoded_dataframe_raca_cor = self.prepare_to_dummy_encoding(new_dataframe, ["raca_cor"])
        new_dataframe.drop("raca_cor", axis=1, inplace=True)
        new_dataframe[encoded_dataframe_raca_cor.columns.to_list()] = encoded_dataframe_raca_cor.values.tolist()
        return new_dataframe

    def format_covid19_column(self, dataframe):
        new_dataframe = self.replace_na_values(dataframe, "diagnostico_covid19", "-1")
        encoded_dataframe_diagnostico_covid19 = self.prepare_to_dummy_encoding(new_dataframe, ["diagnostico_covid19"])
        new_dataframe.drop("diagnostico_covid19", axis=1, inplace=True)
        new_dataframe[encoded_dataframe_diagnostico_covid19.columns.to_list()] = encoded_dataframe_diagnostico_covid19.values.tolist()
        return new_dataframe

    def format_idade_column(self, dataframe):
        median = dataframe["idade"].median()
        new_dataframe = self.replace_na_values(dataframe, "idade", median)
        first_filter = new_dataframe["idade"] <= -1
        second_filter = new_dataframe["idade"] >= 130
        new_dataframe.loc[first_filter | second_filter, "idade"] = median
        return new_dataframe

    def format_sexo_column(self, dataframe):
        new_dataframe = self.replace_na_values(dataframe, "cs_sexo", "DESCONHECIDO")

        encoded_dataframe = self.prepare_to_dummy_encoding(new_dataframe, ["cs_sexo"])
        new_dataframe.drop("cs_sexo", axis=1, inplace=True)
        new_dataframe[encoded_dataframe.columns.to_list()] = encoded_dataframe.values.tolist()
        return new_dataframe

    def format_disease_columns(self, dataframe):
        disease_columns = ["asma", "cardiopatia", "diabetes", "doenca_hematologica", "doenca_hepatica", "doenca_neurologica",
                           "doenca_renal", "imunodepressao", "obesidade", "pneumopatia", "puerpera", "sindrome_de_down"]
        return self.replace_na_values_with_median_in_multiple_columns(dataframe, disease_columns)

    def format_dataframe(self, dataframe):
        new_dataframe = self.remove_irrelevant_columns(dataframe)
        new_dataframe = self.get_sample(new_dataframe)
        new_dataframe.reset_index(inplace = True, drop = True)
        new_dataframe = self.format_obito_column(new_dataframe)
        new_dataframe = self.format_racacor_column(new_dataframe)
        new_dataframe = self.format_covid19_column(new_dataframe)
        new_dataframe = self.format_idade_column(new_dataframe)
        new_dataframe = self.format_sexo_column(new_dataframe)
        new_dataframe = self.format_disease_columns(new_dataframe)
        new_dataframe = new_dataframe.infer_objects()
        return new_dataframe
from predictor.predictor_model_loader import PredictorModelLoader


class PredictorService:
    predictor_model_loader = PredictorModelLoader('classificador.pkl')
    def predict(self, json_request):
        idade = json_request["idade"]
        asma = json_request["asma"]
        cardiopatia = json_request["cardiopatia"]
        diabetes = json_request["diabetes"]
        doenca_hematologica = json_request["doenca_hematologica"]
        doenca_hepatica = json_request["doenca_hepatica"]
        doenca_neurologica = json_request["doenca_neurologica"]
        doenca_renal = json_request["doenca_renal"]
        imunodepressao = json_request["imunodepressao"]
        obesidade = json_request["obesidade"]
        pneumopatia = json_request["pneumopatia"]
        puerpera = json_request["puerpera"]


        """
        sindrome_de_down: int = Field(None, description="Síndrome de Down")
        eh_racacor_amarela: bool = Field(None, description="Raça/Cor amarela?")
        eh_racacor_branca: bool = Field(None, description="Raça/Cor branca?")
        eh_racacor_desconhecida: bool = Field(None, description="Raça/Cor desconhecida?")

        eh_racacor_ignorada: bool = Field(None, description="Raça/Cor ignorada?")
        eh_racacor_indigena: bool = Field(None, description="Raça/Cor indígena?")
        eh_racacor_nenhuma: bool = Field(None, description="Raça/Cor nenhuma?")
        eh_racacor_parda: bool = Field(None, description="Raça/Cor parda?")

        eh_racacor_preta: bool = Field(None, description="Raça/Cor preta?")
        eh_covid_confirmado: bool = Field(None, description="Covid confirmado?")
        eh_sexo_feminino: bool = Field(None, description="Sexo feminino?")
        eh_sexo_indefinido: bool = Field(None, description="Sexo indefinido?")
        eh_sexo_masculino: bool = Field(None, description="Sexo masculino?")
        """

        return self.predictor_model_loader.get_model().predict([[]])
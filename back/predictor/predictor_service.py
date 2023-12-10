from back.predictor.predictor_model_loader import PredictorModelLoader


class PredictorService:
    predictor_model_loader = PredictorModelLoader('../../classificador.pkl')
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
        sindrome_de_down = json_request["sindrome_de_down"]
        eh_racacor_amarela = json_request["eh_racacor_amarela"]
        eh_racacor_branca = json_request["eh_racacor_branca"]
        eh_racacor_desconhecida = json_request["eh_racacor_desconhecida"]
        eh_racacor_ignorada = json_request["eh_racacor_ignorada"]
        eh_racacor_indigena = json_request["eh_racacor_indigena"]
        eh_racacor_nenhuma = json_request["eh_racacor_nenhuma"]
        eh_racacor_parda = json_request["eh_racacor_parda"]
        eh_racacor_preta = json_request["eh_racacor_preta"]
        eh_covid_confirmado = json_request["eh_covid_confirmado"]
        eh_sexo_feminino = json_request["eh_sexo_feminino"]
        eh_sexo_indefinido = json_request["eh_sexo_indefinido"]
        eh_sexo_masculino = json_request["eh_sexo_masculino"]

        inputs = [idade, asma, cardiopatia, diabetes, doenca_hematologica, doenca_hepatica, doenca_neurologica,
                  doenca_renal, imunodepressao, obesidade, pneumopatia, puerpera, sindrome_de_down, eh_racacor_amarela,
                  eh_racacor_branca, eh_racacor_desconhecida, eh_racacor_ignorada, eh_racacor_indigena, eh_racacor_nenhuma,
                  eh_racacor_parda, eh_racacor_preta, eh_covid_confirmado, eh_sexo_feminino, eh_sexo_indefinido, eh_sexo_masculino]

        return self.predictor_model_loader.get_model().predict([inputs]).tolist()
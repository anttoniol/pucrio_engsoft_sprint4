import os

from back.loader import Loader

dir = os.path.dirname(__file__)

# Serviço para a obtenção da predição de óbito
class PredictorService:
    __pfl_file_path = os.path.join(dir, '..', '..', 'classificador.pkl')
    __model = Loader().load_model("Logistic Regression", __pfl_file_path)
    def predict(self, data):
        idade = data["idade"]
        asma = data["asma"]
        cardiopatia = data["cardiopatia"]
        diabetes = data["diabetes"]
        doenca_hematologica = data["doenca_hematologica"]
        doenca_hepatica = data["doenca_hepatica"]
        doenca_neurologica = data["doenca_neurologica"]
        doenca_renal = data["doenca_renal"]
        imunodepressao = data["imunodepressao"]
        obesidade = data["obesidade"]
        pneumopatia = data["pneumopatia"]
        puerpera = data["puerpera"]
        sindrome_de_down = data["sindrome_de_down"]
        eh_racacor_amarela = data["eh_racacor_amarela"]
        eh_racacor_branca = data["eh_racacor_branca"]
        eh_racacor_desconhecida = data["eh_racacor_desconhecida"]
        eh_racacor_ignorada = data["eh_racacor_ignorada"]
        eh_racacor_indigena = data["eh_racacor_indigena"]
        eh_racacor_nenhuma = data["eh_racacor_nenhuma"]
        eh_racacor_parda = data["eh_racacor_parda"]
        eh_racacor_preta = data["eh_racacor_preta"]
        eh_covid_confirmado = data["eh_covid_confirmado"]
        eh_sexo_feminino = data["eh_sexo_feminino"]
        eh_sexo_indefinido = data["eh_sexo_indefinido"]
        eh_sexo_masculino = data["eh_sexo_masculino"]

        input = [idade, asma, cardiopatia, diabetes, doenca_hematologica, doenca_hepatica, doenca_neurologica,
                  doenca_renal, imunodepressao, obesidade, pneumopatia, puerpera, sindrome_de_down, eh_racacor_amarela,
                  eh_racacor_branca, eh_racacor_desconhecida, eh_racacor_ignorada, eh_racacor_indigena, eh_racacor_nenhuma,
                  eh_racacor_parda, eh_racacor_preta, eh_covid_confirmado, eh_sexo_feminino, eh_sexo_indefinido, eh_sexo_masculino]

        return self.__model.get_content().predict([input]).tolist()
# Classe que representa um modelo composto por um nome e por um conteúdo de configurações do modelo
class Model:
    def __init__(self, model_name, model_content):
        self.__name = model_name
        self.__content = model_content

    def get_name(self):
        return self.__name

    def get_content(self):
        return  self.__content

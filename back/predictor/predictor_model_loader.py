import pickle


class PredictorModelLoader:
    def __init__(self, model_file):
        pickle_in = open(model_file, 'rb')
        self.__model = pickle.load(pickle_in)
        pickle_in.close()

    def get_model(self):
        return self.__model

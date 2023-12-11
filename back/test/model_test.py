from back.evaluator import Evaluator
from back.metric_comparator import MetricComparator
from back.seade_processor import SeadeProcessor
from back.test.seade_model_test_data import SeadeModelTestData

# Classe de teste de desempenho de modelos
class TestModel:
    __seade_model_test_data = SeadeModelTestData()
    __evaluator = Evaluator()
    __epsilon = 0.05

    def test_model(self):
        seade_processor = SeadeProcessor()
        dataframe = seade_processor.format_dataframe(self.__seade_model_test_data.get_dataframe())
        X, y = seade_processor.get_X_and_y(dataframe, self.__seade_model_test_data.get_target_column())
        metrics = self.__evaluator.evaluate(self.__seade_model_test_data.get_model().get_content(), X, y)
        best_metrics = self.__seade_model_test_data.get_metrics()
        assert MetricComparator().compare_metrics(best_metrics, metrics, self.__epsilon)



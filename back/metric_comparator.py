# Compara dois dicionários, em que cada par (chave, valor) contém o nome de uma métrica e o valor dela
class MetricComparator:
    def compare_metrics(self, first_metrics, second_metrics, epsilon):
        first_keys = set(list(first_metrics.keys()))
        second_keys = set(list(first_metrics.keys()))

        if first_keys != second_keys:
            return False # Não realiza a comparação caso os dois dicionários não contêm o mesmo grupo de métricas

        for key in first_keys:
            if abs(first_metrics[key] - second_metrics[key]) > epsilon:
                return False # Não continua a comparação caso seja encontrado um caso em que o epsilon é ultrapassado

        return True


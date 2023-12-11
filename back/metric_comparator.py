# Compara dois dicionários, em que cada par (chave, valor) contém o nome de uma métrica e o valor dela
class MetricComparator:
    def compare_metrics(self, first_metrics, second_metrics, epsilon):
        assert epsilon >= 0

        first_keys = set(list(first_metrics.keys()))
        second_keys = set(list(first_metrics.keys()))

        assert first_keys == second_keys # Verifica se os dois dicionários contêm o mesmo grupo de métricas

        for key in first_keys:
            assert second_metrics[key] >= first_metrics[key] - epsilon # Verifica se a diferença entre as métricas ultrapassa epsilon

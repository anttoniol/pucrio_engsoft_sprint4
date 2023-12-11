from sklearn.metrics import accuracy_score, precision_score, recall_score, jaccard_score

# Avalia o desempenho de um modelo
class Evaluator:
    def evaluate(self, model_content, X_test, y_test):
        # Fazendo as predições com o conjunto de teste
        predictions = model_content.predict(X_test)

        # Estimando valor de métricas no conjunto de teste
        metrics = dict()
        metrics["accuracy"] = accuracy_score(y_test, predictions)
        metrics["precision"] = precision_score(y_test, predictions)
        metrics["jaccard"] = jaccard_score(y_test, predictions)
        metrics["recall"] = recall_score(y_test, predictions)

        return metrics
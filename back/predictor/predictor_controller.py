import json

import flask
from flask_openapi3 import Info, Tag
from flask_openapi3 import OpenAPI

from back.predictor.base_models.predictor_body import PredictorBody
from back.predictor.predictor_service import PredictorService

info = Info(title = "Predictor API", version = "1.0.0")
app = OpenAPI(__name__, info = info)
predictor_tag = Tag(name ="prediction", description = "Some prediction")

predictor_service = PredictorService()

def format_objects(objects):
    formatted_objects = list()
    for object in objects:
        formatted_objects.append(object.__dict__())
    return formatted_objects

def create_response(body, status_code):
    headers = {
        'Access-Control-Allow-Origin': 'http://localhost:3000',
        'Access-Control-Allow-Methods': 'POST, GET, DELETE, OPTIONS',
        'Access-Control-Allow-Headers': '*'
    }
    return flask.Response(status = status_code, response = json.dumps(body),
                          headers = headers, mimetype = "application/json", content_type = "application/json")

@app.post("/predictor/", summary = "Obtain a prediction", tags = [predictor_tag])
def save_book(body: PredictorBody):
    try:
        prediction = predictor_service.predict(body.model_dump())

        body = {
            "mensagem": "Predição realizada com sucesso!",
            "predicao": prediction
        }
        return create_response(body, 200)
    except Exception as ex:
        body = {
            "mensagem": "Erro realizar predição!",
            "predicao": None
        }
        print(ex.__str__())
        return create_response(body, 500)


if __name__ == '__main__':
    app.run(host = 'localhost', port = 5000)
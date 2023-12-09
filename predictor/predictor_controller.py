import json

import flask
from flask_openapi3 import Info, Tag
from flask_openapi3 import OpenAPI

from predictor.base_models.predictor_body import PredictorBody
from predictor.predictor_service import PredictorService

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
    result = predictor_service.predict(body.dict())
    success = result[1]

    if success:
        body = {"mensagem": "Predição realizada com sucesso!"}
        return create_response(body, 200)
    body = {"mensagem": "Erro ao salvar livro!"}
    return create_response(body, 500)


if __name__ == '__main__':
    app.run(host = 'localhost', port = 5000)
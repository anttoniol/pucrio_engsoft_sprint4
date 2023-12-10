import json

import flask
from flask_openapi3 import Info, Tag
from flask_openapi3 import OpenAPI
from flask_cors import CORS


from back.predictor.base_models.predictor_body import PredictorBody
from back.predictor.predictor_service import PredictorService

info = Info(title = "Predictor API", version = "1.0.0")
app = OpenAPI(__name__, info = info)
CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "http://127.0.0.1:3000"]}})

predictor_tag = Tag(name ="prediction", description = "Some prediction")

predictor_service = PredictorService()

def format_objects(objects):
    formatted_objects = list()
    for object in objects:
        formatted_objects.append(object.__dict__())
    return formatted_objects

def create_response(body, status_code):
    return flask.Response(status = status_code, response = json.dumps(body), mimetype = "application/json", content_type = "application/json")

@app.post("/predictor/", summary = "Obtain a prediction", tags = [predictor_tag])
def predict(body: PredictorBody):
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
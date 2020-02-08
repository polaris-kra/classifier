from PIL import Image
from flask_restful import Resource, Api
from flask import jsonify, request
from core.server import ClassifierServer


server = ClassifierServer()
app = server.create()
api = Api(app)


class Classifier(Resource):
    def get(self):
        return jsonify(status='OK')

    def post(self):
        image = request.files["img"]
        image = Image.open(image)
        result = server.classify(image)

        return jsonify(result=result)


api.add_resource(Classifier, '/classify')


if __name__ == "__main__":
    server.run()

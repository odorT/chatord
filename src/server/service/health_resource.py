from flask_restful import Resource
from flask import jsonify


class Health(Resource):
    def get(self):
        return jsonify(
            status='UP'
        )

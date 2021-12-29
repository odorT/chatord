from flask_restful import Resource, reqparse
from flask import jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt

from user_model import UserModel
from util.encoder import AlchemyEncoder
from util.logz import create_logger
from settings import *

import redis
import pickle
import json


class User(Resource):
    def __init__(self):
        self.logger = create_logger()
        self.redis_server = redis.Redis(host=REDIS_HOST, password=REDIS_PASSWORD, port=REDIS_PORT)

    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('password', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('conn_details', type=str, required=True, help='This field cannot be left blank')

    def post(self):
        data = User.parser.parse_args()
        username = data['username']
        password = data['password']
        conn_details = eval(data['conn_details'])

        user = UserModel.query.filter_by(username=username).one_or_none()
        if not user or not user.check_password(password):
            return {'message': 'Wrong username or password.'}, 401

        self.redis_server.hset('conn', username, pickle.dumps(conn_details))

        access_token = create_access_token(
            identity=json.dumps(user, cls=AlchemyEncoder)
        )

        return jsonify(
            access_token=access_token
        )

    def get_clean_data_redis(self):
        clean_data = {}
        data = self.redis_server.hgetall('conn')

        for key in data.keys():
            clean_data.update({
                key.decode('utf-8'): pickle.loads(data[key])
            })

        return clean_data

    @jwt_required()
    def get(self):
        return self.get_clean_data_redis()

    @jwt_required()
    def patch(self):
        data = get_jwt()["sub"]
        username = json.loads(data)["username"]

        self.redis_server.hdel('conn', username)

        return "Successfully logged out"


class UserRegister(Resource):
    def __init__(self):
        self.logger = create_logger()

    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('password', type=str, required=True, help='This field cannot be left blank')

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': 'UserModel has already been created, aborting.'}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {'message': 'user has been created successfully.'}, 201


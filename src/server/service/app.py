from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

from user_resource import User, UserRegister
from health_resource import Health
from settings import *


app = Flask(__name__)

app.config['SECRET_KEY'] = FLASK_SECRET_KEY
app.config['JWT_SECRET_KEY'] = FLASK_SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = MYSQL_URI
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

jwt = JWTManager(app)
api = Api(app)


@app.before_first_request
def create_tables():
    from db import db
    db.init_app(app)
    db.create_all()


api.add_resource(User, f'{CONTEXT_PATH}/user')
api.add_resource(UserRegister, f'{CONTEXT_PATH}/register')
api.add_resource(Health, f'{CONTEXT_PATH}/actuator/health')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

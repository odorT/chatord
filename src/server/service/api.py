import os
import time
from flask import Flask, abort, request, jsonify, g, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
import jwt
from werkzeug.security import generate_password_hash, check_password_hash

# get environment variables
APP_VERSION = os.environ['APP_VERSION']
FLASK_SECRET_KEY = os.environ['FLASK_SECRET_KEY']
MYSQL_USER = os.environ['MYSQL_USER']
MYSQL_PASSWORD = os.environ['MYSQL_PASSWORD']
MYSQL_HOST = 'mysql-db'
MYSQL_DATABASE = os.environ['MYSQL_DATABASE']
MYSQL_URI = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}"

app = Flask(__name__)
app.config['SECRET_KEY'] = FLASK_SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = MYSQL_URI
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
auth = HTTPBasicAuth()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(128))

    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expires_in=600):
        return jwt.encode(
            payload={'id': self.id, 'exp': time.time() + expires_in},
            key=app.config['SECRET_KEY'],
            algorithm='HS256'
        )

    @staticmethod
    def verify_auth_token(token):
        try:
            data = jwt.decode(
                token,
                app.config['SECRET_KEY'],
                algorithms=['HS256']
            )
        except:
            return
        return User.query.get(data['id'])


@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


@app.route(f'/api/{APP_VERSION}/register', methods=['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400)  # missing arguments
    if User.query.filter_by(username=username).first() is not None:
        abort(400)  # existing user
    user = User(username=username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return (
        jsonify({'username': user.username}),
        201,
        {
            'Location': url_for('get_user', id=user.id, _external=True)
        }
    )


@app.route(f'/api/{APP_VERSION}/users/<int:id>')
def get_user(id):
    user = User.query.get(id)
    if not user:
        abort(400)
    return jsonify({'username': user.username})


@app.route(f'/api/{APP_VERSION}/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return jsonify({'token': token, 'duration': 600})


if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', debug=True)

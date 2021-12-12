import os


MYSQL_DATABASE = os.environ['MYSQL_DATABASE']
MYSQL_USER = os.environ['MYSQL_USER']
MYSQL_PASSWORD = os.environ['MYSQL_PASSWORD']
MYSQL_HOST = 'mysql-db'
# MYSQL_HOST = '192.168.0.1'
MYSQL_URI = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}"

FLASK_SECRET_KEY = os.environ['FLASK_SECRET_KEY']
APP_VERSION = os.environ['APP_VERSION']
CONTEXT_PATH = f'/api/{APP_VERSION}'

REDIS_HOST = 'redis'
# REDIS_HOST = '192.168.0.2'
REDIS_PORT = 6379
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']
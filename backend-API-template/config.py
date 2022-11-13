import os
import logging
from os.path import join, dirname

from dotenv import load_dotenv
from flask import Flask

# load .env
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class BaseConfig(object):

    def __init__(self, app: Flask):
        self.init_app(app)

    @classmethod
    def init_app(cls, app: Flask):
        app.config.from_object(cls)

    # # LOGGER
    LOGGING_PATH = '../logs'

    # MYSQL
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'db host')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'db user')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'db password')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'db database')
    MYSQL_POOL_SIZE = int(os.environ.get('MYSQL_POOL_SIZE', 5))
    # JWT
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', '')
    PROPAGATE_EXCEPTIONS = True  # This line will return a nice error message when something goes wrong

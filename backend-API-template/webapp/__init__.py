import os
import logging
from logging.handlers import TimedRotatingFileHandler

from flask import Flask
from flask_cors import CORS
from flask_compress import Compress
from flask_jwt_extended import JWTManager
import config
from common_lib.infra.mysql import DB


def create_app():
    app = Flask(__name__,
                static_folder="static/",
                static_url_path="/static",
                template_folder="static")

    config.BaseConfig.init_app(app)
    DB.init_app(app)
    log_configure(app)
    register_blueprints(app)

    CORS(app)
    Compress(app)
    JWTManager(app)

    return app


def register_blueprints(app: Flask) -> None:
    from webapp.users.routes import user_api
    from webapp.post.routes import post_api

    apis = [user_api, post_api]

    for _api in apis:
        app.register_blueprint(_api.blueprint)


def log_configure(app: Flask):
    log_level = app.config.get('LOGGING_LEVEL', logging.INFO)
    logging.root.setLevel(log_level)

    # turn off werkzeug log
    # werkzeug_logger = logging.getLogger('werkzeug')
    # werkzeug_logger.setLevel(logging.ERROR)

    def configure_basic_logger(app: Flask):
        logger = logging.getLogger(app.import_name)

        log_format = app.config.get('LOGGING_FORMAT', '')
        date_format = app.config.get('LOGGING_DATE_FORMAT', '')

        log_file_dir = os.path.join(app.root_path, app.config.get('LOGGING_PATH', ''))
        log_file_path = os.path.join(log_file_dir, 'app.log')
        if not os.path.exists(log_file_dir):
            os.mkdir(log_file_dir)
        file_handler = TimedRotatingFileHandler(log_file_path, when='W0', backupCount=4)
        file_handler.setFormatter(logging.Formatter(fmt=log_format, datefmt=date_format))
        logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(logging.Formatter(fmt=log_format, datefmt=date_format))
        logger.addHandler(stream_handler)

    def configure_access_logger(app: Flask):
        logger = logging.getLogger('ACCESS')

        access_log_format = app.config.get('ACCESS_LOGGING_FORMAT', '')
        date_format = app.config.get('LOGGING_DATE_FORMAT', '')

        log_file_dir = os.path.join(app.root_path, app.config.get('LOGGING_PATH', ''))
        log_file_path = os.path.join(log_file_dir, 'access.log')
        if not os.path.exists(log_file_dir):
            os.mkdir(log_file_dir)

        file_handler = TimedRotatingFileHandler(log_file_path, when='W0', backupCount=4)
        file_handler.setFormatter(logging.Formatter(fmt=access_log_format, datefmt=date_format))
        logger.addHandler(file_handler)

    configure_basic_logger(app)
    configure_access_logger(app)

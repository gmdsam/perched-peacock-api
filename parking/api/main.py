import logging
import os
import sys
from logging.handlers import TimedRotatingFileHandler
from flask import Flask
from flask_cors import CORS
from flask_injector import FlaskInjector
from injector import singleton, Provider

from parking.api.config.loader import load_config_from_json
from parking.api.namespace import api
from parking.core.db.database import Database
from parking.core.services.parking_service import ParkingService

app = Flask(__name__)
CORS(app)


def configure_injector(config, binder):

    class _ParkingServiceProvider(Provider):
        def get(self, injector):
            return ParkingService(injector.get(Database).handshake(config['DB_URL']))

    binder.bind(
        Database,
        to=Database(),
        scope=singleton
    )
    binder.bind(
        ParkingService,
        to=_ParkingServiceProvider(),
        scope=singleton
    )


def configure_app(_app):
    LOGGING_FORMAT = '%(asctime)-15s %(name)-15s %(levelname)-8s %(message)s'
    console_handler = logging.StreamHandler(stream=sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter(fmt=LOGGING_FORMAT, datefmt='%Y-%m-%dT%H:%M:%S'))
    logging.getLogger().handlers = []
    logging.getLogger().addHandler(console_handler)
    logging.getLogger().setLevel(logging.INFO)
    _app.logger.handlers = []
    _app.logger.propagate = True
    logging.getLogger().info('Configure new Flask App')

    api.init_app(_app)

    _app = load_config_from_json(_app)

    # activate = True if os.environ['PP_AUTH'] == '1' else False

    if _app.config['LOG_PATH'] is not None:
        file_handler = TimedRotatingFileHandler(
            os.path.join(_app.config['LOG_PATH'], 'log_api.txt'),
            when='d',
            interval=1,
            backupCount=30
        )
        file_handler.setFormatter(logging.Formatter(fmt=LOGGING_FORMAT, datefmt='%Y-%m-%dT%H:%M:%S'))
        file_handler.setLevel(logging.INFO)
        logging.getLogger().addHandler(file_handler)

    def _injector_module(binder):
        configure_injector(_app.config, binder)

    injector = FlaskInjector(app=_app, modules=[_injector_module])

    # Initialize Database
    injector.injector.get(Database)


if __name__ == '__main__':
    apiapp = app
    configure_app(app)
    logging.getLogger().info('Application configured, starting on port {}'.format(app.config['PORT']))
    apiapp.run(host=app.config['HOST'], debug=app.config['DEBUG'], port=app.config['PORT'])

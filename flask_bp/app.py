import logging
from flask import Flask
from extensions.Configuration import load_endpoints, load_extensions


def minimal_app():
    app = Flask("api_com_bp")
    return app


def log():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)-4s %(message)s',
                        datefmt='flask_bp.log',
                        filemode='a')

def create_app():
    app = minimal_app()
    log()
    load_extensions(app)
    load_endpoints(app)
    return app

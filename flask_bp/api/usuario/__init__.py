import logging
from flask_restful import Api
from flask import Blueprint
from api.usuario.Resources import Usuarios 


bp = Blueprint("usuario", __name__, url_prefix='/api/v1')
api = Api(bp)
api.add_resource(Usuarios, '/usuarios')


def init_app(app):
    try:
        app.register_blueprint(bp)
    except Exception as e:
        print(f"ERRO: erro no init_app(): {e}")
        logging.info(f"ERRO: erro no init_app(): {e}")

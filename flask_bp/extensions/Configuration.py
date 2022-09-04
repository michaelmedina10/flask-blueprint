import logging


def load_extensions(app):
    from extensions import(
        GeralConfig,
        Documentation)
    GeralConfig.init_app(app)
    Documentation.init_app(app)


def load_endpoints(app):
    try:
        from api import (
            usuario
        )
        usuario.init_app(app)
        
    except Exception as e:
        logging.info("ERRO: Não foi possível carregar os endpoints")

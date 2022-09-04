from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = "/api-docs"
SWAGGER_FILE = "/static/swagger/main.yaml"


def init_app(app):
    swagger_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        SWAGGER_FILE,
        config={"app_name": "API com flask e blueprint"}
    )
    app.register_blueprint(
        swagger_blueprint,
        url_prefix=SWAGGER_URL
    )

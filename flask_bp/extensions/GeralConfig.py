def init_app(app):
    app.config.update(
        SESSION_COOKIE_SECURE=True,
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE='Lax',
        SESSION_COOKIE_DOMAIN='com.br',
        JSON_AS_ASCII=True,
        JSON_SORT_KEYS=False,
        JSONIFY_PRETTYPRINT_REGULAR=False,
        PERMANENT_SESSION_LIFETIME=0,
        SEND_FILE_MAX_AGE_DEFAULT=0
    )
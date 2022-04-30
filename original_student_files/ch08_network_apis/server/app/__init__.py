from flask import Flask


def create_app():
    app = Flask(__name__)

    with app.app_context():
        from . import routes      # import routes while we are in the context of the current app
    return app

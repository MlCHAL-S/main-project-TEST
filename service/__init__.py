from service import config
from flask import Flask
from .extensions import db
from .routes import main


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.DevelopmentConfig)

    db.init_app(app)

    app.register_blueprint(main)
    return app

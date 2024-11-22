from service.config import config_by_name
from flask import Flask
from .extensions import db, talisman, cors
from .routes import main


def create_app(config_name='development'):

    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    db.init_app(app)
    talisman.init_app(app)
    cors.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(main)
    return app

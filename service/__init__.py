from flask import Flask
from service import config

# init app
app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)

from service import routes, models

# init db
models.init_db(app)

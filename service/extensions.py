from flask_sqlalchemy import SQLAlchemy
import redis
from flask_talisman import Talisman
from flask_cors import CORS

db = SQLAlchemy()
redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)
talisman = Talisman()
cors = CORS()

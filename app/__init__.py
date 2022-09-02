from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.utils.config import USER,PASSWORD,DATABASE_NAME,HOST
from app.routes.users import users
from app.routes.bill import bills
from flask_marshmallow import Marshmallow
from decouple import config as config_decouple
from decouple import config 

db= SQLAlchemy()
ma = Marshmallow()

def create_app(enviroment):
    app = Flask(__name__)

    app.config.from_object(enviroment)

    db = SQLAlchemy(app)
    ma = Marshmallow(app)
    ma.init_app(app)
    app.register_blueprint(users)
    app.register_blueprint(bills)

    with app.app_context():
        db.init_app(app)
    return app


enviroment = config['development']
if config_decouple('PRODUCTION', default=False):
    enviroment = config['production']

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.utils.config import USER,PASSWORD,DATABASE_NAME,HOST
from app.routes.users import users
from app.routes.bill import bills
from flask_marshmallow import Marshmallow

db= SQLAlchemy()
ma = Marshmallow()

def create_app(config_file="utils/config.py"):
    app = Flask(__name__)
    db = SQLAlchemy(app)
    ma = Marshmallow(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{USER}:{PASSWORD}@{HOST}:5432/{DATABASE_NAME}"
    app.config.from_pyfile(config_file)
    app.register_blueprint(users)
    app.register_blueprint(bills)
    db.init_app(app)
    ma.init_app(app)

    return app
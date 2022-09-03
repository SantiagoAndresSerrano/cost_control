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
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://postgres:Prisma2022@prismatest.cr5kiddvokid.us-east-2.rds.amazonaws.com:5432/test"
    app.config.from_pyfile(config_file)
    app.register_blueprint(users)
    app.register_blueprint(bills)
    db.init_app(app)
    ma.init_app(app)

    return app
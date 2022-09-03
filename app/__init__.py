from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.utils.config import USER,PASSWORD,DATABASE_NAME,HOST
from app.routes.users import users
from app.routes.bill import bills
from flask_marshmallow import Marshmallow



from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

db= SQLAlchemy()
ma = Marshmallow()

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)

def create_app(config_file="utils/config.py"):
    app = Flask(__name__)
    db = SQLAlchemy(app)
    ma = Marshmallow(app)
    ma.init_app(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:Prisma2022@prismatest.cr5kiddvokid.us-east-2.rds.amazonaws.com:5432/test"
    app.config.from_pyfile(config_file)
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
    app.register_blueprint(users)
    app.register_blueprint(bills)
    db.init_app(app)

    return app
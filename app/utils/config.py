from dotenv import load_dotenv
import os
from decouple import config

load_dotenv()

USER = os.getenv("POSTGRESQL_USERNAME")
PASSWORD = os.getenv("POSTGRESQL_PASSWORD")
DATABASE_NAME = os.getenv("POSTGRESQL_DATABASE")
HOST = os.getenv("HOST")


class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"postgresql://{USER}:{PASSWORD}@{HOST}:5432/{DATABASE_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URL', default='localhost')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
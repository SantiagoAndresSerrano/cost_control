from dotenv import load_dotenv
import os
from decouple import config

load_dotenv()

USER = os.getenv("POSTGRESQL_USERNAME")
PASSWORD = os.getenv("POSTGRESQL_PASSWORD")
DATABASE_NAME = os.getenv("POSTGRESQL_DATABASE")
HOST = os.getenv("HOST")

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Prisma2022@prismatest.cr5kiddvokid.us-east-2.rds.amazonaws.com:5432/test"
    SQLALCHEMY_TRACK_MODIFICATIONS = False



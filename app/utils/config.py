from dotenv import load_dotenv
import os
from decouple import config

load_dotenv()

USER = os.getenv("POSTGRESQL_USERNAME")
PASSWORD = os.getenv("POSTGRESQL_PASSWORD")
DATABASE_NAME = os.getenv("POSTGRESQL_DATABASE")
HOST = os.getenv("HOST")


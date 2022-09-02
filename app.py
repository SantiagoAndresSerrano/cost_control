from flask import Flask
app = Flask(__name__)
from app.utils.config import USER,PASSWORD,DATABASE_NAME,HOST

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{USER}:{PASSWORD}@{HOST}:5432/{DATABASE_NAME}"

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from helpers.constants.database import SQLITE_DB

db = SQLAlchemy()
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLITE_DB

db.init_app(app)

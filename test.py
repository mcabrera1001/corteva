from config.flask_and_database import db, app
from models import *

with app.app_context():
    db.create_all()
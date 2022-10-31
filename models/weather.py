from config.flask_and_database import db

class Weather(db.Model):
    active = db.Column(db.Boolean, default=True) # for soft delete functionality.
    date = db.Column(db.String(8), unique=True)
    station = db.Column(db.String(11))
    min_temperature = db.Column(db.Float, nullable=True)
    max_temperature = db.Column(db.Float, nullable=True)
    precipitation = db.Column(db.Float, nullable=True)

with db.app_context():
    db.create_all()
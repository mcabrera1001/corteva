from config.flask_and_database import db
from helpers.constants import (
    STATION,
    DATE,
    MAX_TEMPERATURE,
    MIN_TEMPERATURE,
    PRECIPITATION,
)
from sqlalchemy_serializer import SerializerMixin

class Weather(db.Model, SerializerMixin):
    serialize_only = (DATE, STATION, MIN_TEMPERATURE, MAX_TEMPERATURE, PRECIPITATION,)

    active = db.Column(db.Boolean, default=True)  # for soft delete functionality.
    date = db.Column(db.String(8), primary_key=True)
    station = db.Column(db.String(11), primary_key=True)
    min_temperature = db.Column(db.Float)
    max_temperature = db.Column(db.Float)
    precipitation = db.Column(db.Float)

    def __init__(self, date, station, min_temperature, max_temperature, precipitation):
        self.date = date
        self.station = station
        self.min_temperature = min_temperature
        self.max_temperature = max_temperature
        self.precipitation = precipitation

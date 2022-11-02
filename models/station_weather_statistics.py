from config.flask_and_database import db
from helpers.constants import (
    STATION,
    YEAR,
    AVERAGE_MIN_TEMPERATURE,
    AVERAGE_MAX_TEMPERATURE,
    TOTAL_PRECIPITATION,
)
from sqlalchemy_serializer import SerializerMixin


class StationWeatherSummary(db.Model, SerializerMixin):
    serialize_only = (
        YEAR,
        STATION,
        AVERAGE_MIN_TEMPERATURE,
        AVERAGE_MAX_TEMPERATURE,
        TOTAL_PRECIPITATION,
    )

    active = db.Column(db.Boolean, default=True)  # for soft delete functionality.
    year = db.Column(db.Integer, primary_key=True)
    station = db.Column(db.String(11), primary_key=True)
    average_min_temperature = db.Column(db.Float)
    average_max_temperature = db.Column(db.Float)
    total_precipitation = db.Column(db.Float)

    def __init__(
        self,
        year,
        station,
        average_min_temperature,
        average_max_temperature,
        total_precipitation,
    ):
        self.year = year
        self.station = station
        self.average_min_temperature = average_min_temperature
        self.average_max_temperature = average_max_temperature
        self.total_precipitation = total_precipitation

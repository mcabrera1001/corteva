from config.flask_and_database import db
from helpers.constants import (
    YEAR,
    CROP_YIELD_1000_MEGATONS,
    CROP,
)
from sqlalchemy_serializer import SerializerMixin

class CropYield(db.Model, SerializerMixin):
    """notice there is no direct mention of corn here. I want this model to extend to any crop"""
    serialize_only = (YEAR, CROP, CROP_YIELD_1000_MEGATONS,)

    active = db.Column(db.Boolean, default=True)  # for soft delete functionality.
    year = db.Column(db.Integer, primary_key=True)
    crop = db.Column(db.String(10))
    crop_yield_1000_megatons = db.Column(
        db.Integer
    )  # specifying the unit in the title helps a lot when database info is lost.

    def __init__(self, year, crop, crop_yield_1000_megatons):
        self.year = year
        self.crop = crop
        self.crop_yield_1000_megatons = crop_yield_1000_megatons

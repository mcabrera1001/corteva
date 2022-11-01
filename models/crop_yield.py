from config.flask_and_database import db

class CropYield(db.Model):
    ''' notice there is no direct mention of corn here. I want this model to extend to any crop '''
    active = db.Column(db.Boolean, default=True) # for soft delete functionality.
    year = db.Column(db.Integer, primary_key=True)
    crop = db.Column(db.String(10))
    # specifying the unit in the title helps a lot when database info is lost.
    crop_yield_1000_megatons = db.Column(db.Integer, nullable=False)

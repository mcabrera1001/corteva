from models import CropYield, Weather
from helpers.constants import YEAR, PAGE, PER_PAGE

crop_yield = [
    CropYield(
        year=1985,
        crop="corn",
        crop_yield_1000_megatons=9999,
    )
]

weather = [
    Weather(
        date=1985,
        station="USC00110072",
        min_temperature=1,
        max_temperature=32,
        precipitation=5,
    )
]

get_crop_yield_data_by_year_args = {YEAR: 1985, PAGE: 1, PER_PAGE: 15}

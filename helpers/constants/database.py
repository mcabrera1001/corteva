SQLITE_DB = "sqlite:///weather.db"

# Weather model
STATION = "station"
DATE = "date"
MAX_TEMPERATURE = "max_temperature"
MIN_TEMPERATURE = "min_temperature"
PRECIPITATION = "precipitation"
WEATHER_MODEL_COLUMNS_IN_ORDER = [
    DATE,
    MAX_TEMPERATURE,
    MIN_TEMPERATURE,
    PRECIPITATION,
    STATION,
]

# Crop Yield Model
YEAR = "year"
CROP = "crop"
CROP_YIELD_1000_MEGATONS = "crop_yield_1000_megatons"
CROP_YIELD_MODEL_COLUMNS_IN_ORDER = [YEAR, CROP_YIELD_1000_MEGATONS, CROP]

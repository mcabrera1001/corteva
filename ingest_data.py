import pandas as pd
from helpers.constants import WEATHER_DATA_FOLDER, WEATHER_MODEL_COLUMNS_IN_ORDER
import os
from helpers.decorators import time_process


@time_process
def ingest_weather_station_data(weather_station_dir):
    station_data = pd.read_csv(weather_station_dir, sep="\t", names=WEATHER_MODEL_COLUMNS_IN_ORDER)
    print(station_data)


# WEATHER_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), WEATHER_DATA_FOLDER)

if __name__ == "__main__":
    ingest_weather_station_data(os.path.join(WEATHER_DATA_FOLDER, 'USC00110072.txt'))
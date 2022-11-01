import pandas as pd
from helpers.constants import (
    WEATHER_DATA_FOLDER,
    WEATHER_MODEL_COLUMNS_IN_ORDER,
    STATION,
    DATE,
    MAX_TEMPERATURE,
    MIN_TEMPERATURE,
    PRECIPITATION,
)
from models import Weather
import os
from helpers.decorators import time_process
from config.flask_and_database import db, app
from multiprocessing.pool import Pool


def covert_txt_to_dataframe(weather_station_dir):
    station_name = os.path.split(weather_station_dir)[1].replace(".txt", "")
    station_data = pd.read_csv(
        weather_station_dir, sep="\t", names=WEATHER_MODEL_COLUMNS_IN_ORDER
    )
    station_data[STATION] = station_name
    return station_data


def add_dataframe_row_to_db(dataframe_row):
    print(dataframe_row)
    try:
        weather = Weather(
            date=str(dataframe_row[DATE]),
            station=dataframe_row[STATION],
            min_temperature=dataframe_row[MIN_TEMPERATURE],
            max_temperature=dataframe_row[MAX_TEMPERATURE],
            precipitation=dataframe_row[PRECIPITATION],
        )
        with app.app_context():
            db.session.add(weather)
            db.session.commit()
    except Exception as error:
        return f"Could not process data for the following date: {weather.date} due to {error}", 1
        # return error, 1

@time_process
def ingest_data_for_one_station(station_file):
    # df_data = covert_txt_to_dataframe(os.path.join(WEATHER_DATA_FOLDER, station_file))
    # result = [add_dataframe_row_to_db(row) for row in df_data.to_dict(orient='records')]
    # print(result)

    with Pool() as pool:
        df_data = covert_txt_to_dataframe(os.path.join(WEATHER_DATA_FOLDER, station_file))
        ingestion_result = pool.map(add_dataframe_row_to_db, df_data.to_dict(orient='records'))
        # print(ingestion_result)

if __name__ == "__main__":
    ingest_data_for_one_station("USC00110072.txt")

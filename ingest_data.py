import pandas as pd
from helpers.constants import (
    WEATHER_DATA_FOLDER,
    CROP_DATA_FOLDER,
    WEATHER_MODEL_COLUMNS_IN_ORDER,
    CROP_YIELD_MODEL_COLUMNS_IN_ORDER,
    STATION,
    DATE,
    MAX_TEMPERATURE,
    MIN_TEMPERATURE,
    PRECIPITATION,
    YEAR,
    CROP_YIELD_1000_MEGATONS,
    CROP,
)
from models import Weather, CropYield
import os
from helpers.decorators import time_process
from config.flask_and_database import db, app
from multiprocessing.pool import Pool
import logging
import sys

logging.basicConfig(filename='logs/ingest.log', encoding='utf-8')

def add_object_to_db(model_object):
    with app.app_context():
        db.session.add(model_object)
        db.session.commit()

def process_ingestion_results(ingestion_results):
    ingested_amount = len([result for result in ingestion_results if not result])
    logging.info(f'Successfully ingested a total of {ingested_amount} out of {len(ingestion_results)} records.')
    logging.warning(f'Could not ingest a total of {len(ingestion_results) - ingested_amount}.')

def covert_station_data_to_dataframe(weather_station_dir):
        station_name = os.path.split(weather_station_dir)[1].replace(".txt", "")
        station_data = pd.read_csv(
            weather_station_dir, sep="\t", names=WEATHER_MODEL_COLUMNS_IN_ORDER, na_values=['-9999']
        )
        station_data[STATION] = station_name
        return station_data.to_dict(orient='records')

def covert_crop_yield_to_dataframe(crop_yield_dir):
    """ Why didn't I just combine this function with covert_station_data_to_dataframe?
        As the data changes these two functions might do end up doing completely different things.
        I'll rather have two functions than one function with many if statements and nested logic """
    crop_name = os.path.split(crop_yield_dir)[1].replace(".txt", "").split('_')[1]
    crop_data = pd.read_csv(
            crop_yield_dir, sep="\t", names=CROP_YIELD_MODEL_COLUMNS_IN_ORDER, na_values=['-9999']
        )
    crop_data[CROP] = crop_name
    return crop_data.to_dict(orient='records')


def add_weather_row_to_db(dataframe_row):
    print(dataframe_row)
    try:
        weather = Weather(
            date=str(dataframe_row[DATE]),
            station=dataframe_row[STATION],
            min_temperature=dataframe_row[MIN_TEMPERATURE],
            max_temperature=dataframe_row[MAX_TEMPERATURE],
            precipitation=dataframe_row[PRECIPITATION],
        )
        add_object_to_db(weather)
    except Exception as error:
        logging.error(f"Could not process weather data for the following date: {weather.date} due to {error}")
        return 1

def add_crop_row_to_db(dataframe_row):
    print(dataframe_row)
    try:
        crop_yield = CropYield(
            year=dataframe_row[YEAR], crop=dataframe_row[CROP], crop_yield_1000_megatons=dataframe_row[CROP_YIELD_1000_MEGATONS]
        )
        add_object_to_db(crop_yield)
    except Exception as error:
        logging.error(f"Could not process crop data for the following year: {crop_yield.year} due to {error}")
        return 1

@time_process
def ingest_data_for_one_station(station_file):
    df_data = covert_station_data_to_dataframe(os.path.join(WEATHER_DATA_FOLDER, station_file))
    # kept reaching the concurrency limit of sqlite so I kept it at Pool(4).
    with Pool(4) as pool:
        ingestion_results = pool.map(add_weather_row_to_db, df_data)
        process_ingestion_results(ingestion_results)

@time_process
def ingest_data_for_one_crop(crop_file):
    crop_data = covert_crop_yield_to_dataframe(os.path.join(CROP_DATA_FOLDER, crop_file))
    # kept reaching the concurrency limit of sqlite so I kept it at Pool(4).
    with Pool(4) as pool:
        ingestion_results = pool.map(add_crop_row_to_db, crop_data)
        process_ingestion_results(ingestion_results)


if __name__ == "__main__":
    weather_file_name = sys.argv[1]
    crop_file_name = sys.argv[2]
    ingest_data_for_one_station(weather_file_name)
    ingest_data_for_one_crop(crop_file_name)

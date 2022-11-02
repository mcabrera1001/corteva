from config.flask_and_database import db, app
import pandas as pd
from models import Weather, CropYield, StationWeatherSummary
from sqlalchemy.sql import func
from helpers.constants import (
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
import logging
import os


def add_object_to_db(model_object):
    with app.app_context():
        db.session.add(model_object)
        db.session.commit()


def process_ingestion_results(ingestion_results):
    ingested_amount = len([result for result in ingestion_results if not result])
    logging.info(
        f"Successfully ingested a total of {ingested_amount} out of {len(ingestion_results)} records."
    )


def generate_list_of_files(directory):
    data_files = os.listdir(directory)
    return data_files


def covert_station_data_to_dataframe(weather_station_dir):
    station_name = os.path.split(weather_station_dir)[1].replace(".txt", "")
    station_data = pd.read_csv(
        weather_station_dir,
        sep="\t",
        names=WEATHER_MODEL_COLUMNS_IN_ORDER,
        na_values=["-9999"],
    )
    station_data[STATION] = station_name
    station_data = station_data[:10]
    return station_data


def covert_crop_yield_to_dataframe(crop_yield_dir):
    """Why didn't I just combine this function with covert_station_data_to_dataframe?
    As the data changes these two functions might do end up doing completely different things.
    I'll rather have two functions than one function with many if statements and nested logic"""
    crop_name = os.path.split(crop_yield_dir)[1].replace(".txt", "").split("_")[1]
    crop_data = pd.read_csv(
        crop_yield_dir,
        sep="\t",
        names=CROP_YIELD_MODEL_COLUMNS_IN_ORDER,
        na_values=["-9999"],
    )
    crop_data[CROP] = crop_name
    return crop_data.to_dict(orient="records")


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
        logging.error(
            f"Could not process weather data for the following date: {weather.date} due to {error}"
        )
        return 1


def add_crop_row_to_db(dataframe_row):
    print(dataframe_row)
    try:
        crop_yield = CropYield(
            year=dataframe_row[YEAR],
            crop=dataframe_row[CROP],
            crop_yield_1000_megatons=dataframe_row[CROP_YIELD_1000_MEGATONS],
        )
        add_object_to_db(crop_yield)
    except Exception as error:
        logging.error(
            f"Could not process crop data for the following year: {crop_yield.year} due to {error}"
        )
        return 1


def calculate_weather_stats(year, station):
    with app.app_context():
        query = db.session.query(
            func.avg(Weather.max_temperature) / 10,
            func.avg(Weather.min_temperature) / 10,
            func.sum(Weather.precipitation) / 10,
        )
        filter_by_station_and_year = query.filter(
            Weather.date.ilike(f"%{year}%"), Weather.station == station
        ).all()[0]
        if any(filter_by_station_and_year):
            try:
                weather_summary = StationWeatherSummary(
                    year=year,
                    station=station,
                    average_min_temperature=filter_by_station_and_year[1],
                    average_max_temperature=filter_by_station_and_year[0],
                    total_precipitation=filter_by_station_and_year[2],
                )

                print(weather_summary.to_dict())
                add_object_to_db(weather_summary)
            except Exception as error:
                logging.error(
                    f"Could not add data for {station} for year: {year} due to {error}"
                )
                return 1
        return logging.warn(f"No data for {station} for year: {year}")

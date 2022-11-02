from helpers.constants import (
    WEATHER_DATA_FOLDER,
    CROP_DATA_FOLDER,
    STATION,
    DATE,
)
import os
from helpers.decorators import time_process
from helpers.ingest_data_helpers import (
    process_ingestion_results,
    generate_list_of_files,
    covert_station_data_to_dataframe,
    add_weather_row_to_db,
    covert_crop_yield_to_dataframe,
    add_crop_row_to_db,
    calculate_weather_stats,
)
from multiprocessing.pool import Pool
import logging

logging.basicConfig(
    filename="logs/ingest.log",
    format="%(asctime)s %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    filemode="w",
    encoding="utf-8",
    level=logging.DEBUG,
)


@time_process
def ingest_data_for_one_station(df_data):
    with Pool(4) as pool:
        ingestion_results = pool.map(add_weather_row_to_db, df_data)
        process_ingestion_results(ingestion_results)


@time_process
def ingest_data_for_one_crop(crop_file):
    crop_data = covert_crop_yield_to_dataframe(
        os.path.join(CROP_DATA_FOLDER, crop_file)
    )
    # kept reaching the concurrency limit of sqlite so I kept it at Pool(4).
    with Pool(4) as pool:
        ingestion_results = pool.map(add_crop_row_to_db, crop_data)
        process_ingestion_results(ingestion_results)


@time_process
def ingest_statistics_for_one_station(df_data):
    years = df_data[DATE].astype(str).str[:4].unique()
    station = df_data[STATION].unique()[0]
    with Pool(4) as pool:
        ingestion_results = pool.starmap(
            calculate_weather_stats, [(year, station) for year in years]
        )
        process_ingestion_results(ingestion_results)


if __name__ == "__main__":
    weather_file_names = generate_list_of_files(WEATHER_DATA_FOLDER)
    for weather_file in weather_file_names:
        df_data = covert_station_data_to_dataframe(
            os.path.join(WEATHER_DATA_FOLDER, weather_file)
        )
        ingest_data_for_one_station(df_data.to_dict(orient="records"))
        ingest_statistics_for_one_station(df_data)
    crop_file_names = generate_list_of_files(CROP_DATA_FOLDER)
    for crop_file in crop_file_names:
        ingest_data_for_one_crop(crop_file)

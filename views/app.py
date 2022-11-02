import logging

from flask import Flask, request

from config.flask_and_database import app, db
from controllers.app_controllers import (
    get_crop_yield_data_by_year,
    get_weather_data_by_station_and_date,
    get_weather_statistics,
)

logging.basicConfig(
    filename="logs/api.log", filemode="w", encoding="utf-8", level=logging.DEBUG
)


@app.route("/api/weather", methods=["GET"])
def get_weather():
    query_results = get_weather_data_by_station_and_date(request.args)
    results = [result.to_dict() for result in query_results]
    return results


@app.route("/api/yield", methods=["GET"])
def get_crop_yield():
    query_results = get_crop_yield_data_by_year(request.args)
    results = [result.to_dict() for result in query_results]
    return results


@app.route("/api/weather/stats", methods=["GET"])
def get_weather_stats():
    query_results = get_weather_statistics(request.args)
    results = [result.to_dict() for result in query_results]
    return results


if __name__ == "__main__":
    app.run(debug=True)

from flask import jsonify, Flask, request
from models import Weather
import logging
from controllers.app_controllers import get_weather_data_by_station_and_date

logging.basicConfig(filename="logs/api.log", filemode="w", encoding="utf-8", level=logging.DEBUG)

from config.flask_and_database import db, app


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/api/weather", methods=["GET"])
def get_weather():
    # query = Weather.query.first()
    # return query.to_dict()
    query_results = get_weather_data_by_station_and_date(request.args)
    results = [result.to_dict() for result in query_results]
    return results


if __name__ == "__main__":
    app.run(debug=True)

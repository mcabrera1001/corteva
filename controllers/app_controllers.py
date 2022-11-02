from models import Weather
from helpers.api_request_parsers import build_filter_params


def get_weather_data_by_station_and_date(args):
    filter_by = build_filter_params(args)
    weather_list = Weather.query.filter_by(**filter_by)
    return weather_list
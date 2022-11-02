from models import Weather, CropYield, StationWeatherSummary
from helpers.api_request_parsers import (
    build_weather_filter_params,
    get_pagination_settings,
    buil_crop_yield_filter_params,
    build_weather_statistics_filter_params,
)


def get_weather_data_by_station_and_date(args):
    filter_by = build_weather_filter_params(args)
    page, per_page = get_pagination_settings(args)
    weather_list = Weather.query.filter_by(**filter_by).paginate(
        page=page, per_page=per_page
    )
    return weather_list


def get_crop_yield_data_by_year(args):
    filter_by = buil_crop_yield_filter_params(args)
    page, per_page = get_pagination_settings(args)
    crop_yield_list = CropYield.query.filter_by(**filter_by).paginate(
        page=page, per_page=per_page
    )
    return crop_yield_list


def get_weather_statistics(args):
    filter_by = build_weather_statistics_filter_params(args)
    page, per_page = get_pagination_settings(args)
    station_weather_list = StationWeatherSummary.query.filter_by(**filter_by).paginate(
        page=page, per_page=per_page
    )
    return station_weather_list

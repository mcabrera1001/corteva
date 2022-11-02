from helpers.constants import (
    STATION,
    DATE,
    DEFAULT_PAGE,
    TOTAL_PER_PAGE,
    PAGE,
    PER_PAGE,
    YEAR,
)


def build_weather_filter_params(args):
    query_str_dict = {DATE: args.get(DATE), STATION: args.get(STATION)}
    return {key: value for key, value in query_str_dict.items() if value}


def buil_crop_yield_filter_params(args):
    query_str_dict = {YEAR: args.get(YEAR)}
    return {key: value for key, value in query_str_dict.items() if value}


def build_weather_statistics_filter_params(args):
    query_str_dict = {YEAR: args.get(YEAR), STATION: args.get(STATION)}
    return {key: value for key, value in query_str_dict.items() if value}


def get_pagination_settings(args):
    page = int(page) if (page := args.get(PAGE)) else DEFAULT_PAGE
    rows_per_page = (
        int(total)
        if (total := args.get(PER_PAGE)) and int(total) < 100
        else TOTAL_PER_PAGE
    )
    return page, rows_per_page

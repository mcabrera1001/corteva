from helpers.constants import (
    STATION,
    DATE,
)


def build_filter_params(args):
    query_str_dict = {DATE: args.get(DATE), STATION: args.get(STATION)}
    return {key: value for key, value in query_str_dict.items() if value}

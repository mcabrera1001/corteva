import unittest
from unittest.mock import patch
from tests.controllers.controller_helpers import (
    weather,
    get_crop_yield_data_by_year_args,
)
from controllers.app_controllers import get_weather_data_by_station_and_date


class TestGetWeatherDataByStationAndDate(unittest.TestCase):
    @patch("controllers.app_controllers.Weather")
    def test_crop_yield_data_has_correct_length(self, mock_weather):
        mock_weather.query.filter_by().paginate.return_value = weather
        crop_yield_list = get_weather_data_by_station_and_date(
            get_crop_yield_data_by_year_args
        )
        self.assertEqual(len(crop_yield_list), len(weather))

    @patch("controllers.app_controllers.Weather")
    def test_yield_data_contains_expected_fields(self, mock_crop_yield):
        mock_crop_yield.query.filter_by().paginate.return_value = weather
        crop_yield_list = get_weather_data_by_station_and_date(
            get_crop_yield_data_by_year_args
        )
        self.assertEqual(
            crop_yield_list[0].to_dict().keys(), weather[0].to_dict().keys()
        )


if __name__ == "__main__":
    unittest.main()

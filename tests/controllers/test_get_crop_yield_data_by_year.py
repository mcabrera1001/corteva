import unittest
from unittest.mock import patch
from tests.controllers.controller_helpers import (
    crop_yield,
    get_crop_yield_data_by_year_args,
)
from controllers.app_controllers import get_crop_yield_data_by_year


class TestGetCropYieldDataByYear(unittest.TestCase):
    @patch("controllers.app_controllers.CropYield")
    def test_crop_yield_data_has_correct_length(self, mock_crop_yield):
        mock_crop_yield.query.filter_by().paginate.return_value = crop_yield
        crop_yield_list = get_crop_yield_data_by_year(get_crop_yield_data_by_year_args)
        self.assertEqual(len(crop_yield_list), len(crop_yield))

    @patch("controllers.app_controllers.CropYield")
    def test_yield_data_contains_expected_fields(self, mock_crop_yield):
        mock_crop_yield.query.filter_by().paginate.return_value = crop_yield
        crop_yield_list = get_crop_yield_data_by_year(get_crop_yield_data_by_year_args)
        self.assertEqual(
            crop_yield_list[0].to_dict().keys(), crop_yield[0].to_dict().keys()
        )


if __name__ == "__main__":
    unittest.main()

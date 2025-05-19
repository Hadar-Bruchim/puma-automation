import time
from lib2to3.fixes.fix_input import context

import pytest

from tests.base_test import BaseTest
from tests.login import login_fixture

from utils.config_reader import ConfigReader


@pytest.mark.usefixtures("setup_driver_class")
class TestSearchForProduct(BaseTest):

    def test_01_click_on_search_btn(self):
        self.products_page.remove_popups()
        time.sleep(2)
        self.products_page.click_on_search()
        self.products_page.insert_text_in_search_bar("ferrai")
        time.sleep(2)
        self.products_page.click_on_search_result_item("Scuderia Ferrari Suede XL Hero")
        time.sleep(2)
        assert self.item_page.get_product_name() == "Scuderia Ferrari Suede XL Hero"
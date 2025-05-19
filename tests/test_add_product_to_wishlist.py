import time

import pytest

from tests.base_test import BaseTest
from tests.login import login_fixture

from utils.config_reader import ConfigReader


@pytest.mark.usefixtures("setup_driver_class", "login_fixture")
class TestAddProductToWishlist(BaseTest):


    def test_01_click_on_wishlist(self):
        self.products_page.choose_category_from_menu("wishlist")
        assert self.wishlist_page.wishlist_item_count_text() == "0 items"

    def test_02_move_to_women_clothing_category(self):
        self.products_page.choose_main_category('Women','clothing')
        time.sleep(3)
        assert self.products_page.get_category_title() == "WOMEN'S CLOTHING"

    def test_03_select_the_first_cloth(self):
        items = self.products_page.get_clothing_items()
        first_item = items[1]
        first_item.click()
        time.sleep(3)
        assert self.item_page.add_to_cart_button_text() == "ADD TO CART"

    def test_04_select_available_size(self):
        size = self.item_page.click_on_available_size(size=None)
        assert size is not None, "Error: size is None!"

    def test_05_add_to_wishlist(self):
        self.item_page.add_to_wishlist()
        self.products_page.choose_category_from_menu("wishlist")
        assert self.wishlist_page.wishlist_item_count_text() == "1 items"








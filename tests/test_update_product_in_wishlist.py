import time

import pytest

from tests.base_test import BaseTest
from tests.login import login_fixture

from utils.config_reader import ConfigReader


@pytest.mark.usefixtures("setup_driver_class", "login_fixture")
class TestUpdateProductInWishlist(BaseTest):

    def test_01_click_on_wishlist(self):
        self.products_page.choose_category_from_menu("wishlist")
        assert self.wishlist_page.wishlist_item_count_text() == "1 items"

    def test_02_click_on_update(self):
        self.wishlist_page.click_on_update_item_icon()
        time.sleep(3)
        assert self.wishlist_page.get_update_product_text() == "UPDATE ITEM"

    def test_03_update_a_new_size(self):
        current_size = self.wishlist_page.get_current_size()
        size = self.item_page.click_on_available_size(current_size)
        assert size is not None, "Error: size is None!"

    def test_04_click_on_update_item(self):
        self.wishlist_page.click_on_update_item()
        time.sleep(2)
        size = self.wishlist_page.get_current_size()
        assert size is not None, "Error: size is None!"



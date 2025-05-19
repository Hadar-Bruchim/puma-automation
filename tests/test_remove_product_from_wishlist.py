import time

import pytest

from tests.base_test import BaseTest
from tests.login import login_fixture

from utils.config_reader import ConfigReader


@pytest.mark.usefixtures("setup_driver_class", "login_fixture")
class TestRemoveProductFromWishlist(BaseTest):


    def test_01_click_on_wishlist(self):
        self.products_page.choose_category_from_menu("wishlist")
        assert self.wishlist_page.wishlist_item_count_text() == "1 items"

    def test_02_click_on_remove(self):
        self.wishlist_pageclick_on_remove_icon()
        time.sleep(1)
        self.wishlist_page.click_on_remove_btn()
        time.sleep(1)
        assert self.wishlist_page.wishlist_item_count_text() == "0 items"




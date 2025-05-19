import time


import pytest

from tests.base_test import BaseTest
from tests.login import login_fixture

from utils.config_reader import ConfigReader


@pytest.mark.usefixtures("setup_driver_class", "login_fixture")
class TestAddToCart(BaseTest):


    def test_01_click_on_cart(self):
        self.products_page.choose_category_from_menu("cart")
        assert self.cart_page.get_empty_cart_text() == "Your Shopping Cart is Empty"

    def test_02_add_product_to_cart(self):
        self.products_page.choose_category_from_menu("wishlist")
        self.wishlist_page.click_on_add_to_cart()
        time.sleep(5)
        self.products_page.choose_category_from_menu("cart")
        time.sleep(5)
        assert self.cart_page.get_number_of_items_icon() == '1'

    def test_03_insert_wrong_promo_cod(self):
        self.cart_page.insert_wrong_promo_code()
        time.sleep(2)
        assert self.cart_page.get_error_coupon_text() == 'Coupon cannot be added to your cart'

    def test_04_click_on_checkout(self):
        self.cart_page.click_on_checkout()
        time.sleep(3)
        assert self.checkout_page.get_checkout_text() == 'CHECKOUT'
        time.sleep(3)
        self.checkout_page.click_on_payment()
        time.sleep(3)
        assert self.checkout_page.get_payment_method_text() == 'Credit Card\nVisa\nMaster\nAmericanExpress\nDiscover'









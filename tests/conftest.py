import os
import time

import pytest
from selenium import webdriver

from pages.account_settings_page import AccountSettingsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.item_page import ItemPage
from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from pages.wishlist_page import WishlistPage

from utils.config_reader import ConfigReader


@pytest.fixture(scope="class")
def setup_driver_class(request):
    request.cls.driver = webdriver.Chrome()
    request.cls.driver.maximize_window()

    if os.path.exists("cookies.pkl"):
        request.cls.driver.get("https://google.com")
        from utils.session_utils import load_cookies
        load_cookies(request.cls.driver)

    request.cls.driver.get(ConfigReader.read_config("general","url"))
    time.sleep(1)
    request.cls.products_page = ProductsPage(request.cls.driver)
    request.cls.login_page = LoginPage(request.cls.driver)
    request.cls.forgot_password_page= ForgotPasswordPage(request.cls.driver)
    request.cls.wishlist_page = WishlistPage(request.cls.driver)
    request.cls.item_page = ItemPage(request.cls.driver)
    request.cls.cart_page = CartPage(request.cls.driver)
    request.cls.checkout_page = CheckoutPage(request.cls.driver)
    request.cls.account_settings_page = AccountSettingsPage(request.cls.driver)

    yield
    request.cls.driver.quit()

@pytest.fixture(scope="function")
def setup_function(request):
    request.cls.driver = webdriver.Chrome()
    request.cls.driver.maximize_window()
    request.cls.driver.get(ConfigReader.read_config("general","url"))
    time.sleep(1)
    request.cls.products_page = ProductsPage(request.cls.driver)
    request.cls.login_page = LoginPage(request.cls.driver)
    request.cls.forgot_password_page = ForgotPasswordPage(request.cls.driver)
    request.cls.wishlist_page = WishlistPage(request.cls.driver)
    request.cls.item_page = ItemPage(request.cls.driver)
    request.cls.cart_page = CartPage(request.cls.driver)
    request.cls.checkout_page = CheckoutPage(request.cls.driver)
    request.cls.account_settings_page = AccountSettingsPage(request.cls.driver)
    yield
    request.cls.driver.quit()
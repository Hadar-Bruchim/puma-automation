import time

import pytest

from tests.base_test import BaseTest
from utils.config_reader import ConfigReader



@pytest.mark.usefixtures("setup_driver_class", "login_fixture")
class TestLogIn(BaseTest):

    def test_01_remove_popups(self):
        self.products_page.remove_popups()
        time.sleep(2)

    def test_02_click_on_profile_and_signin(self):
        self.products_page.choose_category_from_menu("profile")
        self.products_page.click_on_login_btn()
        assert self.products_page.get_text_login_btn() == 'LOGIN'
        time.sleep(2)

    def test_03_login(self):
        self.login_page.insert_email_and_password(ConfigReader.read_config("users","user_name"),
                                                  ConfigReader.read_config("users","password"))
        time.sleep(2)
        self.products_page.choose_category_from_menu("profile")
        assert self.login_page.get_text_logout_btn() == 'LOGOUT'
        self.products_page.choose_category_from_menu("profile")


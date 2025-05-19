import time

import pytest

from tests.base_test import BaseTest
from utils.config_reader import ConfigReader


@pytest.mark.usefixtures("setup_driver_class")
class TestForgotPassword(BaseTest):


    def test_01_remove_popups(self):
        self.products_page.remove_popups()
        time.sleep(2)

    def test_02_click_on_profile_and_signin(self):
        self.products_page.choose_category_from_menu("profile")
        self.products_page.click_on_login_btn()
        time.sleep(2)

    def test_03_click_on_forgot_password(self):
        self.login_page.forgot_password()
        assert "Please provide your account email address" in self.forgot_password_page.get_forgot_password_title()
        time.sleep(2)

    def test_04_insert_email(self):
        self.forgot_password_page.insert_email("hadar@gmail.com")
        self.forgot_password_page.click_on_submit()
        time.sleep(3)
        assert "We’ve sent an email" in self.forgot_password_page.get_reset_password_text()




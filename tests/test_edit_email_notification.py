import time


import pytest

from tests.base_test import BaseTest
from tests.login import login_fixture

from utils.config_reader import ConfigReader


@pytest.mark.usefixtures("setup_driver_class", "login_fixture")
class TestAddToCart(BaseTest):

    def test_01_select_account_settings(self):
        self.products_page.choose_category_from_menu("profile")
        self.products_page.choose_sub_category("account")
        self.products_page.choose_side_category("account settings")
        assert self.account_settings_page.get_my_account_title() == "Account Settings"

    def test_02_click_on_the_email_notifications(self):
        self.account_settings_page.click_on_edit_email_notification()
        time.sleep(2)
        assert self.account_settings_page.get_email_notifications_text() == "Email Notifications"

    def test_02_select_the_third_option(self):
        self.account_settings_page.update_email_notification("third")
        self.account_settings_page.click_on_save_btn()








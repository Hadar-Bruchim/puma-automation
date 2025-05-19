import time
import pytest
from utils.config_reader import ConfigReader
from utils.session_utils import save_cookies


@pytest.fixture(scope='class')
def login_fixture(request):
    request.cls.products_page.remove_popups()
    request.cls.products_page.choose_category_from_menu("profile")
    request.cls.products_page.click_on_login_btn()
    request.cls.login_page.insert_email_and_password(ConfigReader.read_config("users", "user_name"),
                                                                    ConfigReader.read_config("users", "password"))
    request.cls.products_page.choose_category_from_menu("profile")
    assert request.cls.login_page.get_text_logout_btn() == 'LOGOUT'
    request.cls.products_page.choose_category_from_menu("profile")

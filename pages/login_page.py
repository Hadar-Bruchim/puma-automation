import time


from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __EMAIL_FIELD = (By.CSS_SELECTOR, "#email")
    __PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
    __SIGNIN_BTN = (By.CSS_SELECTOR, "[data-test-id = 'auth-button-login']")
    __LOGOUT_BTN= (By.CSS_SELECTOR, "[data-test-id = 'logout-button']")
    __FORGOT_PASSWORD_BTN = (By.CSS_SELECTOR, "[data-test-id = 'forgotten-password-link']")


    def insert_email_and_password(self, email, password):
        self.fill_text(self.__EMAIL_FIELD, email)
        self.fill_text(self.__PASSWORD_FIELD, password)
        time.sleep(2)
        self.click(self.__SIGNIN_BTN)
        time.sleep(2)

    def get_text_logout_btn(self):
        return self.get_text(self.__LOGOUT_BTN)

    def forgot_password(self):
        self.click(self.__FORGOT_PASSWORD_BTN)







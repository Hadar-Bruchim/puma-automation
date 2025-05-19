from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

import time



class ForgotPasswordPage(LoginPage):
    def __init__(self, driver):
        super().__init__(driver)

    __FORGOT_PASSWORD_TITLE = (By.CSS_SELECTOR, ".text-base.whitespace-pre-wrap")
    __EMAIL_FIELD = (By.CSS_SELECTOR, "#email-input")
    __SUBMIT_BTN  = (By.CSS_SELECTOR, "[data-test-id = 'submit-password-reset-btn']")
    __RESET_PASSWORD_TEXT = (By.CSS_SELECTOR, "[data-test-id = 'password-reset-email-sent-success']")


    def get_forgot_password_title(self):
        return self.get_text(self. __FORGOT_PASSWORD_TITLE)

    def insert_email(self, email):
        self.fill_text(self.__EMAIL_FIELD, email)
        time.sleep(2)

    def click_on_submit(self):
        self.click(self.__SUBMIT_BTN)

    def get_reset_password_text(self):
        return self.get_text(self. __RESET_PASSWORD_TEXT)





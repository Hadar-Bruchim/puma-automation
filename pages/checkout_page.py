from selenium.webdriver import ActionChains

from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

import time



class CheckoutPage(LoginPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.actions = ActionChains(driver)


    __CHECKOUT_HEADING_TEXT = (By.CSS_SELECTOR, "#checkout-heading")
    __CONTINUE_TO_PAYMENT_BTN = (By.CSS_SELECTOR, "[data-test-id = 'continue-to-payment']")
    __PAYMENT_METHOD_TEXT = (By.CSS_SELECTOR, "[data-uds-child = 'children']")


    def get_checkout_text(self):
        return self.get_text(self.__CHECKOUT_HEADING_TEXT)

    def fill_info_payment(self):
        pass

    def click_on_payment(self):
        self.actions.scroll_by_amount(0, 1000).perform()
        self.click(self.__CONTINUE_TO_PAYMENT_BTN)

    def get_payment_method_text(self):
        self.actions.scroll_by_amount(0, 300).perform()
        payment_methods = self.get_elements(self.__PAYMENT_METHOD_TEXT)
        credit_card_method = payment_methods[2]
        return credit_card_method.text

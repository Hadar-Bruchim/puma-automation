from selenium.webdriver import ActionChains, Keys

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

import time



class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.actions = ActionChains(driver)

    __GET_EMPTY_CART_TEXT = (By.CSS_SELECTOR, "#puma-skip-here > div > section > div > p")
    __GET_NUMBER_OF_ITEMS_ICON = (By.CSS_SELECTOR, "[data-test-id = 'nav-cart-tally-badge']")
    __PROMO_CODE = (By.CSS_SELECTOR, "#promo-code")
    __ERROR_COUPON_TEXT = (By.CSS_SELECTOR, "[data-uds-child = 'error-text']")
    __CHECKOUT_BTN = (By.CSS_SELECTOR, "[data-test-id = 'cart-summary-checkout']")


    def get_empty_cart_text(self):
        return self.get_text(self.__GET_EMPTY_CART_TEXT)

    def get_number_of_items_icon(self):
        return self.get_text(self.__GET_NUMBER_OF_ITEMS_ICON)

    def insert_wrong_promo_code(self):
        self.fill_text(self.__PROMO_CODE, "1234")
        time.sleep(2)
        promo_input = self.driver.find_element(*self.__PROMO_CODE)
        promo_input.click()
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER).perform()

    def get_error_coupon_text(self):
        return self.get_text(self.__ERROR_COUPON_TEXT)

    def click_on_checkout(self):
        self.actions.scroll_by_amount(0, 500).perform()
        time.sleep(3)
        self.click(self.__CHECKOUT_BTN)





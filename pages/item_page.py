

from selenium.webdriver import ActionChains

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

import time



class ItemPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.actions = ActionChains(driver)

    __ADD_TO_WISHLIST_BTN = (By.CSS_SELECTOR, "#add-to-wishlist")
    __ADD_TO_CART_BTN= (By.CSS_SELECTOR, "[data-test-id = 'add-to-cart-button']")
    __SIZE_BTN = (By.CSS_SELECTOR, "[data-content = 'size-value']")
    __DISABLED_BTN = (By.CSS_SELECTOR, ".relative.border.flex.items-center.justify-center.flex-none.rounded-sm.cursor-pointer")
    __GET_PRODUCT_NAME = (By.CSS_SELECTOR, "#pdp-product-title")

    def click_on_available_size(self, size):
        size_elements = self.get_elements(self.__SIZE_BTN)
        disabled_elements = self.get_elements(self.__DISABLED_BTN)

        for size_element, disabled_element in zip(size_elements, disabled_elements):
            data_disabled = disabled_element.get_attribute("data-disabled")
            if size_element.text == size:
                continue
            if data_disabled == "false":
                print(f"Size {size_element.text} is clickable, clicking now")
                size_element.click()
                time.sleep(2)
                return size_element.text

            elif data_disabled == "true":
                print(f" Size {size_element.text} is not clickable")
            else:
                print(f"This item out of stock")


    def add_to_wishlist(self):
        self.actions.scroll_by_amount(0, 500).perform()
        self.click(self.__ADD_TO_WISHLIST_BTN)

    def add_to_cart_button_text(self):
        self.actions.scroll_by_amount(0, 500).perform()
        return self.get_text(self.__ADD_TO_CART_BTN)

    def get_product_name(self):
        return self.get_text(self.__GET_PRODUCT_NAME)

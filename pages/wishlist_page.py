from pages.base_page import BasePage
from selenium.webdriver.common.by import By

import time


class WishlistPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __WISHLIST_ITEM_COUNT_TEXT = (By.CSS_SELECTOR, "[data-test-id = 'wishlist-item-count']")
    __UPDATE_PRODUCT_ICON = (By.CSS_SELECTOR, "[data-test-id = 'edit-product-button']")
    __UPDATE_ITEM_BTN = (By.CSS_SELECTOR, "#save-product")
    __REMOVE_PRODUCT_ICON = (By.CSS_SELECTOR, "[data-test-id = 'remove-product-button']")
    __REMOVE_BTN = (By.CSS_SELECTOR, "#confirm-button")
    __SIZE_TEXT = (By.CSS_SELECTOR, "[data-test-id = 'size']")
    __ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test-id = 'add-to-cart-button']")


    def wishlist_item_count_text(self):
        return self.get_text(self. __WISHLIST_ITEM_COUNT_TEXT )

    def click_on_update_item_icon(self):
        self.click(self.__UPDATE_PRODUCT_ICON)

    def click_on_remove_icon(self):
        self.click(self.__REMOVE_PRODUCT_ICON)

    def click_on_remove_btn(self):
        self.click(self.__REMOVE_BTN)

    def get_update_product_text(self):
        return self.get_text(self.__UPDATE_ITEM_BTN)

    def click_on_update_item(self):
        self.click(self.__UPDATE_ITEM_BTN)

    def get_current_size(self):
        return self.get_text(self.__SIZE_TEXT)

    def click_on_add_to_cart(self):
        self.click(self.__ADD_TO_CART_BTN)






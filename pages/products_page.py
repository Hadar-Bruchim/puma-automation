from pages.base_page import BasePage
from selenium.webdriver.common.by import By

import time

class ProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __COUNTRY_POPUP_BTN = (By.CSS_SELECTOR, "[data-test-id = 'close-btn']")
    __COOKIES_BTN = (By.CSS_SELECTOR, "[data-test-id = 'cookie-banner-close-btn']")
    __SALE_POPUP_BTN = (By.CSS_SELECTOR,
                        "#__next > div.relative.min-h-screen.flex.flex-col > div.sticky.overflow-hidden.bottom-0.px-4.py-4.lg\:px-8.lg\:py-8.block.z-\[11\].pointer-events-none > div > div > div > button > div.relative.opacity-100 > svg > use")
    __PROFILE_BTN = (By.CSS_SELECTOR, "#account-button")
    __WISHLIST_BTN = (By.CSS_SELECTOR, "#nav-wishlist-link")
    __CART_BTN = (By.CSS_SELECTOR, "#nav-cart-link")
    __CLOTHING_ITEMS = (By.CSS_SELECTOR, '[data-test-id= "product-list-item"]')
    __PRODUCT_ITEM_TITLE = (By.CSS_SELECTOR, '[data-test-id= "product-results"] > span')
    __LOGIN_BTN = (By.CSS_SELECTOR, "[data-test-id = 'login-button']")
    __CATEGORIES_LIST = (By.CSS_SELECTOR, "[data-test-id = 'main-nav-category-item']")
    __SEARCH_BTN = (By.CSS_SELECTOR, "[data-test-id = 'search-button-nav']")
    __SEARCH_BAR = (By.CSS_SELECTOR, "[data-test-id = 'search-flyout-form-input']")
    __RESULT_FROM_SEARCH = (By.CSS_SELECTOR, "[data-test-id = 'search-product-name']")
    __ACCOUNT_SETTINGS_BTN = (By.CSS_SELECTOR, "#puma-skip-here  div > nav > a:nth-child(7)")


    def remove_popups(self):
        self.click(self.__COUNTRY_POPUP_BTN)
        self.click(self.__COOKIES_BTN)
        time.sleep(2)
        self.click(self.__SALE_POPUP_BTN)
        time.sleep(2)


    def build_href_selector(self, category_name, sub_category=None):
        sub_path = category_name.lower()
        if sub_category:
            sub_path = f"{sub_path}/{sub_category}"
        href_value = f"/us/en/{sub_path}"
        return f'a[href="{href_value}"]'


    def choose_category_from_menu(self, category):
        match category:

            case 'profile':
                self.click(self.__PROFILE_BTN)
                time.sleep(2)

            case 'wishlist':
                self.click(self.__WISHLIST_BTN)
                time.sleep(2)

            case 'cart':
                self.click(self.__CART_BTN)
                time.sleep(2)

            case _:
                time.sleep(2)

    def choose_sub_category(self, sub_category):
        category_selector = self.build_href_selector(sub_category)
        element = (By.CSS_SELECTOR, category_selector)

        match sub_category:

            case 'account':
                self.click(element)
                time.sleep(3)


    def choose_side_category(self, side_category):
        match side_category:

            case 'account settings':
                self.click(self.__ACCOUNT_SETTINGS_BTN)
                time.sleep(2)


            case _:
                time.sleep(2)


    # def build_href_selector(self, category_name, sub_category=None):
    #     sub_path = category_name.lower()
    #     if sub_category:
    #         sub_path = f"{sub_path}/{sub_category}"
    #     return f'a[href*="{sub_path}"]'


    def choose_main_category(self, category_name, sub_category):
        categories_list = self.get_elements(self.__CATEGORIES_LIST)
        for category in categories_list:
            if category.text == category_name:
                category_selector = self.build_href_selector(category_name)
                element = (By.CSS_SELECTOR, category_selector)
                self.move_to_element(element)
                time.sleep(3)
                sub_category_selector = self.build_href_selector(category_name, sub_category)
                element = (By.CSS_SELECTOR, sub_category_selector)
                self.move_to_element_and_click(element)


    def click_on_login_btn(self):
        self.click(self.__LOGIN_BTN)
        time.sleep(2)

    def get_text_login_btn(self):
        return self.get_text(self.__LOGIN_BTN)


    def get_clothing_items(self):
        return self.get_elements(self.__CLOTHING_ITEMS)

    def get_category_title(self):
        return self.get_text(self.__PRODUCT_ITEM_TITLE)

    def click_on_search(self):
        self.click(self.__SEARCH_BTN)

    def insert_text_in_search_bar(self, text):
        self.fill_text(self.__SEARCH_BAR, text)

    def click_on_search_result_item(self, item_name):
        all_results = self.get_elements(self.__RESULT_FROM_SEARCH)
        for product in all_results:
            if product.text == item_name:
                product.click()
                break



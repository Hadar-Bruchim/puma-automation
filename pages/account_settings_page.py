from selenium.webdriver import ActionChains

from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

import time



class AccountSettingsPage(LoginPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.actions = ActionChains(driver)

    __MY_ACCOUNT_TITLE_TEXT= (By.CSS_SELECTOR, "[data-test-id = 'my-account-title']")
    __EMAIL_NOTIFICATION_BTN  = (By.CSS_SELECTOR, "[data-test-id = 'edit-email-notification-button']")
    __EMAIL_NOTIFICATION_TEXT = (By.CSS_SELECTOR, "[data-test-id = 'account-settings-modal-heading']")
    __EMAIL_NOTIFICATION_OPTIONS = (By.CSS_SELECTOR, "[data-uds-child = 'indicator']")
    __SAVE_CHANGES_BTN = (By.CSS_SELECTOR, "[data-test-id = 'submit-newsletter-preferences']")


    def get_my_account_title(self):
        return self.get_text(self.__MY_ACCOUNT_TITLE_TEXT)

    def click_on_edit_email_notification(self):
        self.actions.scroll_by_amount(0, 500).perform()
        self.click(self.__EMAIL_NOTIFICATION_BTN)

    def get_email_notifications_text(self):
        return self.get_text(self.__EMAIL_NOTIFICATION_TEXT)

    def update_email_notification(self,option):
        options = self.get_elements(self.__EMAIL_NOTIFICATION_OPTIONS)
        if option == 'first':
            first_item = options[0]
            first_item.click()
        elif option == 'second':
            second_item = options[1]
            second_item.click()
        elif option == "third":
            third_item = options[2]
            third_item.click()

    def click_on_save_btn(self):
        self.click(self.__SAVE_CHANGES_BTN)





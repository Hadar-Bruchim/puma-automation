import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    @property
    def driver(self):
        return self.__driver

    # def fill_text(self, locator, text ):
    #     #__NEXT_BTN = (By.CSS_SELECTOR, ".btn-next")
    #     self.driver.find_element(*locator).clear()
    #     self.driver.find_element(locator[0], locator[1]).send_keys(text)

    def fill_text(self, locator , text):
        element= self.driver.find_element(*locator)
        element.clear()
        time.sleep(1)
        element.send_keys(text)
        time.sleep(2)

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def get_elements(self, locator):
        return self.driver.find_elements(*locator)

    def select(self, locator, value):
        priority= self.driver.find_element(*locator)
        s = Select(priority)
        s.select_by_value(value)

    def move_to_element(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def move_to_element_and_click(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        time.sleep(3)




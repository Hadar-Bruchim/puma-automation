import pickle
import os
import time

COOKIES_FILE = "cookies.pkl"

def save_cookies(driver, file_path=COOKIES_FILE):
    with open(file_path, "wb") as file:
        pickle.dump(driver.get_cookies(), file)

def load_cookies(driver, file_path=COOKIES_FILE):
    if os.path.exists(file_path):
        with open(file_path, "rb") as file:
            cookies = pickle.load(file)
            for cookie in cookies:
                driver.add_cookie(cookie)

def login_and_save_cookies(driver, login_url):
    driver.get(login_url)
    time.sleep(20)  # או תכתבי כאן את הלוגין האוטומטי שלך
    save_cookies(driver)

def open_logged_in_session(driver, base_url):
    driver.get(base_url)
    load_cookies(driver)
    driver.refresh()
    return driver

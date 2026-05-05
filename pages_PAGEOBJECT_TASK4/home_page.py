from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePage(BasePage):
    URL = "https://geek-trip.ru/"

    CABINET = (By.CLASS_NAME, "header__cabinet")
    JUNKFOOD_COLLECTION = (By.CSS_SELECTOR, 'a[href="/collection/junkfood"]')

    def open_home(self):
        self.open(self.URL)

    def go_to_auth(self):
        self.click(self.CABINET)

    def open_junkfood_collection(self):
        self.click(self.JUNKFOOD_COLLECTION)
from selenium.webdriver.common.by import By
from .base_page import BasePage


class AuthPage(BasePage):
    URL = "https://geek-trip.ru/client_account/session/new"

    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.CLASS_NAME, "js-co-login-submit")
    REGISTER_LINK = (By.CSS_SELECTOR, 'a[href="/client_account/contacts/new"]')
    TITLE = (By.CLASS_NAME, "co-checkout-title")
    ERROR = (By.CLASS_NAME, "co-notice--danger")

    def open_auth(self):
        self.open(self.URL)

    def open_registration(self):
        self.click(self.REGISTER_LINK)

    def login(self, email: str, password: str):
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        self.click(self.SUBMIT)

    def get_history_title(self) -> str:
        return self.text_of(self.TITLE)

    def get_error_text(self) -> str:
        return self.text_of(self.ERROR)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base_page import BasePage


class RegistrationPage(BasePage):
    URL = "https://geek-trip.ru/client_account/contacts/new"

    NAME = (By.ID, "client_name")
    SURNAME = (By.ID, "client_surname")
    PHONE = (By.ID, "client_phone")
    EMAIL = (By.ID, "client_email")
    PASSWORD = (By.ID, "client_password")
    PASSWORD_CONFIRMATION = (By.ID, "client_password_confirmation")
    SUBMIT = (By.CLASS_NAME, "js-co-login-submit")
    TITLE = (By.CLASS_NAME, "co-checkout-title")
    ERROR = (By.CLASS_NAME, "co-notice--danger")

    def open_registration(self):
        self.open(self.URL)

    def register(self, name: str, surname: str, phone: str, email: str, password: str):
        self.type(self.NAME, name)
        self.type(self.SURNAME, surname)
        self.type(self.PHONE, phone)
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        self.type(self.PASSWORD_CONFIRMATION, password)
        self.click(self.SUBMIT)

        self.wait.until(
            EC.text_to_be_present_in_element(self.TITLE, "История заказов")
        )

    def get_history_title(self) -> str:
        return self.text_of(self.TITLE)

    def get_error_text(self) -> str:
        return self.text_of(self.ERROR)
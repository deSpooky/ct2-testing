from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class CatalogPage(BasePage):
    ADD_TO_CART = (By.CSS_SELECTOR, "[data-add-cart-counter-btn]")
    CART = (By.CLASS_NAME, "header__cart")

    def add_product_to_cart(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.ADD_TO_CART)
        )
        self.driver.execute_script("arguments[0].click();", button)

    def open_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CART)
        ).click()
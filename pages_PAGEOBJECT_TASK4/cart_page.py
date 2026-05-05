from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class CartPage(BasePage):
    ITEM_TITLE = (By.CLASS_NAME, "item-title")
    TOTAL_PRICE = (By.CSS_SELECTOR, "[data-cart-item-total-price]")

    def wait_cart_loaded(self):
        self.wait.until(
            EC.visibility_of_element_located(self.ITEM_TITLE)
        )

    def get_item_title(self) -> str:
        self.wait_cart_loaded()
        return self.text_of(self.ITEM_TITLE)

    def get_total_price(self) -> str:
        return self.text_of(self.TOTAL_PRICE)
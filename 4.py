from multiprocessing import Value
from ssl import Options
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()

chrome_options.page_load_strategy = "eager"

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)

try:
    driver.get("https://geek-trip.ru/")
    driver.find_element(By.CLASS_NAME, "header__cabinet").click()

    driver.find_element(By.ID, "email").send_keys("spooky@test.com")
    driver.find_element(By.ID, "password").send_keys("spooky")

    driver.find_element(By.CLASS_NAME, "js-co-login-submit").click()

    driver.find_element(By.CSS_SELECTOR,'a[href="/collection/junkfood"]').click()

    wait = WebDriverWait(driver, 10)

    button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-add-cart-counter-btn]'))
    )

    button.click()

    time.sleep(1)

    cart = wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME, "header__cart"))
)
    cart.click()

    item = driver.find_element(By.CLASS_NAME, "item-title")
    price = driver.find_element(By.CSS_SELECTOR, "[data-cart-item-total-price]")

    assert "Шоколадные Шарики Milka Melo Cakes" in item.text
    assert "350" in price.text  

finally:
    time.sleep(5)
    driver.quit()
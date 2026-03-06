from multiprocessing import Value
from ssl import Options
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("window")

chrome_options.page_load_strategy = "eager"

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)

try:
    driver.get("https://geek-trip.ru/")
    driver.find_element(By.CLASS_NAME, "header__cabinet").click()

    driver.find_element(By.ID, "email").send_keys("spooky@test.com")
    driver.find_element(By.ID, "password").send_keys("spooky")

    driver.find_element(By.CLASS_NAME, "js-co-login-submit").click()
    driver.find_element(By.CLASS_NAME, "header__cart").click()

    assert driver.find_element(By.CLASS_NAME, "cart-item")
    
finally:
    time.sleep(5)
    driver.quit()
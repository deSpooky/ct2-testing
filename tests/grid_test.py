import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

chrome_options = ChromeOptions()
firefox_options = FirefoxOptions()
driver = webdriver.Remote(
    command_executor = "http://localhost:4444",
    options=firefox_options
)

try:
    driver.get("https://google.com")
    driver.find_element(By.NAME, value="q").send_keys("Selenium Grid")
finally:
    time.sleep(5)
    driver.quit()
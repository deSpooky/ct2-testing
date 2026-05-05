import math

from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, browser: WebDriver, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(10)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except:
            return False
        return True

    def solve_alert_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log10(abs(12*math.sin(float(x)))))
        alert.send_keys(answer)
        alert.accept()
        alert = self.browser.switch_to.alert
        text = alert.text
        print(text)
        alert.accept()
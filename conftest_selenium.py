from os import name

import pytest
from selenium import webdriver

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--language", action="store", default="ru")

@pytest.fixture(scope="session")
def browser(request):
    if request.config.getoption("browser") == "Firefox":
        options = FirefoxOptions()
    elif request.config.getoption("browser") == "Edge":
        options = EdgeOptions()
    else:  
        options = ChromeOptions()
        options.page_load_strategy = 'normal'
        options.add_experimental_option(name= "prefs", value= {"intl.accept_language":
            request.config.getoption("language")})

    browser = webdriver.Remote(
        command_executor="http://10.11.19.21:4444",
        options=options
    )
    
    yield browser
    browser.quit()

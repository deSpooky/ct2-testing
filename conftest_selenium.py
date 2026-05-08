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
    browser_name = request.config.getoption("browser")
    user_language = request.config.getoption("language")
    
    if browser_name == "firefox":
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", user_language)
    elif browser_name == "edge":
        options = EdgeOptions()
    else:  
        options = ChromeOptions()
        options.page_load_strategy = 'normal'
        options.add_experimental_option("prefs", {"intl.accept_languages": user_language})

    browser = webdriver.Remote(
        command_executor="http://localhost:4444",
        options=options
    )
    
    yield browser
    browser.quit()

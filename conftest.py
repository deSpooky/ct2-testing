import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Chrome")
    parser.addoption("--language", action="store", default="ru")


@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("browser")
    language = request.config.getoption("language")

    if browser_name == "Firefox":
        driver = webdriver.Firefox()

    elif browser_name == "Edge":
        driver = webdriver.Edge()

    else:
        options = Options()
        options.page_load_strategy = "eager"
        options.add_experimental_option(
            "prefs",
            {"intl.accept_languages": language}
        )

        driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(5)

    yield driver

    driver.quit()

@pytest.fixture
def driver(browser):
    return browser
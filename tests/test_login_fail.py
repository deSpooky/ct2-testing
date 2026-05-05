from pages_PAGEOBJECT_TASK4.home_page import HomePage
from pages_PAGEOBJECT_TASK4.auth_page import AuthPage


def test_unsuccessful_login_random_data(driver):
    home = HomePage(driver)
    auth = AuthPage(driver)

    home.open_home()
    home.go_to_auth()

    auth.login("spooky@test.com", "5")

    assert "Сочетание логина и пароля не подходит" in auth.get_error_text()
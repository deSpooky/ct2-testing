from pages_PAGEOBJECT_TASK4.home_page import HomePage
from pages_PAGEOBJECT_TASK4.auth_page import AuthPage


def test_successful_login_existing_data(driver):
    home = HomePage(driver)
    auth = AuthPage(driver)

    home.open_home()
    home.go_to_auth()

    auth.login("spooky@test.com", "spooky")

    assert "История заказов" in auth.get_history_title()
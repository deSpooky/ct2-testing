from pages_PAGEOBJECT_TASK4.home_page import HomePage
from pages_PAGEOBJECT_TASK4.auth_page import AuthPage
from pages_PAGEOBJECT_TASK4.registration_page import RegistrationPage


def test_unsuccessful_registration_occupied_data(driver):
    home = HomePage(driver)
    auth = AuthPage(driver)
    reg = RegistrationPage(driver)

    home.open_home()
    home.go_to_auth()
    auth.open_registration()

    reg.register(
        name="spooky",
        surname="dats",
        phone="+79999999666",
        email="spooky@test.com",
        password="spooky",
    )

    assert "Пользователь с таким email уже зарегистрирован" in reg.get_error_text()
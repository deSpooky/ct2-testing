import uuid

from pages_PAGEOBJECT_TASK4.home_page import HomePage
from pages_PAGEOBJECT_TASK4.auth_page import AuthPage
from pages_PAGEOBJECT_TASK4.registration_page import RegistrationPage


def test_successful_registration_new_data(driver):
    home = HomePage(driver)
    auth = AuthPage(driver)
    reg = RegistrationPage(driver)

    unique_email = f"spooky_{uuid.uuid4().hex[:8]}@test.com"

    home.open_home()
    home.go_to_auth()
    auth.open_registration()

    reg.register(
        name="spooky",
        surname="dats",
        phone="+79999999999",
        email=unique_email,
        password="spooky",
    )

    assert "История заказов" in reg.get_history_title()
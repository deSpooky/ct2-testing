from pages_PAGEOBJECT_TASK4.home_page import HomePage
from pages_PAGEOBJECT_TASK4.auth_page import AuthPage
from pages_PAGEOBJECT_TASK4.catalog_page import CatalogPage
from pages_PAGEOBJECT_TASK4.cart_page import CartPage


def test_add_item_to_cart_and_check_it(driver):
    home = HomePage(driver)
    auth = AuthPage(driver)
    catalog = CatalogPage(driver)
    cart = CartPage(driver)

    home.open_home()
    home.go_to_auth()

    auth.login("spooky@test.com", "spooky")

    home.open_junkfood_collection()

    catalog.add_product_to_cart()

    catalog.open_cart()

    item_title = cart.get_item_title()
    total_price = cart.get_total_price()

    assert "Кислые" in item_title
    assert "50" in total_price
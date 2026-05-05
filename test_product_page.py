from pages.product_page import ProductPage


def test_guest_can_add_product_to_cart(browser):
    """Проверяет, что страница открывается, затем кликаем на кнопку добавления, затем решаем задачу, затем проверяем данные на уведомлениях"""
    link = "http://10.11.30.32/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    # ...
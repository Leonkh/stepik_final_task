# from pages.main_page import MainPage
# from pages.login_page import LoginPage
from pages.product_page import ProductPage
import time
import math
# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    # page.go_to__product_page()
    page.click_to_add_to_basket()
    page.solve_quiz_and_get_code()
    # time.sleep(10)

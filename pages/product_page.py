from .base_page import BasePage
from .locators import ProductPageLocators
import math
# from .login_page import LoginPage
# from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
# import math
class ProductPage(BasePage): 
    def click_to_add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)
    
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert ("login" in self.browser.current_url), "There is not login"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_EMAIL), "Login form email is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_PASS), "Login form pass is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_EMAIL), "Register form email is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_PASS), "Register form pass is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_PASS_CONFIRM), "Register form pass confirm is not presented"
        assert True
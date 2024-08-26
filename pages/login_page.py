from selenium.webdriver import Keys

from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Url is not correct"

    def should_be_login_form(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert True, "Login form is not found"

    def should_be_register_form(self):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM)
        assert True, "Registration form is not found"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        email_field.send_keys(Keys.ENTER)
        password_field = self.browser.find_element(*LoginPageLocators.PASS_FIELD)
        password_field.send_keys(password)
        password_field.send_keys(Keys.ENTER)
        password_field_repeat = self.browser.find_element(*LoginPageLocators.PASS_FIELD_REPEAT)
        password_field_repeat.send_keys(password)
        password_field_repeat.send_keys(Keys.ENTER)

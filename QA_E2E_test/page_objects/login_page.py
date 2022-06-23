from helium import *
from locators.locators import LoginPageLocator


class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver
        set_driver(self.driver)

    def enter_username(self, username):
        wait_until(TextField(LoginPageLocator.username).exists, 10)
        write(username, TextField(LoginPageLocator.username))

    def enter_password(self, password):
        write(password, TextField(LoginPageLocator.password))

    def click_sign_in_button(self):
        click(Button(LoginPageLocator.sign_in_button))

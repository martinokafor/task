from helium import *
from locators.locators import HomePageLocator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class HomePage(object):

    def __init__(self, driver):
        self.driver = driver
        set_driver(self.driver)

    def click_sign_in_button(self):
        wait_until(Text(HomePageLocator.sign_in_button).exists, 10)
        click(Text(HomePageLocator.sign_in_button))

    def accept_cookies(self):
        element = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located(
                HomePageLocator.accept_cookies))
        element.click()


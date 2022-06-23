import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import SpacePageLocator
from helium import *


class SpacePage(object):

    def __init__(self, driver, base_url):
        self.driver = driver
        set_driver(self.driver)
        self.driver.get(base_url + "foremeka/spaces")

    def create_public_space(self, name_of_space):
        wait_until(Text(SpacePageLocator.public_space_text).exists, 10)
        click(Text(SpacePageLocator.public_space_text))
        click(TextField(SpacePageLocator.public_space_text_field))
        press(CONTROL + "a" + CLEAR)
        write(
            name_of_space, into=TextField(
                SpacePageLocator.public_space_text_field))

    def click_save_space_button(self):
        click(S(SpacePageLocator.save_button))

    def click_more_button(self):
        wait_until(S(SpacePageLocator.more_button).exists, 10)
        click(find_all(S(SpacePageLocator.more_button))[2])

    def click_delete_space_button(self):
        wait_until(Text(SpacePageLocator.delete_space).exists, 10)
        click(Text(SpacePageLocator.delete_space))

    def enter_space_name_and_delete_space(self, space_name):
        element = self.driver.find_element(*SpacePageLocator.inner)
        WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable(SpacePageLocator.name_input))
        element = element.find_element(*SpacePageLocator.name_input)
        element.click()
        time.sleep(1)
        write(space_name)
        time.sleep(1)
        press(ENTER)

    def verify_create_space_card(self):
        wait_until(S(SpacePageLocator.create_space_card).exists, 10)
        Text(SpacePageLocator.create_space_title).exists()
        elements = self.driver.find_elements(*SpacePageLocator.create_space_card_buttons)
        element_text = []
        for element in elements:
            element_text.append(element.text.splitlines())
        assert element_text[0] == ["Private space", "Public space"]

    def verify_card_header_public_space(self):
        public_space = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located(
                SpacePageLocator.public_space))
        assert public_space.find_element(
            *SpacePageLocator.card_header).is_displayed()

    def verify_card_header_private_space(self):
        private_space = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located(
                SpacePageLocator.private_space))
        assert private_space.find_element(
            *SpacePageLocator.card_header).is_displayed()

    def verify_card_footer_public_space(self):
        public_space = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located(
                SpacePageLocator.public_space))
        elements = public_space.find_elements(*SpacePageLocator.counter_icon)
        assert elements[0].is_displayed()
        assert elements[1].is_displayed()
        assert elements[2].is_displayed()
        assert public_space.find_element(
            *SpacePageLocator.owner_icon).is_displayed()

    def verify_card_footer_private_space(self):
        private_space = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located(
                SpacePageLocator.private_space))
        elements = private_space.find_elements(*SpacePageLocator.counter_icon)
        # FIXME BUG: workflows icon is not shown in screenshot for private
        #  space but exist in the application
        assert elements[0].is_displayed() is False
        assert elements[1].is_displayed()
        assert elements[2].is_displayed()
        assert private_space.find_element(
            *SpacePageLocator.owner_icon).is_displayed()

    def verify_card_body_public_space(self):
        public_space = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located(
                SpacePageLocator.public_space))
        element = public_space.find_element(*SpacePageLocator.card_body)
        assert element.is_displayed()
        assert element.text is not None

    def verify_card_body_private_space(self):
        private_space = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located(
                SpacePageLocator.private_space))
        element = private_space.find_element(*SpacePageLocator.card_body)
        assert element.is_displayed()
        assert element.text is not None

    def wait_until_notification_message_disappears(self):
        try:
            WebDriverWait(self.driver, 25).until(
                EC.invisibility_of_element_located(
                    SpacePageLocator.notification_message))
            time.sleep(4)
        except:
            pass

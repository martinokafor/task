from random import randint
from test_suite.base_test import BaseTest
from page_objects.login_page import LoginPage
from page_objects.space_page import SpacePage
from page_objects.home_page import HomePage


class Test(BaseTest):

    def setUp(self):
        super(Test, self).setUp()

    def test_create_and_delete_space(self):
        username = "foremeka"
        password = "12345"
        space_name = f"space {randint(100,900)}"

        home_page = HomePage(self.driver)
        home_page.accept_cookies()
        home_page.click_sign_in_button()
        login_page = LoginPage(self.driver)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_sign_in_button()
        space_page = SpacePage(self.driver, self.base_url)
        space_page.create_public_space(space_name)
        space_page.click_save_space_button()
        space_page.wait_until_notification_message_disappears()
        space_page.click_more_button()
        space_page.click_delete_space_button()
        space_page.enter_space_name_and_delete_space(space_name)

    def test_verify_elements_in_space_page(self):
        username = "foremeka"
        password = "12345"

        home_page = HomePage(self.driver)
        home_page.accept_cookies()
        home_page.click_sign_in_button()
        login_page = LoginPage(self.driver)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_sign_in_button()
        space_page = SpacePage(self.driver, self.base_url)
        space_page.verify_create_space_card()
        space_page.verify_card_header_public_space()
        space_page.verify_card_body_public_space()
        space_page.verify_card_footer_public_space()
        space_page.verify_card_header_private_space()
        space_page.verify_card_body_private_space()
        space_page.verify_card_footer_private_space()



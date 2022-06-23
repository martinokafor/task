from selenium.webdriver.common.by import By


class HomePageLocator:
    " Helium + Selenium approach of locators"
    sign_in_button = "Sign in"
    accept_cookies = (By.CLASS_NAME, "accept-button.button.primary")


class LoginPageLocator(HomePageLocator):
    " Helium + Selenium approach of locators"
    username = "Username or email address"
    password = "Password"


class SpacePageLocator:
    " Helium + Selenium approach of locators"
    public_space_text = "Public space"
    save_button = ".function-button.single.primary"
    more_button = ".tooltip"
    delete_space = "Delete space"
    name_input = (By.XPATH, "//form[@id='confirmationForm']")
    inner = (By.CLASS_NAME, "inner")
    notification_message = (By.CLASS_NAME, "message")
    public_space_text_field = "Enter public space name"
    create_space_card = ".create-space-card"
    create_space_title = "Create new space"
    create_space_card_buttons = (By.CLASS_NAME, "buttons")
    card_body = (By.CLASS_NAME, "card-body")
    card_footer = ".card-footer"
    card_header = (By.CSS_SELECTOR, ".card-header")
    counter_icon = (By.CSS_SELECTOR, ".counter")
    owner_icon = (By.CLASS_NAME, "avatar.avatar-placeholder")
    private_space = (By.CLASS_NAME, "space-card.private-space-card")
    public_space = (By.CLASS_NAME, "space-card")

import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.base_url = "https://hub.knime.com/"
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self.base_url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
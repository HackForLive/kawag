"""
A simple selenium test example written for debugging purposes
"""

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



class TestTemplate(unittest.TestCase):
    """Include test cases on a given url"""

    def setUp(self):
        """Start web driver"""
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        # self.driver = webdriver.Remote(command_executor="http://127.0.0.1:8444", 
        #                                desired_capabilities=DesiredCapabilities.CHROME)


        self.driver.implicitly_wait(10)

    def tearDown(self):
        """Stop web driver"""
        self.driver.quit()

    def test_case_1(self):
        """Find and click top-right button"""
        try:
            self.driver.get('https://www.oursky.com/')
            el = self.driver.find_element(By.CLASS_NAME, 'landing__hero')
            el.click()
        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def test_case_2(self):
        """Find and click Learn more button"""
        try:
            self.driver.get('https://www.oursky.com/')
            el = self.driver.find_element(By.XPATH, ".//*[@class='landing__btn']/span")
            el.click()
        except NoSuchElementException as ex:
            self.fail(ex.msg)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplate)
    unittest.TextTestRunner(verbosity=2).run(suite)

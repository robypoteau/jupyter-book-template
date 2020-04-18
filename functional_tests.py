from selenium import webdriver
import unittest

from os import getcwd

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_function(self):
        html_filename = 'file://' + getcwd() + '/docs/Index.html'
        self.browser.get(html_filename)

        # Make sure the links work

        pass

if __name__ == "__main__":
    unittest.main()

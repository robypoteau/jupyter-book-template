from selenium import webdriver
import unittest

from os import getcwd, listdir

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_homepage_links_exist(self):
        html_home_filename = 'file://' + getcwd() + '/docs/Index.html'
        self.browser.get(html_home_filename)

        notebook_filename = [file.replace('.ipynb', '.html') for file in listdir('./notebooks/') if file.endswith('.ipynb')]
        notebook_filename.remove('Index.html')
        notebook_filename.sort()

        for filename in notebook_filename:
            try:
                self.browser.find_element_by_xpath(f"//a[contains(@href,'{filename}')]")
            except NoSuchElementException:
                self.fail(f"'{filename}' was not properly copied to TOC as an html")



if __name__ == "__main__":
    unittest.main()

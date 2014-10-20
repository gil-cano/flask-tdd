from selenium import webdriver
from selenium.webdriver.common.keys import Keys


import unittest


class WordCounterTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_index(self):
        # Edith has heard about a cool new online app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:5000')
        self.assertIn('Word Counter', self.browser.title)

        inputbox = self.browser.find_element_by_id('text')
        self.assertEqual(inputbox.get_attribute('placeholder'), '')

        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)


if __name__ == '__main__':
    unittest.main()

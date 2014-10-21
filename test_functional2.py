from selenium import webdriver
from selenium.webdriver.common.keys import Keys


import unittest


class WordCounterTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_index(self):
        # Gil has heard about a cool new online app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:5000')
        self.assertIn('Word Counter', self.browser.title)

        # He is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('text')

        # He types "Facultad de Ciencias" into a text box
        inputbox.send_keys('Facultad de Ciencias')

        # When he hits enter, the page updates, and now the page lists
        # number of characters and number of words
        submit = self.browser.find_element_by_id('submit')
        submit.send_keys(Keys.ENTER)

        alert = self.browser.find_element_by_class_name('alert')
        self.assertIn('3 palabras 20 caracteres', alert.text)

        # self.browser.find_elements_by_tag_name('button')[0].text


if __name__ == '__main__':
    unittest.main()

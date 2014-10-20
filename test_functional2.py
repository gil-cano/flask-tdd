from selenium import webdriver


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


if __name__ == '__main__':
    unittest.main()

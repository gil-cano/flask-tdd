from app import app

import unittest


class AppTestCase(unittest.TestCase):

    def test_index(self):
        """initial test. ensure flask was set up correctly"""
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        assert "Word Counter" in response.data

if __name__ == '__main__':
    unittest.main()

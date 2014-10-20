import unittest
from my_mod import my_func


class MyTests(unittest.TestCase):
    def test_my_func(self):
        test_vals = (2, 3)
        expected = reduce(lambda x, y: x * y, test_vals)
        actual = my_func(*test_vals)
        self.assertEquals(expected, actual)

if __name__ == '__main__':
    unittest.main()

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

# http://www.jeffknupp.com/blog/2013/11/29/improve-your-python-decorators-explained/?utm_source=Python+Weekly+Newsletter&utm_campaign=d70b0a6e79-Python_Weekly_Issue_116_December_5_2013&utm_medium=email&utm_term=0_9e26887fc5-d70b0a6e79-312663121#
# http://docs.python-guide.org/en/latest/writing/tests/
# http://cewing.github.io/training.codefellows/lectures/day09/jenkins.html
# http://intermediate-and-advanced-software-carpentry.readthedocs.org/en/latest/testing-python.html
# http://codefellows.github.io/sea-f2-python-sept14/session07.html
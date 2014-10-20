import unittest


class MyTests(unittest.TestCase):
    def test_tautology(self):
        self.assertEquals(1, 1)

if __name__ == '__main__':
    unittest.main()

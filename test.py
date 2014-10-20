import unittest


class MyTests(unittest.TestCase):

    def test_tautology(self):
        self.assertEquals(1, 1)

    def test_sort(self):
        seq = [5, 4, 1, 3, 2]
        seq.sort()
        self.assertEqual(seq, [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()

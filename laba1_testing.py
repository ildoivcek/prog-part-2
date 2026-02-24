import unittest
import from laba1 longest_peak

class TestLongestPeak(unittest.TestCase):

    def test_example(self):
        self.assertEqual(longest_peak([1, 3, 5, 4, 2, 8, 3, 7]), 5)

    def test_sorted_zrostae(self):
        self.assertEqual(longest_peak([1, 2, 3, 4, 5]), 0)

    def test_sorted_spadae(self):
        self.assertEqual(longest_peak([5, 4, 3, 2, 1,]), 0)

    def test_two_elements(self):
        self.assertEqual(longest_peak([1, 2]), 0)

    def test_no_peaks(self):
        self.assertEqual(longest_peak([2, 2, 2]), 0)
        self.assertEqual(longest_peak([-1, -5, -1]), 0)

    def test_three_peaks(self):
        self.assertEqual(longest_peak([1, 3, 2, 1, 5, 4, 1, 4, 8, 6, 2]), 5)


if __name__ == '__main__':
    unittest.main()

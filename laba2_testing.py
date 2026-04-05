import unittest
from laba2 import largest_min_distance

class TestAggressiveCows(unittest.TestCase):
    
    def test_example(self):
        self.assertEqual(largest_min_distance(5, 3, [1, 2, 8, 4, 9]), 3)

    def test_two_cows(self):
        self.assertEqual(largest_min_distance(5, 2, [1, 2, 8, 4, 9]), 8)

    def test_all_cows(self):
        self.assertEqual(largest_min_distance(5, 5, [1, 2, 8, 4, 9]), 1)

if __name__ == '__main__':
    unittest.main()

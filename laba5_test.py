import unittest
from laba5 import count_islands
from laba5_dod import max_island_area

class TestIslandsLab(unittest.TestCase):
    def setUp(self):
        self.test_grid = [
            [1, 1, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 0, 1],
            [1, 0, 0, 0]
        ]

    def test_count_islands(self):
        self.assertEqual(count_islands(self.test_grid), 3)

    def test_max_area(self):
        #найбільший острів має 3 клітинки
        self.assertEqual(max_island_area(self.test_grid), 3)

    def test_empty_grid(self):
        self.assertEqual(count_islands([]), 0)
        self.assertEqual(max_island_area([]), 0)

    def test_no_land(self):
        no_land = [[0, 0], [0, 0]]
        self.assertEqual(count_islands(no_land), 0)
        self.assertEqual(max_island_area(no_land), 0)

if __name__ == "__main__":
    unittest.main()

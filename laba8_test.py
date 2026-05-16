import unittest
from wchain import get_chain

class TestGame(unittest.TestCase):
    def test_main(self):
        #приклад на 5
        words = ["t", "at", "cat", "cats", "car", "crats"]
        self.assertEqual(get_chain(words), 5)

    def test_simple(self):
        #один ланцюжок
        self.assertEqual(get_chain(["a", "ab", "abc"]), 3)

if __name__ == "__main__":
    unittest.main()

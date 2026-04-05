import unittest
from laba4 import PriorityQueue


class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = PriorityQueue()

    def test_push_and_peek(self):
        self.pq.push("Task1", 10)
        self.pq.push("Task2", 50)
        self.assertEqual(self.pq.peek(), "Task2")

    def test_pop_order(self):
        self.pq.push("A", 10)
        self.pq.push("B", 30)
        self.pq.push("C", 20)
        self.assertEqual(self.pq.pop(), "B")
        self.assertEqual(self.pq.pop(), "C")
        self.assertEqual(self.pq.pop(), "A")

    def test_empty_queue(self):
        self.assertIsNone(self.pq.pop())
        self.assertIsNone(self.pq.peek())

    def test_same_priority(self):
        self.pq.push("First", 100)
        self.pq.push("Second", 100)
        self.assertEqual(self.pq.pop(), "First")
        self.assertEqual(self.pq.pop(), "Second")

    def test_bfs_levels(self):
        self.pq.push("Root", 50)
        self.pq.push("Left", 70)
        self.pq.push("Right", 30)
        
        levels = self.pq.get_level_order()
        
        self.assertEqual(len(levels), 2)
        self.assertIn("[Root:50]", levels[0][0])
        self.assertIn("[Left:70]", levels[1][0])
        self.assertIn("[Right:30]", levels[1][1])

     def test_complex_tree(self):
        data = [("M", 50), ("H", 80), ("L", 20), ("MH", 60)]
        for v, p in data:
            self.pq.push(v, p)
        
        self.assertEqual(self.pq.pop(), "H")
        self.assertEqual(self.pq.pop(), "MH")
        self.assertEqual(self.pq.pop(), "M")
        self.assertEqual(self.pq.pop(), "L")


if __name__ == "__main__":
    unittest.main()

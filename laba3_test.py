import unittest
from laba3 import BinaryTree, binary_tree_diameter


class TestBinaryTreeDiameter(unittest.TestCase):
    def test_official_example(self):
       #Тест структури 9 -> 8 -> 7 -> 3 -> 4 -> 5 -> 6 (діаметр 6)
        #ліва гілка (9-8-7)
        node9 = BinaryTree(9)
        node8 = BinaryTree(8, left=node9)
        node7 = BinaryTree(7, left=node8)
        
        #права гілка від трійки (4-5-6)
        node6 = BinaryTree(6)
        node5 = BinaryTree(5, right=node6)
        node4 = BinaryTree(4, right=node5)
        
        #обєєднання в вузол 3
        node3 = BinaryTree(3, left=node7, right=node4)
        
        #корінь та вузол 2
        root = BinaryTree(1, left=node3, right=BinaryTree(2))
        
        self.assertEqual(binary_tree_diameter(root), 6)

    def test_null_tree(self):
       #порожнє дерев

        self.assertEqual(binary_tree_diameter(None), 0)

    def test_single_node(self):
        #один вузол
        self.assertEqual(binary_tree_diameter(BinaryTree(10)), 0)


if __name__ == "__main__":
    unittest.main()

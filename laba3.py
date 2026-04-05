class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def get_max_val(a, b, c=None):
    res = a
    if b > res:
        res = b
    if c is not None and c > res:
        res = c
    return res


def get_diameter_and_height(node: BinaryTree):
    if node is None:
        return 0, -1

    left_diameter, left_height = get_diameter_and_height(node.left)
    right_diameter, right_height = get_diameter_and_height(node.right)
    bigger_height = left_height
    if right_height > left_height:
        bigger_height = right_height
    
    current_height = 1 + bigger_height

    diameter_through_node = (left_height + 1) + (right_height + 1)

    current_max_diameter = get_max_val(
        diameter_through_node, 
        left_diameter, 
        right_diameter
    )

    return current_max_diameter, current_height


def binary_tree_diameter(tree: BinaryTree) -> int:
    if tree is None:
        return 0
    diameter, _ = get_diameter_and_height(tree)
    return diameter

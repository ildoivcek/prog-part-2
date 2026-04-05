import os

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def print_tree(self):
        canvas = [[" "] * 100 for _ in range(40)]
        
        def draw(node, r, c, dir_x, h_step, v_step):
            if not node: return
            
            if node.right:
                canvas[r - max(1, v_step // 2)][c + (dir_x * h_step) // 2] = "\\" if dir_x == -1 else "/"
                draw(node.right, r - v_step, c + dir_x * h_step, dir_x, max(2, h_step - 2), max(2, v_step // 2))

            for i, char in enumerate(str(node.value)):
                if 0 <= r < 40 and 0 <= c + i < 100:
                    canvas[r][c + i] = char
                
            if node.left:
                canvas[r + max(1, v_step // 2)][c + (dir_x * h_step) // 2] = "/" if dir_x == -1 else "\\"
                draw(node.left, r + v_step, c + dir_x * h_step, dir_x, max(2, h_step - 2), max(2, v_step // 2))

        root_r = 18
        if self.right:
            canvas[root_r][42:45] = ["-", "-", "-"]
            draw(self.right, root_r, 46, 1, 10, 10)
            
        canvas[root_r][40] = str(self.value)
        
        if self.left:
            canvas[root_r][36:39] = ["-", "-", "-"]
            draw(self.left, root_r, 34, -1, 10, 10)

        for row in canvas:
            line = "".join(row).rstrip()
            if line: print(line)

def sorted_array_to_bst(arr):
    if not arr:
        return None
    
    mid = len(arr) // 2
    root = BinaryTree(int(arr[mid]))
    
    root.left = sorted_array_to_bst(arr[:mid])
    root.right = sorted_array_to_bst(arr[mid+1:])
    return root

def main():
    filename = "inorder_invert.txt"
    if not os.path.exists(filename):
        print(f"{filename} не знайдено")
        return
        
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read().replace(',', ' ').split()
        values = sorted([int(x) for x in data if x.lstrip('-').isdigit()])

    print(f"список посортований {values}")
    
    root = sorted_array_to_bst(values)
    
    if root:
        print("\nІНВЕРТОВАНЕ ВІДОБРАЖЕННЯ")
        root.print_tree()

if __name__ == "__main__":
    main()

import sys

class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None

class PriorityQueue:
    def __init__(self):
        self.root = None

    def push(self, value, priority):
        if not self.root:
            self.root = Node(value, priority)
        else:
            self._insert(self.root, value, priority)

    def _insert(self, current, value, priority):
        if priority > current.priority:
            if current.left is None:
                current.left = Node(value, priority)
            else:
                self._insert(current.left, value, priority)
        else:
            if current.right is None:
                current.right = Node(value, priority)
            else:
                self._insert(current.right, value, priority)
                
    #доп я придумала ну джеміні            
    def get_level_order(self):
        if not self.root:
            return []
        
        result = []
        queue = [(self.root, 0)]  
        
        while queue:
            node, level = queue.pop(0)
            
            if len(result) <= level:
                result.append([])
            
            result[level].append(f"{node.value}:{node.priority}")
            
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        return result
    #кінець методу для дод

    def pop(self):
        if not self.root:
            return None
        
        parent = None
        current = self.root
        
        while current.left:
            parent = current
            current = current.left
            
        value = current.value
        
        if parent:
            parent.left = current.right
        else:
            self.root = current.right
            
        return value

    def peek(self):
        if not self.root:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.value

    def display(self, node=None, level=0, prefix="Root: "):
        if level == 0:
            node = self.root
            if not node:
                print("пусто")
                return
        if node:
            print("    " * level + prefix + f"[{node.value}:{node.priority}]")
            if node.left or node.right:
                if node.left:
                    self.display(node.left, level + 1, "L-- ")
                if node.right:
                    self.display(node.right, level + 1, "R-- ")


def main():
    pq = PriorityQueue()
    
    while True:
        print("\n1. додати (push) | 2. вилучити (pop) | 3. подивитись шо є (peek) | 4. вихід")
        choice = input("оберіть дію: ").strip()

        if choice == '1':
            try:
                val = input("значення: ")
                prio = int(input("пріоритет (число): "))
                pq.push(val, prio)
            except ValueError:
                print("помилка: введіть ціле число для пріоритету.")
        elif choice == '2':
            res = pq.pop()
            print(f"вилучено: {res}" if res else "нема шо")
        elif choice == '3':
            res = pq.peek()
            print(f"найвищий пріоритет: {res}" if res else "нема шо")
        elif choice == '4':
            sys.exit(0)
        
        print("\nпоки шо такий вигляд")
        pq.display()

if __name__ == "__main__":
    main()

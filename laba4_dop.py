import sys
try:
    from laba4 import PriorityQueue
except ImportError:
    print("файл .py не знайдено в поточній директорії")
    sys.exit(1)

def run_bonus_task():
    pq = PriorityQueue()
    
    print("ОБХІД У ШИРИНУ (BFS)")
    print("рівнева структура бінарного дерева")
    
    while True:
        print("\n" + "="*40)
        print("1. додати новий елемент (push)")
        print("2. візуалізувати дерево за рівнями (BFS)")
        print("3. очистити чергу (створити нову)")
        print("4. повернутися до основної програми")
        
        choice = input("\nоберіть опцію: ").strip()
        
        if choice == '1':
            try:
                val = input("введіть назву (value): ")
                prio = int(input("введіть пріоритет (integer): "))
                pq.push(val, prio)
                print(f"елемент '{val}' додано до структури")
            except ValueError:
                print("пріоритет має бути цілим числом")
                
        elif choice == '2':
            try:
                levels = pq.get_level_order()
                if not levels:
                    print("структура порожня. додайте елементи (опція 1).")
                else:
                    print("\nВІЗУАЛІЗАЦІЯ")
                    for i, level_nodes in enumerate(levels):
                        print(f"рівень {i}:  {'  |  '.join(level_nodes)}")
            except AttributeError:
                print("Метод 'get_level_order' не знайдено в класі PriorityQueue.")
                
        elif choice == '3':
            pq = PriorityQueue()
            print("чергу успішно очищено")
            
        elif choice == '4':
            print("завершення роботи модуля BFS")
            break
        else:
            print("некоректний ввід. використовуйте цифри 1-4.")

if __name__ == "__main__":
    run_bonus_task()

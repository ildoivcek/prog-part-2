# похід починаю з 0
def longest_mountain(height, times):
    max_total_time = 0
    best_climb_time = 0

    # починає йти з 1 кроку до передостаннього
    for i in range(1, len(height) - 1):
        
        # перевіряє чи він на вершині
        if height[i - 1] < height[i] and height[i] > height[i + 1]:
            
            # дивиться вліво тобто назад
            left_step = i - 1
            while left_step >= 0 and height[left_step] < height[left_step + 1]:
                left_step -= 1  # уявний крок назад вниз
                
            # дивиться вперед направо типу скільки йому спускатись
            right_step = i + 1
            while right_step < len(height) and height[right_step] < height[right_step - 1]:
                right_step += 1  # уявно вперед вниз

            # left_step + 1 -> це індекс (номер) початку гори
            # i             -> це індекс вершини
            # right_step - 1-> це індекс кінця гори

            # Час на підйом (час на вершині мінус час на початку)
            climb_time = times[i] - times[left_step + 1]
            
            # Час на всю гору (час в кінці мінус час на початку)
            total_time = times[right_step - 1] - times[left_step + 1]
            
            # Якщо загальний час цієї гори більший за рекорд у блокноті:
            if total_time > max_total_time:
                max_total_time = total_time
                best_climb_time = climb_time # запам'ятовуємо час підняття саме для цієї гори

    # повертаємо одразу два рекорди
    return max_total_time, best_climb_time


if __name__ == '__main__':
    print("--- GPS Трекер Туриста ---")
    str_heights = input("Введіть висоти гір (н-кад: 1 3 5 4 2): ")
    str_times = input("Введіть секунди GPS (н-кад: 0 10 25 35 50): ")
    
    try:
        # перетворюю в списки
        height_array = [int(x) for x in str_heights.split()]
        times_array = [int(x) for x in str_times.split()]
        
        # перевірка, щоб людина ввела однакову кількість висот і секунд
        if len(height_array) != len(times_array):
            print("Помилка! Кількість висот і секунд має співпадати.")
        else:
            # віддаємо туристу і висоти, і секунди
            total_t, climb_t = longest_mountain(height_array, times_array)
            print(f"Загальний час на найбільшу гору: {total_t} сек.")
            print(f"З них час підняття на вершину: {climb_t} сек.")
            
    except ValueError:
        print("тільки числа")

def radix_sort(arr):
    if len(arr) <= 1:
        return arr
        
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
            
    position = 1
    
    while max_num // position > 0:
        buckets = [[], [], [], [], [], [], [], [], [], []]
        
        for num in arr:
            digit = (num // position) % 10
            buckets[digit].append(num)
            
        arr = []
        for bucket in buckets:
            for item in bucket:
                arr.append(item)
                
        position *= 10
        
    return arr

def can_place_cows(distance, C, free_sections):
    cows_placed = 1
    last_position = free_sections[0]
    
    for i in range(1, len(free_sections)):
        if free_sections[i] - last_position >= distance:
            cows_placed += 1
            last_position = free_sections[i]
            if cows_placed == C:
                return True
    return False

def largest_min_distance(N, C, free_sections):
    free_sections = radix_sort(free_sections)
    
    low = 1
    high = free_sections[-1] - free_sections[0]
    best_distance = 0
    
    while low <= high:
        mid = (low + high) // 2
        
        if can_place_cows(mid, C, free_sections):
            best_distance = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return best_distance

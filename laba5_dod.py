from collections import deque
from laba5 import get_all_islands_coordinates, get_islands_areas

#додаткове завдання 1: пошук площі найбільшого острова
def max_island_area(grid):
    if not grid:
        return 0
    areas = get_islands_areas(grid)
    return max(areas) if areas else 0


#додаткове завдання 2: пошук найкоротшого мосту між островами (BFS)
def find_bridge_length(grid):
    islands = get_all_islands_coordinates(grid)
    
    if len(islands) < 2:
        return "Треба мінімум 2 острови для прокладання мосту"

    source_island = islands[0]
    
    target_points = set()
    for i in range(1, len(islands)):
        for r, c in islands[i]:
            target_points.add((r, c))
    
    queue = deque()
    visited = set()
    
    for r, c in source_island:
        queue.append((r, c, 0))
        visited.add((r, c))

    while queue:
        r, c, dist = queue.popleft()
        
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited:
                if (nr, nc) in target_points:
                    return dist
                
                if grid[nr][nc] == 0:
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))
    
    return -1

def get_all_islands_coordinates(grid): #grid - matrutsya
    if not grid:
        return []

    rows = len(grid)
    cols = len(grid[0])
    visited = set() #klitinki sushi
    all_islands = [] #ploshcha

    def dfs(r, c): #r ryadok c stovpec
        stack = [(r, c)]
        island_cells = []
        visited.add((r, c))
        
        while stack:
            curr_r, curr_c = stack.pop()
            island_cells.append((curr_r, curr_c))
            directions = [
                (-1, 0), (1, 0), (0, -1), (0, 1),
                (-1, -1), (-1, 1), (1, -1), (1, 1)
            ]
            
            for dr, dc in directions: #delta r c yak zmina
                nr, nc = curr_r + dr, curr_c + dc # n new r new s
                if (0 <= nr < rows and 0 <= nc < cols and 
                    grid[nr][nc] == 1 and (nr, nc) not in visited):
                    visited.add((nr, nc))
                    stack.append((nr, nc))
        return island_cells

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                all_islands.append(dfs(r, c))

    return all_islands

def get_islands_areas(grid):
    islands = get_all_islands_coordinates(grid)
    return [len(island) for island in islands]

def count_islands(grid):
    return len(get_all_islands_coordinates(grid))

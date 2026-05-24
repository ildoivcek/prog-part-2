from src.laba7 import bfs

def find_critical_roads(original_dorogy, final_graf, s_super):
    #шукаємо дороги, які повністю забиті машинами (min-cut).
    це ті дороги, де в одну сторону потік став 0, а в іншу — максимум.
    
    # 1. знаходимо всі вузли, до яких ще можна дійти від джерела в залишковому графі
    visited = {v: False for v in final_graf}
    queue = [s_super]
    visited[s_super] = True
    idx = 0
    while idx < len(queue):
        u = queue[idx]
        idx += 1
        for v, cap in final_graf[u].items():
            if not visited[v] and cap > 0:
                visited[v] = True
                queue.append(v)

    # 2. критична дорога — це та, де один кінець доступний, а інший ні
    critical = []
    for u, v, cap in original_dorogy:
        if visited[u] and not visited[v]:
            critical.append((u, v, cap))
            
    return critical

def print_report(potiq, critical):
    """гарний вивід для звіту"""
    print(f"результат: {potiq} машин/день")
    print("критичні ділянки (треба розширити):")
    for u, v, c in critical:
        print(f"  дорога {u} -> {v} (забита на {c} машин)")

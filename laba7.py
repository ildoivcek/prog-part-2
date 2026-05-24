import csv
from collections import deque

def load_data(path):
    #читаємо csv і витягуємо списки ферм, магазинів і доріг
    with open(path, mode="r", encoding="utf-8") as f:
        r = csv.reader(f)
        fermy = [i.strip() for i in next(r)]
        magazy = [i.strip() for i in next(r)]
        dorogy = []
        for row in r:
            if row:
                dorogy.append((row[0].strip(), row[1].strip(), int(row[2].strip())))
    return fermy, magazy, dorogy

def bfs(graf, s, t, parent):
    #шукаємо шлях через bfs у залишковому графі
    visited = {v: False for v in graf}
    queue = deque([s])
    visited[s] = True
    while queue:
        u = queue.popleft()
        for v, cap in graf[u].items():
            if not visited[v] and cap > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == t: return True
    return False

def get_max_flow(fermy, magazy, dorogy):
    #рахуємо макс потік і повертаємо результат разом із фінальним графом
    vuzly = set()
    for u, v, _ in dorogy: vuzly.update([u, v])
    vuzly.update(fermy + magazy)

    s_super = "super_source"
    t_super = "super_sink"
    
    # будуємо граф (початковий і залишковий одночасно)
    graf = {v: {} for v in vuzly}
    graf[s_super], graf[t_super] = {}, {}

    for f in fermy:
        graf[s_super][f] = float('inf')
        graf[f][s_super] = 0
    for m in magazy:
        if m not in graf: graf[m] = {}
        graf[m][t_super] = float('inf')
        graf[t_super][m] = 0
    for u, v, cap in dorogy:
        graf[u][v] = graf[u].get(v, 0) + cap
        if u not in graf[v]: graf[v][u] = 0

    max_potiq = 0
    parent = {}
    
    # поки є шлях — качаємо квіти
    while bfs(graf, s_super, t_super, parent):
        path_flow = float('inf')
        curr = t_super
        while curr != s_super:
            path_flow = min(path_flow, graf[parent[curr]][curr])
            curr = parent[curr]
        
        max_potiq += path_flow
        v = t_super
        while v != s_super:
            u = parent[v]
            graf[u][v] -= path_flow
            graf[v][u] += path_flow #додаємо можливість "скасувати" поїздку (зворотне ребро), якщо знайдемо кращий маршрут пізніше.
            v = parent[v]
            
    return max_potiq, graf, s_super, t_super

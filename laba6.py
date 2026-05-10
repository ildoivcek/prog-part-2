def find_unreachable_cities(cities, storages, pipelines):

    #знаходить міста до яких неможливо подати газ із кожного сховища

    #побудова графа (список суміжності)
    graph = {city: [] for city in cities}
    for storage in storages:
        graph[storage] = []

    for start, end in pipelines:
        if start in graph:
            graph[start].append(end)

    result = []

    #перевірка для кожного сховища
    for storage in storages:
        visited = set()

        def dfs(current_node):
            visited.add(current_node)
            for neighbor in graph.get(current_node, []):
                if neighbor not in visited:
                    dfs(neighbor) #тут транзит

        #запускаю пошук із поточного сховища
        dfs(storage)

        #знаходжу міста які не були відвідані
        unreachable = [city for city in cities if city not in visited]

        if unreachable:
            result.append([storage, unreachable])

    return result

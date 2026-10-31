def ao_star(graph, heuristic, node):
    if node not in graph or not graph[node]:
        return heuristic[node]

    min_cost = float('inf')
    best_path = None

    for option in graph[node]:
        cost = 0

        for child in option:
            cost += heuristic[child] + 1

        if cost < min_cost:
            min_cost = cost
            best_path = option

    heuristic[node] = min_cost

    print("Node:", node)
    print("Best Path:", best_path)
    print("Minimum Cost:", min_cost)

    for child in best_path:
        ao_star(graph, heuristic, child)

    return min_cost


graph = {
    'A': [['B', 'C'], ['D']],
    'B': [['E'], ['F']],
    'C': [['G']],
    'D': [['H', 'I']],
    'E': [],
    'F': [],
    'G': [],
    'H': [],
    'I': []
}

heuristic = {
    'A': 10,
    'B': 4,
    'C': 3,
    'D': 5,
    'E': 2,
    'F': 3,
    'G': 1,
    'H': 2,
    'I': 2
}

print("AO* Search Result")
cost = ao_star(graph, heuristic, 'A')

print("Final Cost:", cost)

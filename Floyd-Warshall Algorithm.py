def floyd_warshall(graph):
    vertices = list(graph.keys())
    distance = {v: {w: float('infinity') for w in vertices} for v in vertices}
    
    for v in vertices:
        distance[v][v] = 0

    for v in vertices:
        for w in graph[v]:
            distance[v][w] = graph[v][w]

    for k in vertices:
        for i in vertices:
            for j in vertices:
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance

# Example usage
graph = {
    'A': {'B': 3, 'D': 7},
    'B': {'C': 1},
    'C': {'A': 8, 'D': 2},
    'D': {'C': 5}
}

print(floyd_warshall(graph))

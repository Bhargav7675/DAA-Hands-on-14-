import heapq

def dijkstra(graph, start):
    # Shortest paths is a dict of nodes whose value is a tuple of (previous node, shortest distance)
    shortest_paths = {vertex: (None, float('infinity')) for vertex in graph}
    shortest_paths[start] = (None, 0)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Nodes can only be visited once. We check if we have visited a node already.
        if current_distance > shortest_paths[current_vertex][1]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < shortest_paths[neighbor][1]:
                shortest_paths[neighbor] = (current_vertex, distance)
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return shortest_paths

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

print(dijkstra(graph, 'A'))
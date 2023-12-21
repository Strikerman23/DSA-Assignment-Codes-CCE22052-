1.PYTHON CODE FOR DIJIKSTRA's ALGORITHM
import heapq

def dijkstra(graph, start):
    # Initialize distances with infinity for all nodes except the start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue to track nodes and their tentative distances
    pq = [(0, start)]
    
    total_dist = 0
    paths = {node: [] for node in graph}
    
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        
        # If current distance is greater than the known distance, skip
        if curr_dist > distances[curr_node]:
            continue
        
        for neighbor, weight in graph[curr_node].items():
            dist = curr_dist + weight
            if dist < distances[neighbor]:
                distances[neighbor] = dist
                # Update the path with the current shortest path
                paths[neighbor] = paths[curr_node] + [curr_node]
                heapq.heappush(pq, (dist, neighbor))
    
    shortest_paths = {}
    for node, path in paths.items():
        if node != start and distances[node] != float('inf'):
            shortest_paths[node] = [start] + path + [node]
    
    for node, dist in distances.items():
        if dist != float('inf'):
            total_dist += dist
    
    return distances, total_dist, shortest_paths

# Different Test Case
new_graph = {
    'X': {'Y': 7, 'Z': 2},
    'Y': {'X': 7, 'Z': 1, 'W': 4},
    'Z': {'X': 2, 'Y': 1, 'W': 6},
    'W': {'Y': 4, 'Z': 6}
}

distances, total_distance, shortest_paths = dijkstra(new_graph, 'X')
print("Distances:", distances)
print("Total Distance:", total_distance)
print("Shortest Paths:", shortest_paths)

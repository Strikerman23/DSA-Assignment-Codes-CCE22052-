3.FLOYD'S ALGORITHM
V = 5  # Number of vertices in the graph
INF = float('inf')  # Define infinity as the large enough value

def floydWarshall(graph):
    # dist[][] will store the shortest distances between every pair of vertices
    dist = [list(row) for row in graph]  # Initialize the solution matrix
    
    # For each intermediate vertex 'k', find the shortest paths between all pairs of vertices
    for k in range(V):
        for i in range(V):  # Choose source vertex 'i'
            for j in range(V):  # Choose destination vertex 'j'
                # If vertex 'k' is on the shortest path from 'i' to 'j', update dist[i][j]
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    printSolution(dist)

def printSolution(dist):
    print("Shortest distances between every pair of vertices:")
    for i in range(V):
        for j in range(V):
            print(f"{dist[i][j]:^7}", end=' ') if dist[i][j] != INF else print(" INF ", end=' ')
        print()

# Different test case
graph = [
    [0, 3, 8, INF, -4],
    [INF, 0, INF, 1, 7],
    [INF, 4, 0, INF, INF],
    [2, INF, -5, 0, INF],
    [INF, INF, INF, 6, 0]
]

# Function call
floydWarshall(graph)

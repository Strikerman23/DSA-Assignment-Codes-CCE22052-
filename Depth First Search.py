#5.Depth First Search:
from collections import defaultdict

class Graph:
    # Constructor
    def __init__(self):
        # Default dictionary to store graph
        self.graph = defaultdict(list)

    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, v, visited):
        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')

        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):
        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)

# Driver's code
if __name__ == "__main__":
    # Create a more complex graph with disconnected components
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 4)
    g.addEdge(2, 5)
    g.addEdge(3, 6)
    g.addEdge(6, 7)
    g.addEdge(7, 8)

    # Test with a different starting vertex in a disconnected component
    print("DFS from vertex 3 (disconnected component):")
    g.DFS(3)

    # Explore all connected components
    print("\nDFS for all connected components:")
    visited = set()  # Reset visited set
    for vertex in range(9):
        if vertex not in visited:
            g.DFS(vertex)

#4."Breadth-First Search (BFS) Algorithm for Graph" 
from collections import defaultdict

class Graph:
    def __init__(self):
        # Default dictionary to store the graph
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        # Function to add an edge to the graph
        self.graph[u].append(v)

    def breadth_first_search(self, start):
        # Function to perform Breadth-First Search (BFS) traversal
        visited = [False] * (max(self.graph) + 1)
        queue = []

        queue.append(start)
        visited[start] = True

        print("Breadth First Traversal (starting from vertex", start, "):", end=" ")

        while queue:
            current_vertex = queue.pop(0)
            print(current_vertex, end=" ")

            for adjacent_vertex in self.graph[current_vertex]:
                if not visited[adjacent_vertex]:
                    queue.append(adjacent_vertex)
                    visited[adjacent_vertex] = True

# Driver code
if __name__ == '__main__':
    # Create a different example graph
    example_graph = Graph()
    example_graph.add_edge(0, 1)
    example_graph.add_edge(0, 2)
    example_graph.add_edge(1, 2)
    example_graph.add_edge(1, 3)
    example_graph.add_edge(2, 4)
    example_graph.add_edge(3, 4)
    example_graph.add_edge(4, 0)

    # Perform BFS starting from vertex 0
    example_graph.breadth_first_search(0)

#7.KRUSKAL's ALGORITHM
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = []  # List to store edges as [source, destination, weight] tuples

    def add_edge(self, vertex1, vertex2, weight):
        self.edges.append([vertex1, vertex2, weight])

    def find_set(self, parent, vertex):
        """Finds the set to which a vertex belongs, using path compression."""
        if parent[vertex] != vertex:
            parent[vertex] = self.find_set(parent, parent[vertex])
        return parent[vertex]

    def union_sets(self, parent, rank, set1, set2):
        """Combines two sets using union by rank."""
        if rank[set1] < rank[set2]:
            parent[set1] = set2
        elif rank[set1] > rank[set2]:
            parent[set2] = set1
        else:
            parent[set2] = set1
            rank[set1] += 1

    def kruskal_mst(self):
        """Constructs the minimum spanning tree using Kruskal's algorithm."""
        minimum_spanning_tree = []
        edges_in_mst = 0

        # Sort edges by weight in non-decreasing order
        sorted_edges = sorted(self.edges, key=lambda edge: edge[2])

        parent = [vertex for vertex in range(self.num_vertices)]  # Initialize disjoint sets
        rank = [0] * self.num_vertices  # Initialize ranks for union by rank

        while edges_in_mst < self.num_vertices - 1:
            # Pick the smallest edge
            edge = sorted_edges[edges_in_mst]
            vertex1, vertex2, weight = edge

            # Check if adding this edge creates a cycle
            set1 = self.find_set(parent, vertex1)
            set2 = self.find_set(parent, vertex2)

            if set1 != set2:
                # Add the edge to the MST
                minimum_spanning_tree.append(edge)
                edges_in_mst += 1
                self.union_sets(parent, rank, set1, set2)

        # Print the MST edges and total weight
        total_weight = 0
        print("Edges in the constructed MST:")
        for edge in minimum_spanning_tree:
            total_weight += edge[2]
            print("{} -- {} == {}".format(edge[0], edge[1], edge[2]))
        print("Minimum Spanning Tree Weight:", total_weight)

# Test Case 2
if __name__ == '__main__':
    graph = Graph(5)
    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 3, 6)
    graph.add_edge(1, 2, 3)
    graph.add_edge(1, 3, 8)
    graph.add_edge(1, 4, 5)
    graph.add_edge(2, 4, 7)
    graph.add_edge(3, 4, 9)

    graph.kruskal_mst()

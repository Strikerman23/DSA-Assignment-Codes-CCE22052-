#6.Prim's Algorithm
import sys

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    def print_mst(self, parent):
        print("Edge \tWeight")
        for vertex in range(1, self.num_vertices):
            print(f"{parent[vertex]} - {vertex} \t {self.adjacency_matrix[vertex][parent[vertex]]}")

    def find_min_key_vertex(self, key, mst_set):
        min_value = sys.maxsize
        min_index = -1
        for vertex in range(self.num_vertices):
            if key[vertex] < min_value and mst_set[vertex] is False:
                min_value = key[vertex]
                min_index = vertex
        return min_index

    def prim_mst(self):
        key = [sys.maxsize] * self.num_vertices
        parent = [None] * self.num_vertices
        mst_set = [False] * self.num_vertices

        key[0] = 0  # Start from vertex 0
        parent[0] = -1  # Make it the root of MST

        for _ in range(self.num_vertices - 1):
            u = self.find_min_key_vertex(key, mst_set)
            mst_set[u] = True

            for vertex in range(self.num_vertices):
                if self.adjacency_matrix[u][vertex] > 0 and mst_set[vertex] is False and key[vertex] > self.adjacency_matrix[u][vertex]:
                    key[vertex] = self.adjacency_matrix[u][vertex]
                    parent[vertex] = u

        self.print_mst(parent)

# Different test case
if __name__ == '__main__':
    g = Graph(9)
    g.adjacency_matrix = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
    ]
    g.prim_mst()

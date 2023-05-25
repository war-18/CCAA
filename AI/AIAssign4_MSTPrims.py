import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def min_key(self, key, mst_set):
        min_val = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_index = v
        return min_index

    def prim_mst(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mst_set = [False] * self.V

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not mst_set[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        # Print the constructed MST
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

# Take input from the user
V = int(input("Enter the number of vertices: "))
graph = Graph(V)

# Input the adjacency matrix
print("Enter the adjacency matrix (space-separated):")
for i in range(V):
    row = list(map(int, input().split()))
    for j in range(V):
        graph.graph[i][j] = row[j]

# Find and print the minimum spanning tree
print("Prim's Minimal Spanning Tree:")
graph.prim_mst()

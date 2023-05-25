class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal_mst(self):
        result = []
        i = 0
        e = 0

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        # Print the constructed MST
        print("Edge \tWeight")
        for u, v, w in result:
            print(u, "-", v, "\t", w)

# Take input from the user
V = int(input("Enter the number of vertices: "))
E = int(input("Enter the number of edges: "))

graph = Graph(V)

# Input the edges and weights
print("Enter the edges and weights (u v w) separated by spaces:")
for _ in range(E):
    u, v, w = map(int, input().split())
    graph.add_edge(u, v, w)

# Find and print the minimum spanning tree
print("Kruskal's Minimal Spanning Tree:")
graph.kruskal_mst()

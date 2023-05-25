from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, v, visited):
        visited.add(v)
        print(v, end=" ")

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, v):
        visited = set()
        queue = []

        visited.add(v)
        queue.append(v)

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


# Create a graph
graph = Graph()

# Take input from the user to add edges to the graph
num_edges = int(input("Enter the number of edges: "))
for _ in range(num_edges):
    u, v = input("Enter the edge (u v): ").split()
    graph.add_edge(u, v)

# Take input for the starting vertex
start_vertex = input("Enter the starting vertex: ")

# Perform DFS
print("Depth First Search (DFS):")
visited = set()
graph.dfs(start_vertex, visited)
print()

# Perform BFS
print("Breadth First Search (BFS):")
graph.bfs(start_vertex)
print()


'''
testcase:
Enter the number of edges: 5
Enter the edge (u v): A B
Enter the edge (u v): A C
Enter the edge (u v): B D
Enter the edge (u v): C E
Enter the edge (u v): D E
Enter the starting vertex: A
'''
import sys

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def find_min_distance(self, distances, visited):
        min_distance = sys.maxsize
        min_index = -1

        for v in range(self.vertices):
            if distances[v] < min_distance and not visited[v]:
                min_distance = distances[v]
                min_index = v

        return min_index

    def dijkstra(self, source):
        distances = [sys.maxsize] * self.vertices
        distances[source] = 0
        visited = [False] * self.vertices

        for _ in range(self.vertices):
            u = self.find_min_distance(distances, visited)
            visited[u] = True

            for v in range(self.vertices):
                if self.graph[u][v] > 0 and not visited[v] and distances[v] > distances[u] + self.graph[u][v]:
                    distances[v] = distances[u] + self.graph[u][v]

        return distances

# Example usage
if __name__ == '__main__':
    # Get number of vertices from user
    num_vertices = int(input("Enter the number of vertices: "))

    # Create a graph
    graph = Graph(num_vertices)

    # Get the adjacency matrix from the user
    print("Enter the adjacency matrix (separated by space):")
    for i in range(num_vertices):
        row = list(map(int, input().split()))
        for j in range(num_vertices):
            graph.graph[i][j] = row[j]

    # Get source vertex
    source_vertex = int(input("Enter the source vertex: "))

    # Apply Dijkstra's algorithm
    shortest_distances = graph.dijkstra(source_vertex)

    # Print the shortest distance from source to all vertices
    print("Shortest distances from the source vertex:")
    for v in range(num_vertices):
        print(f"Vertex {v}: {shortest_distances[v]}")

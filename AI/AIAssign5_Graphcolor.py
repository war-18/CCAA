def is_safe(vertex, color, graph, color_assignment):
    # Check if it is safe to assign the color to the vertex

    for v in graph[vertex]:
        if color_assignment[v] == color:
            return False

    return True


def graph_coloring(graph, colors):
    num_vertices = len(graph)
    color_assignment = [-1] * num_vertices

    def backtrack(vertex):
        # Base case: All vertices are assigned colors
        if vertex == num_vertices:
            return True

        for color in colors:
            if is_safe(vertex, color, graph, color_assignment):
                color_assignment[vertex] = color  # Assign the color

                if backtrack(vertex + 1):  # Recursive call
                    return True

                color_assignment[vertex] = -1  # Backtrack if solution not found

        return False

    if not backtrack(0):
        print("No solution exists.")
    else:
        print("Color assignment:")
        for vertex, color in enumerate(color_assignment):
            print(f"Vertex {vertex+1}: Color {color}")


# Taking input from the user
num_vertices = int(input("Enter the number of vertices: "))
num_edges = int(input("Enter the number of edges: "))

graph = [[] for _ in range(num_vertices)]
print("Enter the edges in the format 'vertex1 vertex2', one edge per line:")
for _ in range(num_edges):
    v1, v2 = map(int, input().split())
    graph[v1 - 1].append(v2 - 1)
    graph[v2 - 1].append(v1 - 1)

num_colors = int(input("Enter the number of colors: "))
colors = list(range(1, num_colors + 1))

graph_coloring(graph, colors)




'''
Enter the number of vertices: 5
Enter the number of edges: 6
Enter the edges in the format 'vertex1 vertex2', one edge per line:
1 2
1 3
2 3
2 4
3 4
4 5
Enter the number of colors: 3

'''
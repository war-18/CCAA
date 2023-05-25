#include <bits/stdc++.h>
using namespace std;

class Graph {
    unordered_map<char, unordered_set<char>> graph;

public:
    void addEdge(char u, char v) {
        graph[u].insert(v);
        graph[v].insert(u);
    }

    void dfs(char v, unordered_set<char>& visited) {
        visited.insert(v);
        cout << v << " ";

        for (char neighbor : graph[v]) {
            if (visited.find(neighbor) == visited.end()) {
                dfs(neighbor, visited);
            }
        }
    }

    void bfs(char v) {
        unordered_set<char> visited;
        queue<char> q;

        visited.insert(v);
        q.push(v);

        while (!q.empty()) {
            char vertex = q.front();
            q.pop();
            cout << vertex << " ";

            for (char neighbor : graph[vertex]) {
                if (visited.find(neighbor) == visited.end()) {
                    visited.insert(neighbor);
                    q.push(neighbor);
                }
            }
        }
    }
};

int main() {
    Graph graph;

    // Take input from the user to add edges to the graph
    int num_edges;
    cout << "Enter the number of edges: ";
    cin >> num_edges;

    cout << "Enter the edges (u v): " << endl;
    for (int i = 0; i < num_edges; i++) {
        char u, v;
        cin >> u >> v;
        graph.addEdge(u, v);
    }

    // Take input for the starting vertex
    char start_vertex;
    cout << "Enter the starting vertex: ";
    cin >> start_vertex;

    // Perform DFS
    cout << "Depth First Search (DFS):" << endl;
    unordered_set<char> visited;
    graph.dfs(start_vertex, visited);
    cout << endl;

    // Perform BFS
    cout << "Breadth First Search (BFS):" << endl;
    graph.bfs(start_vertex);
    cout << endl;

    return 0;
}




/*
testcase:
Enter the number of edges: 5
Enter the edge (u v): A B
Enter the edge (u v): A C
Enter the edge (u v): B D
Enter the edge (u v): C E
Enter the edge (u v): D E
Enter the starting vertex: A
*/
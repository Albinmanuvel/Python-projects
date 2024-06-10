def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")

    for next_node in graph[start]:
        if next_node not in visited:
            dfs(graph, next_node, visited)

# Example :
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Depth-First Search:")
dfs(graph, 'A')
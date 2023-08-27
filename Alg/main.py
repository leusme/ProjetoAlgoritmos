import pandas as pd

url = "https://www.inf.pucrs.br/~danielc/peng1a/outros/distancias.xls"
df = pd.read_excel(url)

vertices = list(df.columns)

graph = {vertex: {} for vertex in vertices}

def prim(graph):
    start_vertex = vertices[0]
    visited = {vertex: False for vertex in vertices}
    distances = {vertex: float('inf') for vertex in vertices}
    parent = {vertex: None for vertex in vertices}

    distances[start_vertex] = 0

    for _ in range(len(vertices)):
        current_vertex = find_min_vertex(distances, visited)
        visited[current_vertex] = True

        for neighbor, weight in graph[current_vertex].items():
            if not visited[neighbor] and weight < distances[neighbor]:
                distances[neighbor] = weight
                parent[neighbor] = current_vertex

    mst = {vertex: {} for vertex in vertices}
    for vertex, par in parent.items():
        if par is not None:
            mst[vertex][par] = distances[vertex]
            mst[par][vertex] = distances[vertex]

    return mst

def find_min_vertex(distances, visited):
    min_vertex = None
    min_distance = float('inf')

    for vertex in distances:
        if not visited[vertex] and distances[vertex] < min_distance:
            min_vertex = vertex
            min_distance = distances[vertex]

    return min_vertex

minimum_spanning_tree = prim(graph)

for vertex, neighbors in minimum_spanning_tree.items():
    for neighbor, weight in neighbors.items():
        print(f"{vertex} - {neighbor}: {weight}")

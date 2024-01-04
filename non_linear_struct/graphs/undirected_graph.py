class GraphUndirected:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def display(self):
        for vertex in self.graph:
            print(vertex, "->", " -> ".join(map(str, self.graph[vertex])))


# Exemplo de uso do Grafo Não-direcionado
graph = GraphUndirected()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)

print("Grafo Não-direcionado:")
graph.display()

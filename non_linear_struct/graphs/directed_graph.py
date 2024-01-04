class GraphDirected:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def display(self):
        for vertex in self.graph:
            print(vertex, "->", " -> ".join(map(str, self.graph[vertex])))


# Exemplo de uso do Grafo Direcionado
graph = GraphDirected()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)

print("Grafo Direcionado:")
graph.display()

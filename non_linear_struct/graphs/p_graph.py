from collections import defaultdict


class GraphWeightedDirected:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))

    def display(self):
        for vertex in self.graph:
            print(vertex, "->", " -> ".join(f"{v}:{w}" for v, w in self.graph[vertex]))


# Exemplo de uso do Grafo Ponderado Direcionado
graph = GraphWeightedDirected()
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 2, 2)
graph.add_edge(2, 3, 7)

print("Grafo Ponderado Direcionado:")
graph.display()

# Não Direcionado


class GraphWeightedUndirected:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Para grafos não direcionados

    def display(self):
        for vertex in self.graph:
            print(vertex, "->", " -> ".join(f"{v}:{w}" for v, w in self.graph[vertex]))


# Exemplo de uso do Grafo Ponderado Não Direcionado
graph = GraphWeightedUndirected()
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 2, 2)
graph.add_edge(2, 3, 7)

print("Grafo Ponderado Não Direcionado:")
graph.display()

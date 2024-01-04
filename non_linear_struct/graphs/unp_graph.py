from collections import defaultdict


class GraphUnweightedDirected:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def display(self):
        for vertex in self.graph:
            print(vertex, "->", " -> ".join(map(str, self.graph[vertex])))


# Exemplo de uso do Grafo Não Ponderado Direcionado
graph = GraphUnweightedDirected()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)

print("Grafo Não Ponderado Direcionado:")
graph.display()

# Não Direcionado


class GraphUnweightedUndirected:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Para grafos não direcionados

    def display(self):
        for vertex in self.graph:
            print(vertex, "->", " -> ".join(map(str, self.graph[vertex])))


# Exemplo de uso do Grafo Não Ponderado Não Direcionado
graph = GraphUnweightedUndirected()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)

print("Grafo Não Ponderado Não Direcionado:")
graph.display()

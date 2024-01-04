class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # Adicionando uma aresta para grafos não direcionados

    def is_cyclic_util(self, v, visited, parent):
        visited[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                if self.is_cyclic_util(i, visited, v):
                    return True
            elif parent != i:
                return True

        return False

    def is_cyclic(self):
        visited = {node: False for node in self.graph}

        for node in self.graph:
            if not visited[node]:
                if self.is_cyclic_util(node, visited, -1):
                    return True

        return False


# Exemplo de um Grafo Cíclico
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)

if g.is_cyclic():
    print("O grafo é cíclico")
else:
    print("O grafo não é cíclico")

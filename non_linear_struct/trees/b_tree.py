class Node:
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.keys = []
        self.child = []


class BTree:
    def __init__(self, t):
        self.root = Node()
        self.t = t  # Grau mínimo da árvore

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = Node()
            temp.child.insert(0, root)
            self._split_child(temp, 0)
            self._insert_non_full(temp, k)
            self.root = temp
        else:
            self._insert_non_full(root, k)

    def _insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(0)
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self._split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self._insert_non_full(x.child[i], k)

    def _split_child(self, x, i):
        t = self.t
        y = x.child[i]
        z = Node(leaf=y.leaf)

        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t : (2 * t - 1)]
        y.keys = y.keys[0 : (t - 1)]

        if not y.leaf:
            z.child = y.child[t : (2 * t)]
            y.child = y.child[0 : (t - 1)]

    def search(self, k, x=None):
        if x is not None:
            i = 0
            while i < len(x.keys) and k > x.keys[i]:
                i += 1
            if i < len(x.keys) and k == x.keys[i]:
                return (x, i)
            elif x.leaf:
                return None
            else:
                return self.search(k, x.child[i])
        else:
            return self.search(k, self.root)

    def inorder_traverse(self, x=None):
        if x is not None:
            i = 0
            while i < len(x.keys):
                if not x.leaf:
                    self.inorder_traverse(x.child[i])
                print(x.keys[i], end=" ")
                i += 1
            if not x.leaf:
                self.inorder_traverse(x.child[i])


# Exemplo de uso da Árvore B
b_tree = BTree(t=3)
keys = [
    1,
    3,
    7,
    10,
    11,
    13,
    14,
    15,
    18,
    16,
    19,
    24,
    25,
    26,
    21,
    4,
    5,
    20,
    22,
    2,
    17,
    12,
    6,
    8,
    23,
    9,
]
for key in keys:
    b_tree.insert(key)

print("Inorder traversal da Árvore B:")
b_tree.inorder_traverse()

class Node:
    def __init__(self, key, color):
        self.key = key
        self.left = None
        self.right = None
        self.color = color  # 'R' for Red, 'B' for Black


class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)
        self.root.color = "B"  # Root sempre preto

    def _insert_recursive(self, root, key):
        if not root:
            return Node(key, "R")

        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        else:
            root.right = self._insert_recursive(root.right, key)

        # Realiza rotações e ajustes de cores para manter as propriedades da árvore rubro-negra
        if self._is_red(root.right) and not self._is_red(root.left):
            root = self._rotate_left(root)
        if self._is_red(root.left) and self._is_red(root.left.left):
            root = self._rotate_right(root)
        if self._is_red(root.left) and self._is_red(root.right):
            self._flip_colors(root)

        return root

    def _is_red(self, node):
        return node is not None and node.color == "R"

    def _rotate_left(self, root):
        x = root.right
        root.right = x.left
        x.left = root
        x.color = root.color
        root.color = "R"
        return x

    def _rotate_right(self, root):
        x = root.left
        root.left = x.right
        x.right = root
        x.color = root.color
        root.color = "R"
        return x

    def _flip_colors(self, root):
        root.color = "R"
        root.left.color = "B"
        root.right.color = "B"

    def inorder_traversal(self):
        self._inorder_traversal_recursive(self.root)
        print()

    def _inorder_traversal_recursive(self, root):
        if root:
            self._inorder_traversal_recursive(root.left)
            print(root.key, end=" ")
            self._inorder_traversal_recursive(root.right)


# Exemplo de uso da Árvore Rubro-Negra
rb_tree = RedBlackTree()
keys = [7, 3, 18, 10, 22, 8, 11, 26]
for key in keys:
    rb_tree.insert(key)

print("Inorder traversal da Árvore Rubro-Negra:")
rb_tree.inorder_traversal()

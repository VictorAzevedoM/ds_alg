class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        hash_key = self._hash_function(key)
        found = False
        for index, element in enumerate(self.hash_table[hash_key]):
            if len(element) == 2 and element[0] == key:
                self.hash_table[hash_key][index] = (key, value)
                found = True
                break
        if not found:
            self.hash_table[hash_key].append((key, value))

    def search(self, key):
        hash_key = self._hash_function(key)
        for element in self.hash_table[hash_key]:
            if element[0] == key:
                return element[1]
        return None

    def delete(self, key):
        hash_key = self._hash_function(key)
        for index, element in enumerate(self.hash_table[hash_key]):
            if element[0] == key:
                del self.hash_table[hash_key][index]
                break


# Exemplo de uso da Tabela de Hash
hash_table = HashTable(10)
hash_table.insert(10, "Python")
hash_table.insert(20, "Java")
hash_table.insert(30, "C++")

print("Valor associado à chave 20:", hash_table.search(20))

hash_table.delete(20)
print("Valor associado à chave 20 após a exclusão:", hash_table.search(20))

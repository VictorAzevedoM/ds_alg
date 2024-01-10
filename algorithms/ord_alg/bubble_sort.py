#O Bubble Sort é um algoritmo simples de ordenação que percorre a lista várias vezes, 
#comparando elementos adjacentes e trocando-os se estiverem na ordem errada.


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Exemplo de uso:
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Array ordenado:", arr)

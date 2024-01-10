"""
O Selection Sort percorre a lista várias vezes, 
dividindo-a em duas partes: a parte ordenada e a parte não ordenada. 
Ele busca o menor elemento na parte não ordenada e o coloca no início da parte não ordenada.
Esse processo é repetido até que toda a lista esteja ordenada.
"""


def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_idx = i

        # Encontra o índice do menor elemento não ordenado
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Troca o menor elemento com o primeiro elemento não ordenado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


# Exemplo de uso do Selection Sort
arr = [64, 25, 12, 22, 11]
print("Array original:", arr)

sorted_arr = selection_sort(arr)
print("Array ordenado:", sorted_arr)

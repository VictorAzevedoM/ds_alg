"""
O Insertion Sort percorre a lista, começando do segundo elemento, e insere cada elemento na posição correta na parte ordenada da lista, 
deslocando os elementos maiores para a direita para abrir espaço para a inserção.
"""


def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Move os elementos da lista que são maiores que a chave para uma posição à frente
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# Exemplo de uso do Insertion Sort
arr = [64, 25, 12, 22, 11]
print("Array original:", arr)

sorted_arr = insertion_sort(arr)
print("Array ordenado:", sorted_arr)

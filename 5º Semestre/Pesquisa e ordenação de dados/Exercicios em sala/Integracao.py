import time
import random

# -------- MEDIANA DE TRÊS --------
def selecionaMediana(arr, inicio, fim):
    mid = (inicio + fim) // 2

    if arr[inicio] > arr[mid]:
        arr[inicio], arr[mid] = arr[mid], arr[inicio]

    if arr[mid] > arr[fim]:
        arr[mid], arr[fim] = arr[fim], arr[mid]

    if arr[inicio] > arr[mid]:
        arr[inicio], arr[mid] = arr[mid], arr[inicio]

    arr[mid], arr[fim] = arr[fim], arr[mid]

    return arr[fim]

# -------- PARTITION (LOMUTO) --------
def partition(arr, inicio, fim):
    pivot = selecionaMediana(arr, inicio, fim)

    i = inicio - 1

    for j in range(inicio, fim):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[fim] = arr[fim], arr[i + 1]
    return i + 1

# -------- QUICK SORT --------
def quicksort(arr, inicio, fim):
    if inicio < fim:
        pi = partition(arr, inicio, fim)
        quicksort(arr, inicio, pi - 1)
        quicksort(arr, pi + 1, fim)

# -------- TESTE --------
arr = [random.randint(0, 10000) for _ in range(10000)]

inicio = time.perf_counter()
quicksort(arr, 0, len(arr) - 1)
fim = time.perf_counter()

print(f"Tempo (Quick Sort + Mediana): {fim - inicio:.5f} segundos")
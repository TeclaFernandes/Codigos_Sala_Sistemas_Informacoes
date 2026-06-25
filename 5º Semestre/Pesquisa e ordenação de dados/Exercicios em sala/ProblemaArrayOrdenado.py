import sys
import time

def partition(arr, inicio, fim):
    pivot = arr[fim]
    i = inicio - 1

    for j in range(inicio, fim):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[fim] = arr[fim], arr[i + 1]
    return i + 1

def quicksort(arr, inicio, fim):
    if inicio < fim:
        pi = partition(arr, inicio, fim)
        quicksort(arr, inicio, pi - 1)
        quicksort(arr, pi + 1, fim)

arr = list(range(10000))  # array já ordenado

sys.setrecursionlimit(20000)

inicio = time.time()
quicksort(arr, 0, len(arr) - 1)
fim = time.time()

print(f"Tempo de execução: {fim - inicio:.5f} segundos")

inicio = time.perf_counter()
quicksort(arr, 0, len(arr) - 1)
fim = time.perf_counter()

print(f"Tempo: {fim - inicio:.5f}s")
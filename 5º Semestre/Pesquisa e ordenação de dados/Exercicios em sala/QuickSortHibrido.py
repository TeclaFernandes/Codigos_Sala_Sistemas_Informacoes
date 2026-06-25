import random
import time

# -------- INSERTION SORT --------
def insertion_sort(arr, inicio, fim):
    for i in range(inicio + 1, fim + 1):
        key = arr[i]
        j = i - 1

        while j >= inicio and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

# -------- PARTITION (Lomuto) --------
def partition(arr, inicio, fim):
    pivot = arr[fim]
    i = inicio - 1

    for j in range(inicio, fim):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[fim] = arr[fim], arr[i + 1]
    return i + 1

# -------- PARTITION ALEATÓRIO --------
def randomized_partition(arr, inicio, fim):
    pivot_index = random.randint(inicio, fim)
    arr[pivot_index], arr[fim] = arr[fim], arr[pivot_index]
    return partition(arr, inicio, fim)

# -------- QUICK SORT HÍBRIDO --------
def quicksort_hybrid(arr, inicio, fim, threshold=10):
    if inicio < fim:

        if fim - inicio + 1 <= threshold:
            insertion_sort(arr, inicio, fim)
            return

        pi = randomized_partition(arr, inicio, fim)

        quicksort_hybrid(arr, inicio, pi - 1, threshold)
        quicksort_hybrid(arr, pi + 1, fim, threshold)

# -------- TESTE --------
arr = [random.randint(0, 10000) for _ in range(10000)]

inicio = time.perf_counter()
quicksort_hybrid(arr, 0, len(arr) - 1)
fim = time.perf_counter()

print(f"Tempo de execução (Quick Sort Híbrido): {fim - inicio:.5f} segundos")
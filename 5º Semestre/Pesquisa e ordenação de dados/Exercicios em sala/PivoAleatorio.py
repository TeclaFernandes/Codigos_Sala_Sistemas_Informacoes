import random
import time

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

# -------- QUICK SORT RANDOMIZADO --------
def quicksort_random(arr, inicio, fim):
    if inicio < fim:
        pi = randomized_partition(arr, inicio, fim)
        quicksort_random(arr, inicio, pi - 1)
        quicksort_random(arr, pi + 1, fim)

# -------- TESTE --------
arr = list(range(10000))  # caso pior (ordenado)

inicio = time.perf_counter()
quicksort_random(arr, 0, len(arr) - 1)
fim = time.perf_counter()

print(f"Tempo de execução (Randomized Quick Sort): {fim - inicio:.5f} segundos")
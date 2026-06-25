import time
import sys

sys.setrecursionlimit(100000)

depth_counter_standard = 0
max_depth_standard = 0

depth_counter_median = 0
max_depth_median = 0

def partition_standard(arr, inicio, fim):
    pivot = arr[fim]
    i = inicio - 1

    for j in range(inicio, fim):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[fim] = arr[fim], arr[i + 1]
    return i + 1

def quicksort_standard(arr, inicio, fim, depth=0):
    global depth_counter_standard, max_depth_standard

    if inicio < fim:
        depth_counter_standard += 1
        max_depth_standard = max(max_depth_standard, depth)

        pi = partition_standard(arr, inicio, fim)

        quicksort_standard(arr, inicio, pi - 1, depth + 1)
        quicksort_standard(arr, pi + 1, fim, depth + 1)

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

def partition_median(arr, inicio, fim):
    pivot = selecionaMediana(arr, inicio, fim)

    i = inicio - 1

    for j in range(inicio, fim):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[fim] = arr[fim], arr[i + 1]
    return i + 1

def quicksort_median(arr, inicio, fim, depth=0):
    global depth_counter_median, max_depth_median

    if inicio < fim:
        depth_counter_median += 1
        max_depth_median = max(max_depth_median, depth)

        pi = partition_median(arr, inicio, fim)

        quicksort_median(arr, inicio, pi - 1, depth + 1)
        quicksort_median(arr, pi + 1, fim, depth + 1)

N = 50000
arr_base = list(range(N))  # já ordenado

# -------- padrão --------
arr1 = arr_base.copy()

start = time.perf_counter()
quicksort_standard(arr1, 0, N - 1)
end = time.perf_counter()

print("=== QUICK SORT PADRÃO ===")
print(f"Tempo: {end - start:.5f}s")
print(f"Profundidade máxima: {max_depth_standard}")

# -------- mediana --------
arr2 = arr_base.copy()

start = time.perf_counter()
quicksort_median(arr2, 0, N - 1)
end = time.perf_counter()

print("\n=== QUICK SORT MEDIANA DE 3 ===")
print(f"Tempo: {end - start:.5f}s")
print(f"Profundidade máxima: {max_depth_median}")
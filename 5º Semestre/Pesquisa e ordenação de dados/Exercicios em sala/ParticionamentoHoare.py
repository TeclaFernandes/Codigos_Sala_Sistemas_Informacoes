import random
import copy

# ---------- Lomuto (com contagem de swaps) ----------
def lomuto_partition(arr, inicio, fim, status):
    pivot = arr[fim]
    i = inicio - 1

    for j in range(inicio, fim):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            status["swaps"] += 1

    arr[i + 1], arr[fim] = arr[fim], arr[i + 1]
    status["swaps"] += 1

    return i + 1


def quicksort_lomuto(arr, inicio, fim, status):
    if inicio < fim:
        pi = lomuto_partition(arr, inicio, fim, status)
        quicksort_lomuto(arr, inicio, pi - 1, status)
        quicksort_lomuto(arr, pi + 1, fim, status)

# ---------- Hoare (com contagem de swaps) ----------
def hoare_partition(arr, inicio, fim, status):
    pivot = arr[inicio]
    i = inicio - 1
    j = fim + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]
        status["swaps"] += 1


def quicksort_hoare(arr, inicio, fim, status):
    if inicio < fim:
        p = hoare_partition(arr, inicio, fim, status)
        quicksort_hoare(arr, inicio, p, status)
        quicksort_hoare(arr, p + 1, fim, status)

# ---------- Comparação (mesmo array) ----------
arr_base = [random.randint(0, 10000) for _ in range(10000)]

arr1 = copy.deepcopy(arr_base)
stats_lomuto = {"swaps": 0}

quicksort_lomuto(arr1, 0, len(arr1) - 1, stats_lomuto)

arr2 = copy.deepcopy(arr_base)
stats_hoare = {"swaps": 0}

quicksort_hoare(arr2, 0, len(arr2) - 1, stats_hoare)

print("Swaps Lomuto:", stats_lomuto["swaps"])
print("Swaps Hoare:", stats_hoare["swaps"])
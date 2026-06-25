def partition(arr, inicio, fim):
    pivot = arr[fim]  # pivô (último elemento)
    print(f"Pivô escolhido: {pivot}")

    i = inicio - 1

    for j in range(inicio, fim):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[fim] = arr[fim], arr[i + 1]

    print(f"Array: {arr}\n")

    return i + 1

def quicksort(arr, inicio, fim):
    if inicio < fim:
        pi = partition(arr, inicio, fim)

        quicksort(arr, inicio, pi - 1)
        quicksort(arr, pi + 1, fim)

arr = [10, 7, 8, 9, 1, 5]
quicksort(arr, 0, len(arr) - 1)

print("Array ordenado:", arr)
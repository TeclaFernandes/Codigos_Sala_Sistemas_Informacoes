def partition(arr, inicio, fim):
    pivot = arr[fim]
    i = inicio - 1 

    for j in range(inicio, fim):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[fim] = arr[fim], arr[i+1]
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

# Testes:
# A = [56, 89, 35, 5, 97, 4, 21, 7]
A = [10, 80, 30, 90, 40, 50, 70]
print("Array inicial:", A)
quickSort(A, 0, len(A) - 1)
print("Array final:", A)
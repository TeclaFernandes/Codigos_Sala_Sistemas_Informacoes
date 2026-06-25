def insertionSort(arr):
    cont = 0
    
    for i in range(1, len(arr)):
        key = arr[i]         
        j = i

        while j > 0:

            if arr[j-1] <= key:
                cont += 1
                break   
            arr[j] = arr[j-1]
            cont += 1
            j -= 1   

        arr[j] = key 

    print(cont)

arr = [1, 2, 3, 4, 5]
# arr = [5, 4, 3, 2, 1]
# arr = [3, 1, 4, 2, 5]
insertionSort(arr)
print(arr)
def count_inversions(arr):
    def merge_count(arr, left, right):
        if left >= right:
            return 0 

        mid = (left + right) // 2
        inversions = 0
        inversions += merge_count(arr, left, mid)
        inversions += merge_count(arr, mid + 1, right)

        temp = []
        i, j = left, mid + 1

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                inversions += (mid - i + 1)  
                j += 1

        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= right:
            temp.append(arr[j])
            j += 1

        for k in range(len(temp)):
            arr[left + k] = temp[k]

        return inversions

    total_inversions = merge_count(arr, 0, len(arr) - 1)
    return total_inversions, arr

A = [8, 4, 2, 1]
inversions, sorted_arr = count_inversions(A)
print("Número de inversões:", inversions)
print("Array ordenado:", sorted_arr)
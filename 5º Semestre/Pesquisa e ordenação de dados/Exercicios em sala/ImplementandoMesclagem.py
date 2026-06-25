# def mesclar(listaA, listaB, listaC):
#     i = 1
#     j = 1
#     k = 1

#     while (i <= len(listaA)) and (j <= len(listaB)):
#         if listaA[i] <= listaB[j]:
#             listaC[k] = listaA[i]
#             i = i + 1
#         else: 
#             listaC[k] = listaB[j]
#             j = j + 1
#         k = k + 1

#     while (i <= len(listaA)):
#         listaC[k] = listaA[i]
#         i = i + 1
#         k = k + 1

#     while (j <= len(listaB)):
#         listaC[k] = listaB[j]
#         j = j + 1
#         k = k + 1

#     return listaC

# listaA = [2, 5, 9]
# listaB = [1, 6, 8, 10]
# listaC = []
# result = mesclar(listaA, listaB, listaC)

def merge_sort(array):
    if len(array) <= 1:
        return array

    meio = len(array) // 2
    listaA = array[:meio]
    listaB = array[meio:]

    listaA = merge_sort(listaA)
    listaB = merge_sort(listaB)

    return merge(listaA, listaB)

def merge(listaA, listaB):
    resultado = []
    i = j = 0

    while i < len(listaA) and j < len(listaB):
        if listaA[i] <= listaB[j]:
            resultado.append(listaA[i])
            i += 1
        else:
            resultado.append(listaB[j])
            j += 1

    while i < len(listaA):
        resultado.append(listaA[i])
        i += 1

    while j < len(listaB):
        resultado.append(listaB[j])
        j += 1

    return resultado

listaA = [2, 5, 9]
listaB = [1, 6, 8, 10]
result = merge(listaA, listaB)
print(result)


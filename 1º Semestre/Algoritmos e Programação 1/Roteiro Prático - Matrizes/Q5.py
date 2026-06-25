def conta_elementos(matriz):
    total_elementos = 0
    indice = 0
    while indice < len(M):
        total_elementos += len(M[indice])
        indice += 1
    return total_elementos

M = [[2, 7], [3, 5]]

print(conta_elementos(M))
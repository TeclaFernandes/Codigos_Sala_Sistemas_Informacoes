def conta_elementos(matriz):
    indice = 0
    soma_elementos = 0
    while indice < len(M):
        for elemento in M[indice]:
            soma_elementos += elemento
        indice += 1
    return soma_elementos

M = [[2, 7], [3, 5]]

print(conta_elementos(M))
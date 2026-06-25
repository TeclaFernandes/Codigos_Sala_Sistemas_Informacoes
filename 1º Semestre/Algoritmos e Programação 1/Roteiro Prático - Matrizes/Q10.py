def somar_matrizes(matriz1, matriz2):
    matriz_soma = []
    
    for i in range(len(matriz1)):
        linha_soma = []
        for j in range(len(matriz1[0])):
            soma = matriz1[i][j] + matriz2[i][j]
            linha_soma.append(soma)
        matriz_soma.append(linha_soma)
    
    return matriz_soma

matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

matriz_resultado = somar_matrizes(matriz1, matriz2)

print("Matriz resultado da soma:")
for linha in matriz_resultado:
    print(linha)

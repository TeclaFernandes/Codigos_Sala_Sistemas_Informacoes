def ler_matriz_3x3():
    matriz = []
    print("Digite os elementos da matriz 3x3:")
    for i in range(3):
        linha = []
        for j in range(3):
            elemento = int(input(f"Elemento [{i+1}, {j+1}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

matriz_3x3 = ler_matriz_3x3()

print("Matriz 3x3:")
for linha in matriz_3x3:
    print(linha)

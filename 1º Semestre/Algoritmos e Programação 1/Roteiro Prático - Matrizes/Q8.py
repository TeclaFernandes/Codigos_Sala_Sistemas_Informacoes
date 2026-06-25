def calcular_colunas(matriz):
    if len(matriz) > 0:
        return len(matriz[0])
    else:
        return 0  # Se a matriz estiver vazia

M = [[2, 7], [3, 5]]

colunas = calcular_colunas(M)
print(f"A matriz tem {colunas} colunas.")

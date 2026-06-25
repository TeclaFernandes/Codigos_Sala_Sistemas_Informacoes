def cruzamento_maximo(A, baixo, meio, alto):
    soma_esq = float('-inf')
    soma = 0
    max_esq = meio
    for i in range(meio, baixo - 1, -1):
        soma += A[i]
        if soma > soma_esq:
            soma_esq = soma
            max_esq = i

    soma_dir = float('-inf')
    soma = 0
    max_dir = meio + 1
    for j in range(meio + 1, alto + 1):
        soma += A[j]
        if soma > soma_dir:
            soma_dir = soma
            max_dir = j

    return (max_esq, max_dir, soma_esq + soma_dir)

def subarranjo_maximo(A, baixo, alto):
    if alto == baixo:
        return (baixo, alto, A[baixo])
    else:
        meio = (baixo + alto) // 2
        baixo_esq, alto_esq, soma_esq = subarranjo_maximo(A, baixo, meio)
        baixo_dir, alto_dir, soma_dir = subarranjo_maximo(A, meio + 1, alto)
        baixo_cz, alto_cz, soma_cz = cruzamento_maximo(A, baixo, meio, alto)

        if soma_esq >= soma_dir and soma_esq >= soma_cz:
            return (baixo_esq, alto_esq, soma_esq)
        elif soma_dir >= soma_esq and soma_dir >= soma_cz:
            return (baixo_dir, alto_dir, soma_dir)
        else:
            return (baixo_cz, alto_cz, soma_cz)

Subconjunto = [1, -4, 3, -4]
esq, dir, soma = subarranjo_maximo(Subconjunto, 0, len(Subconjunto) - 1)
print(soma)

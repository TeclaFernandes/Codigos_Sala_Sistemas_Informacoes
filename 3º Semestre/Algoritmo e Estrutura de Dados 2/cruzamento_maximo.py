def soma_esquerda(A):
    soma_esquerda = float('-inf')
    soma1 = 0
    max_esquerda = 0

    for i in range(0, int((len(A)+1)/2)):
        soma1 += A[i]
        if soma1 > soma_esquerda:
            soma_esquerda = soma1
            max_esquerda = i
    
    soma_direita = float('-inf')
    soma2 = 0
    max_direita = 0

    for j in range(int((len(A)+1)/2+1), A[-1]):
        soma2 += A[j]
        if soma2 > soma_direita:
            soma_direita = soma2
            max_direita = i
    
    num = max(max_esquerda, max_direita, soma_esquerda + soma_direita)
    
    return(num)

Subconjunto = [1, -4, 3, -4]
print(soma_esquerda(Subconjunto))
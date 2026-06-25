def calcCircunferencia(lista):
    soma = []
    count = 0

    for tamanho in lista:
        count += tamanho
        soma.append(count)
    return soma

def busca_binaria(lista, num):
    inicio = 1
    fim = len(lista)

    while inicio <= fim:

        meio = int((inicio+fim)/2)

        if lista[meio] == num:
            return meio
        elif num < lista[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    return "NOT-FOUND"

def calculaPontos(soma):
    n = len(soma)
    circumferencia = soma[n-1]
    n_triangulos = 0

    if (circumferencia % 3) != 0:
        return 0
    
    arco = circumferencia//3

    for i in range(n):

        if i == 0:
            primeiro_ponto = 0
        else:
            primeiro_ponto = soma[i-1]
        if primeiro_ponto >= arco:
            return n_triangulos
        
        segundo_ponto = primeiro_ponto + arco
        if busca_binaria(soma, segundo_ponto) == "NOT-FOUND":
            continue

        terceiro_ponto = primeiro_ponto + 2*arco
        if busca_binaria(soma, terceiro_ponto) == "NOT-FOUND":
            continue
        
        n_triangulos += 1

    return n_triangulos

while True:
    try:
        n = int(input())
        tamanhos = list(map(int, input().split()))
        print(calculaPontos(calcCircunferencia(tamanhos)))
    except EOFError:
        break
def lerArcos(quantidade):
    # Tamanho dos arcos
    entrada = list(map(int, input().split()))
    
    # Se as entradas foram tamanho diferente retorna nada
    if len(entrada) != quantidade:
        return []

    # Adição dos arcos a arr
    arr = []
    for tamanho in entrada:
        if tamanho < 0:
            break
        else:
            arr.append(tamanho)
    return arr

# Arr soma dos valores sequencial
def somaArray(arr):
    soma = 0
    arrSoma = []
    for valor in arr:
        soma += valor
        arrSoma.append(soma)
    return arrSoma

# Contabilizando a quantidade de triangulos
def contaTriangulos(arrSoma):
    if not arrSoma:
        return 0

    # Verifica se a soma total é divisivel por 3
    if arrSoma[-1] % 3 != 0:
        return 0

    numTriangulos = 0

    for i in range(len(arrSoma)):
        cont = arrSoma[i - 1] if i != 0 else 0
        j = cont + (arrSoma[-1]/3)
        k = cont + 2 * (arrSoma[-1]/3)

        # Busca linear implicita
        if j in arrSoma and k in arrSoma:
            numTriangulos += 1

    return numTriangulos

def main():
    qtddArcos = int(input())
    arr = lerArcos(qtddArcos)
    arrSoma = somaArray(arr)
    numTriangulos = contaTriangulos(arrSoma)
    print(numTriangulos)

while True:
    try: 
        main()
    except EOFError: break
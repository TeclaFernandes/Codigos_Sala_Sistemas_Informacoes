def soma_lista():
    n = int(input("Informe um numero: (Digite . para encerrar)"))
    lista = []
    soma = 0

    while n != 0:
        lista.append(n)
        soma += n
        n = int(input("Informe um numero: (Digite . para encerrar)"))
    return soma 
print(f'A soma dos numeros na lista é {soma_lista()}')
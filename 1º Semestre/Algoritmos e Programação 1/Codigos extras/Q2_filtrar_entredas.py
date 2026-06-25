def lista_letra3(n):
    lista = []
    for c in range(n):
        entrada = input("Informe a entrada: ")
        if entrada[c] > 3:
            lista.append(entrada)
    print(lista)
lista_letra3(5)
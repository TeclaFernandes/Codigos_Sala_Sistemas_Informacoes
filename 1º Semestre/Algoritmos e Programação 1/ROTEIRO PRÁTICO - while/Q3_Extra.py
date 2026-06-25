entrada = input("Digite uma lista de números separados por espaços: ")
lista = [int(num) for num in entrada.split()]
n = len(lista)
troca_ocorrida = True
while troca_ocorrida:
    troca_ocorrida = False 
    i = 0
    while i < n - 1:
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            troca_ocorrida = True  
        i += 1
    n -= 1 
print("A lista ordenada é:", lista)

lista = [54, 1, 9, 39, 62, 28, 7, 70, 48, 80]

lista_par = []
lista_impar = []

for numero in lista:
    if numero %2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)

print(f'lista de numeros par --- {lista_par}')
print(f'lista de numero imapes --- {lista_impar}')
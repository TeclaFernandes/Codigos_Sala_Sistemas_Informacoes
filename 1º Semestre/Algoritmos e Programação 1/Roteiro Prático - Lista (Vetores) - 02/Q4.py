lista = [36, 94, 28, 78, 61, 42, 33, 37, 21, 64] 

menor_numero = lista[0]
maior_numero = 0
for numero in lista:
    if numero > maior_numero:   
        maior_numero = numero
    elif numero < menor_numero:
        menor_numero = numero
print(f'O MAIOR numero da lista é: {maior_numero}')
print(f'O MENOR numero da lista é: {menor_numero}')
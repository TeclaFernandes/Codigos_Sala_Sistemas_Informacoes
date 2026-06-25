lista = ["tecla", "fernandes", "oliveira", "sistemas", "informação"]

maior_string = lista[0]
for palavra in lista:
    if len(palavra) > len(maior_string):
        maior_string = palavra
print(maior_string)
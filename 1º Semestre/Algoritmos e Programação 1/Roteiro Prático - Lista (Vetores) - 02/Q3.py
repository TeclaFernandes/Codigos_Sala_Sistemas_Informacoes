lista1 = ["Tecla", "Fernandes", "Oliveira", 19, "ifce", "Crato"]
lista2 = ["Tecla", "Fernandes", "Oliveira", 19, "Jodibe", "Crato"]
nova_lista = []

for palavra1 in lista1:
    for palavra2 in lista2:
        if palavra1 == palavra2:
            nova_lista.append(palavra1)
print(nova_lista)

lista1 = ["tecla", "ifce", "SI", "noite", 19]
lista2 = ["tecla", "TI", "jodibe", "manhã", 19]

len_lista1 = len(lista1)
len_lista2 = len(lista2)

if len_lista1 == len_lista2:
    lista_nova = []
    for c in range(len_lista1):
        if lista1[c:c+len_lista2] == lista2:
            lista_nova.append(c)
print(lista_nova)
# indice confere 
# falta pegar o valor de cada indice
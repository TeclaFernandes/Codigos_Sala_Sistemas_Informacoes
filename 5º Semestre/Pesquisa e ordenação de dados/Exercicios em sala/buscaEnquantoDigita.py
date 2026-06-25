def busca_enquanto_digita(lista_palavras, letra):
    resultados = []

    for palavra in lista_palavras:
        if palavra.lower().startswith(letra.lower()):
            resultados.append(palavra)

    return resultados

palavras = ["banana", "abacate", "maçã", "ameixa", "laranja", "abacaxi"]
resultado = busca_enquanto_digita(palavras, "a")
print("Palavras encontradas:", resultado)
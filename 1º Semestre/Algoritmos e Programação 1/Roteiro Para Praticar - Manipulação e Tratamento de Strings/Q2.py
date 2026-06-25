def conta_palavra(minha_string, palavra):
    contador =  0
    tamanho = len(minha_string)
    tam_palavra = len(palavra)
    for i in range(tamanho):
        if minha_string[i:i+tam_palavra] == palavra:
            contador += 1
    return contador

print(conta_palavra("IFCE campus crato", "IFCE"))
print(conta_palavra("IFCE campus crato - IFCE campus juazeiro do norte", "IFCE"))
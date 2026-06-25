entrada = input("Digite uma palavra para verificar se é um palíndromo: ")
entrada = entrada.replace(" ", "").lower()
inicio = 0
fim = len(entrada) - 1
palindromo = True
while inicio < fim:
    if entrada[inicio] != entrada[fim]:
        palindromo = False
        inicio = fim + 1
    else:
        inicio += 1
        fim -= 1
if palindromo:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")

string = input("Digite a string a ser invertida: ")
invertida = ""
indice = len(string) - 1
while indice >= 0:
    invertida += string[indice]
    indice -= 1
print(f'A string invertida é: {invertida}')

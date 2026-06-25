def montar_palavra(n):
    palavra = ''
    for _ in range(n):
        numero = int(input("Digite um número inteiro: "))
        # Converte o número inteiro para o caractere correspondente no Unicode
        palavra += chr(numero)
    return palavra

# Solicita o número de inteiros ao usuário
n = int(input("Digite o número de inteiros: "))

# Monta a palavra usando os números fornecidos
palavra = montar_palavra(n)

# Exibe a palavra resultante
print(f"{palavra}")

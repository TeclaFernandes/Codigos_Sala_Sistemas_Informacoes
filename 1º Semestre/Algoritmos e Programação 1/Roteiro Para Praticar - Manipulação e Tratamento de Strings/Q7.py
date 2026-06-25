def exibir_unicode(palavra):
    for caractere in palavra:
        valor_unicode = ord(caractere)
        print(f"{caractere} = {valor_unicode}")

# Lê a palavra da entrada padrão
palavra = input("Digite uma palavra: ")

# Exibe cada caractere com seu valor Unicode
exibir_unicode(palavra)

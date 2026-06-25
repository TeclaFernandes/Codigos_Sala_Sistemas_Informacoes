def converte_para_minusculo(palavra):
    nova_palavra = ''
    
    for caractere in palavra:
        # Verifica se o caractere está entre 'A' e 'Z'
        if 'A' <= caractere <= 'Z':
            # Converte para minúscula usando a diferença de 32 no código ASCII
            nova_palavra += chr(ord(caractere) + 32)
        else:
            nova_palavra += caractere
    
    return nova_palavra

print(converte_para_minusculo("TeCLa"))
print(converte_para_minusculo("TeCLa Fernandes"))


def converte_para_maiusculo(palavra):
    nova_palavra = ''
    
    for caractere in palavra:
        # Verifica se o caractere está entre 'a' e 'z'
        if 'a' <= caractere <= 'z':
            # Converte para maiúscula usando a diferença de 32 no código ASCII
            nova_palavra += chr(ord(caractere) - 32)
        else:
            nova_palavra += caractere
    
    return nova_palavra

print(converte_para_maiusculo("TeCLa"))
print(converte_para_maiusculo("TeCLa Fernandes"))
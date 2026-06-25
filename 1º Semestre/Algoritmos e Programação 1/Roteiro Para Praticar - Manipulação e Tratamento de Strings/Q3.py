def substituir_ocorrencias(frase, antiga, nova):
    resultado = ""
    i = 0
    
    while i < len(frase):
        # Verifica se a substring atual é igual à palavra a ser substituída
        if frase[i:i+len(antiga)] == antiga:
            resultado += nova
            i += len(antiga)  # Avança o índice além da palavra substituída
        else:
            resultado += frase[i]
            i += 1  # Avança para o próximo caractere
    
    return resultado

# Lê a frase da entrada padrão
frase = input("Digite uma frase: ")

# Substitui todas as ocorrências de "IFCE" por "Instituto Federal do Ceará"
frase_modificada = substituir_ocorrencias(frase, "IFCE", "Instituto Federal do Ceará")

# Exibe a frase modificada
print(frase_modificada)

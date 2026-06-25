def remover_espacos_extras(s):
    resultado = ''  # Inicializa uma string vazia para armazenar o resultado final sem espaços extras
    espaco_em_branco = False  # Flag para identificar se o último caractere adicionado foi um espaço

    # Percorre cada caractere na string original 's'
    for caractere in s:
        if caractere == ' ':
            # Se o caractere atual for um espaço e o último caractere adicionado foi um espaço,
            # ignora este espaço para evitar múltiplos espaços consecutivos.
            if espaco_em_branco:
                continue
            espaco_em_branco = True  # Marca que um espaço foi encontrado
            resultado += ' '  # Adiciona um único espaço ao resultado
        else:
            espaco_em_branco = False  # Marca que o último caractere não foi um espaço
            resultado += caractere  # Adiciona o caractere atual à nova string

    # Remove o espaço extra no início da string resultante, se houver
    if resultado and resultado[0] == ' ':
        resultado = resultado[1:]
    
    # Remove o espaço extra no final da string resultante, se houver
    if resultado and resultado[-1] == ' ':
        resultado = resultado[:-1]

    return resultado  # Retorna a string final com os espaços extras removidos

# Exemplo de uso
entrada1 = "   Olá,   mundo!  Como   vai?  "  # Define uma string de exemplo com espaços extras
resultado = remover_espacos_extras(entrada1)  # Chama a função para remover os espaços extras da string
print(f"Resultado: '{resultado}'")  # Exibe o resultado final, mostrando a string sem espaços extras
entrada2 = "  Tecla           Fernandes"  # Define uma string de exemplo com espaços extras
resultado = remover_espacos_extras(entrada2)  # Chama a função para remover os espaços extras da string
print(f"Resultado: '{resultado}'")  # Exibe o resultado final, mostrando a string sem espaços extras

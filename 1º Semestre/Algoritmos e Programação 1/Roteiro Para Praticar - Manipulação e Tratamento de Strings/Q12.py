def lingua_do_i(frase):
    # Define um conjunto de vogais a serem substituídas
    vogais = "aeiouAEIOU"
    resultado = ''  # Nova string que irá armazenar o resultado final

    # Percorre cada caractere da string 'frase'
    for caractere in frase:
        # Verifica se o caractere é uma vogal
        if caractere in vogais:
            resultado += 'i'  # Substitui a vogal por 'i'
        else:
            resultado += caractere  # Mantém o caractere inalterado

    return resultado  # Retorna a string com as vogais substituídas por 'i'

# Exemplo de uso
print(lingua_do_i("Olá, como você está?"))
print(lingua_do_i("O IFCE EH UMA OTIMA INSTITUICAO"))


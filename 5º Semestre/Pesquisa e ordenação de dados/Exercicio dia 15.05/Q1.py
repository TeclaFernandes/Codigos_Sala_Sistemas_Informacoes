# Análise de Sentimentos em Redes Sociais

import string

def contar_palavras(texto):
    texto = texto.lower()

    for pontuacao in string.punctuation:
        texto = texto.replace(pontuacao, "")

    palavras = texto.split()

    frequencia = {}

    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1

    return frequencia

texto = "O rato roeu a roupa do rei de Roma. O rato roeu o rei!"
resultado = contar_palavras(texto)

print(resultado["rato"])  
print(resultado["rei"])  
print(resultado["roma"]) 
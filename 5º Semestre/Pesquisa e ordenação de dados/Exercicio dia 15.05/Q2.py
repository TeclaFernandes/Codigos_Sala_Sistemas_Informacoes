# Detecção de Plágio em Trabalhos Acadêmicos

def primeiro_caractere_unico(s):
    frequencia = {}

    for caractere in s:
        if caractere in frequencia:
            frequencia[caractere] += 1
        else:
            frequencia[caractere] = 1

    for indice, caractere in enumerate(s):
        if frequencia[caractere] == 1:
            return indice

    return -1

print(primeiro_caractere_unico("amorama")) 
print(primeiro_caractere_unico("aabbcc"))   
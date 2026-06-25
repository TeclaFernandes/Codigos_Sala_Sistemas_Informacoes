import re

def normalizar(texto):
    texto = texto.lower()
    texto = re.sub(r'[^a-zA-ZÀ-ÿ\s]', '', texto)
    palavras = texto.split()
    return palavras

def contar_frequencia(palavras):
    freq = {}
    for palavra in palavras:
        freq[palavra] = freq.get(palavra, 0) + 1
    return list(freq.items())

def heapify(lista, n, i):
    maior = i
    esq = 2 * i + 1
    dir = 2 * i + 2

    if esq < n and lista[esq][1] > lista[maior][1]:
        maior = esq
    if dir < n and lista[dir][1] > lista[maior][1]:
        maior = dir
    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        heapify(lista, n, maior)

def heap_sort(lista):
    n = len(lista)

    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)
    for i in range(n - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        heapify(lista, i, 0)
    lista.reverse()

texto = """
IA ia IA! inteligencia Inteligencia IA
"""

palavras = normalizar(texto)
frequencias = contar_frequencia(palavras)
heap_sort(frequencias)
print(frequencias)
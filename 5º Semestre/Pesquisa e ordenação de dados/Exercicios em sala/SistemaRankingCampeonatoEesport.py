class Jogador:
    def __init__(self, nickname, vitorias, saldo):
        self.nickname = nickname
        self.vitorias = vitorias
        self.saldo = saldo

    def __repr__(self):
        return f"({self.nickname}, {self.vitorias}, {self.saldo})"

def melhor(a, b):

    if a.vitorias != b.vitorias:
        return a.vitorias > b.vitorias
    if a.saldo != b.saldo:
        return a.saldo > b.saldo
    return a.nickname < b.nickname

def heapify(lista, n, i):
    maior = i
    esq = 2 * i + 1
    dir = 2 * i + 2

    if esq < n and melhor(lista[esq], lista[maior]):
        maior = esq
    if dir < n and melhor(lista[dir], lista[maior]):
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
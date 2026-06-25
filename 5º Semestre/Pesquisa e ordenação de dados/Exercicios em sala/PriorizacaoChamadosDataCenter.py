class Chamado:
    def __init__(self, identificador, severidade, horario):
        self.id = identificador
        self.severidade = severidade
        self.horario = horario

    def __repr__(self):
        return f"({self.id}, {self.severidade}, {self.horario})"

def maior_prioridade(a, b):
    """
    Retorna True se 'a' possui prioridade maior que 'b'
    """
    if a.severidade != b.severidade:
        return a.severidade > b.severidade
    return a.horario < b.horario

def heapify(lista, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and maior_prioridade(lista[esquerda], lista[maior]):
        maior = esquerda
    if direita < n and maior_prioridade(lista[direita], lista[maior]):
        maior = direita
    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        heapify(lista, n, maior)

def heap_sort(lista):
    n = len(lista)

    # Construção do Max-Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)
    # Ordenação
    for i in range(n - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        heapify(lista, i, 0)
    lista.reverse()

# Exemplo
chamados = [
    Chamado("C1", 90, 10),
    Chamado("C2", 95, 12),
    Chamado("C3", 90, 5),
    Chamado("C4", 70, 2)
]
heap_sort(chamados)
print(chamados)
class Sensor:
    def __init__(self, idSensor, temperatura, consumo):
        self.idSensor = idSensor
        self.temperatura = temperatura
        self.consumo = consumo

    def __repr__(self):
        return f"({self.idSensor}, {self.temperatura}, {self.consumo})"

def heapify(lista, n, i):
    maior = i
    esq = 2 * i + 1
    dir = 2 * i + 2

    if esq < n and lista[esq].temperatura > lista[maior].temperatura:
        maior = esq

    if dir < n and lista[dir].temperatura > lista[maior].temperatura:
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

# Exemplo
sensores = [
    Sensor("S1", 90, 100),
    Sensor("S2", 70, 40),
    Sensor("S3", 110, 80),
    Sensor("S4", 95, 120)
]

limite = 50
# Filtragem
validos = [s for s in sensores if s.consumo >= limite]
heap_sort(validos)
print(validos[:5])
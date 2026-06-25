import random

lista = [random.randint(0, 100) for _ in range(11)]

quadrados = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0 and x > 20, lista)))

print("Lista original:", lista)
print("Quadrados pares > 20:", quadrados)

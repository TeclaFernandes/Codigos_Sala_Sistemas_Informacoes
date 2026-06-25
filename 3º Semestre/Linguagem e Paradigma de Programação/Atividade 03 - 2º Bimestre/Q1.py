import random

lista = [random.randint(0, 100) for i in range(11)]

quadrados = [x**2 for x in lista if x % 2 == 0 and x > 20]

print(quadrados)

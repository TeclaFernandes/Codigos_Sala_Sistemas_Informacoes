import random

lista = [random.randint(0, 100) for i in range(5)]    

lista2 = list(map(lambda x: f"R${x},00", lista))

print(lista2)

import random

n = int(input("Advinhe o numero: "))
numero_gerado = random.randrange(1, 100)
while (n != numero_gerado):
    n = int(input("Advinhe o numero: "))
print(f"O numero acertado foi {n}")
print("Fim do loop!")
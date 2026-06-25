def potencia(base, expoente):
    pot = base
    for i in range(1, expoente):
        pot *= base
    return pot

print(potencia(2, 3))
print(potencia(4, 2))
print(potencia(5, 3))
print(potencia(9, 2))
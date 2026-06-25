import math

A = float(input("Informe o valor de A: "))
B = float(input("Informe o valor de B: "))
C = float(input("Informe o valor de C: "))

delta = B**2 - 4*A*C

if delta < 0:
    print("A equação não possui raízes reais.")
else:
    raiz_delta = math.sqrt(delta)
    X1 = (-B + raiz_delta) / (2 * A)
    X2 = (-B - raiz_delta) / (2 * A)
    print(f"O valor de X1 é {X1} e o valor de X2 é {X2}")

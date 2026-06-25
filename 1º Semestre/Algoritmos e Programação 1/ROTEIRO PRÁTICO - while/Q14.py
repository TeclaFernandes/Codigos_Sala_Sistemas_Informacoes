num = float(input("Informe o número para encontrar a raiz quadrada: "))
aproximado = num / 2
tolerancia = 0.00001
while (aproximado * aproximado - num) > tolerancia:
    aproximado = (aproximado + num / aproximado) / 2
print(f"A raiz quadrada aproximada de {num} é: {aproximado:.2f}")
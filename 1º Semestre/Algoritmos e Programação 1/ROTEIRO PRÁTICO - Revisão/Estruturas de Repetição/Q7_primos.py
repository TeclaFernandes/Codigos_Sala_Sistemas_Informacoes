valor_limite = int(input("Informe o valor limite: "))
for numero in range(2, valor_limite + 1):
    divisores = 0 
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores += 1
    if divisores == 2:
        print(numero)

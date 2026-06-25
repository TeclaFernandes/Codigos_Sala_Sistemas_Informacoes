numero = int(input("Digite um número: "))
soma_dos_divisores = 0
divisor = 1
while divisor <= numero // 2:
    if numero % divisor == 0:
        soma_dos_divisores += divisor
    divisor += 1
if soma_dos_divisores == numero:
    print(f"{numero} é um número perfeito!")
else:
    print(f"{numero} não é um número perfeito.")
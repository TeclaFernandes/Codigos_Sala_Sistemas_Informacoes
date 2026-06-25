print("Digite um numero negativo para encerrar o loop... ")
numero = int(input("Informe um numero: "))
soma = 0
while numero >= 0:
    soma += numero
    numero = int(input("Informe um numero: "))
print(f'A soma dos numero informado é {soma}')
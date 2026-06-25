num1 = float(input("Informe o primeiro numero para comparação: "))
num2 = float(input("Informe o segundo numero para comparação: "))

if num1 > num2:
    print(f'{num1} é o maior entre os dois!')
elif num2 > num1:
    print(f'{num2} é o maior entre os dois!')
else:
    print('Os numeros informados são iguais!')
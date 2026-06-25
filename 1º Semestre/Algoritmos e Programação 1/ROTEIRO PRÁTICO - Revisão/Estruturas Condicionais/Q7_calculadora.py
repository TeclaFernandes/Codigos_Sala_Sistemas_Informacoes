print("CALCULADORA: ")
num1 = float(input("Informe o primeiro numero: "))
num2 = float(input("Informe o segundo numero: "))

print("Opçoes \n [1]. ADIÇÃO \n [2]. SUBTRAÇÃO \n [3]. MULTIPLICAÇÃO \n [4]. DIVISÃO")
opcao = int(input("Sua opção: "))

if opcao == 1: 
    print(f'{num1} + {num2} = {num1 + num2}')
elif opcao == 2: 
    print(f'{num1} - {num2} = {num1 - num2}')
elif opcao == 3: 
    print(f'{num1} X {num2} = {num1 * num2}')
elif opcao == 4: 
    if num2 != 0:
        print(f'{num1} / {num2} = {num1 / num2}')
    else: 
        print('Divisão não exestente, pois o denominador é igua a ZERO')
else:
    print('Opção invalida...')
num1 = int(input("Informe o primeiro numero: "))
num2 = int(input("Informe o segundo numero: "))
print("===" * 10)
print("O QUE OPERAÇÃO DESEJA USAR: \n [1] - SOMA \n [2] - SUBTRAÇÃO \n [3] - MULTIPLICAÇÃO \n [4] - DIVISÃO")
print("===" * 10)
continua = "y"
while continua == "y":
    escolha = int(input("Sua opção: "))
    if escolha == 1:
        soma = num1 + num2
        print(f'Seu resultado: {soma}')
    elif escolha == 2:
        sub = num1 - num2
        print(f'Seu resultado: {sub}')
    elif escolha == 3:
        mul = num1 * num2
        print(f'Seu resultado: {mul}')
    elif escolha == 4:
        if num2 == 0:
            print("Não existe divisão por zero! ")
        else:
            div = num1 / num2
            print(f'Seu resultado: {div}')
    else: 
        print("Opção inválida, informe uma opção válida... ")
    continua = input("deseja continuar? (y/n) ")
    print("===" * 10)
print("Operação encerrada.")
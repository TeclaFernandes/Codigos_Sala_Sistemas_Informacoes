print("==="* 15)
print("         CALCULADORA          ")
print("==="* 15)

num1 = float(input("Informe o primeiro numero: "))
num2 = float(input("Informe o segundo numero: "))

print("==="* 15)

print("OPÇÕES: \n [1]. SOMA \n [2]. SUBTRAÇÃO \n [3]. MULTIPLICAÇÃO \n [4]. DIVISÃO")
opcao = int(input("Qual sua opção? "))

print("==="* 15)

if opcao == 1:
    print(f"{num1} + {num2} = {num1+num2}")
elif opcao == 2:
    print(f"{num1} - {num2} = {num1-num2}")
elif opcao == 3:
    print(f"{num1} x {num2} = {num1*num2}")
elif opcao == 4 and num2 != 0:
    print(f"{num1} / {num2} = {num1/num2}")
else:
    print("Opção inválida...")

print("==="* 15)
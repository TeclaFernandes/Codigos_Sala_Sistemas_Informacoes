saldo = float(input("Informe o saldo inicial da conta: R$ "))
print("\nBem-vindo ao Caixa Eletrônico!")
print("Digite 0 para encerrar a operação.")
while saldo > 0:
    saque = float(input("Informe o valor do saque: R$ "))
    if saque <= 0:
        print("O valor do saque deve ser positivo. Tente novamente.")
    elif saque > saldo:
        print(f"Saldo insuficiente. Seu saldo atual é: R$ {saldo:.2f}")
    else:
        saldo -= saque
        print(f"Saque realizado com sucesso! Seu saldo atual é: R$ {saldo:.2f}")
    if saldo <= 0:
        print("Saldo insuficiente. Encerrando a operação.")
        break
print("Obrigado por utilizar o Caixa Eletrônico!")

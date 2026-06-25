n = float(input("Digite o numero da lista: "))
para = input("Deseja continuar? (Nao = done) ")
soma = n
c = 1
while (para != 'done'):
    c += 1
    n = float(input("Digite o numero da lista: "))
    para = input("Deseja continuar? (Nao = done) ")
    soma += n
media = soma/c
print(f'A soma dos numeros informados é {soma}')
print(f'A media dos numeros apresentados é {media}')
print("Fim do loop")
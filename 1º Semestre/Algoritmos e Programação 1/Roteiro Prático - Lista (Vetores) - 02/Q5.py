altura = float(input("Informe a altura: (digite 0 para encerrar)"))
lista = []

while altura != 0:
    lista.append(altura)
    altura = float(input("Informe a altura: (digite 0 para encerrar)"))

soma = 0
for tamanho in lista: 
    soma += tamanho

media = soma/len(lista)

print(f'A relação das alturas informadas é: {lista}')
print(f'A soma das alturas informadas é: {soma}')
print(f'A media das alturas informadas é: {media}')
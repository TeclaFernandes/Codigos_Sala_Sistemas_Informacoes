numero = int(input("Informe a quantidade de notas: "))
soma = 0
for i in range(numero):
    nota = float(input("Informe a nota: "))
    soma += nota
media = soma/numero
print(media)
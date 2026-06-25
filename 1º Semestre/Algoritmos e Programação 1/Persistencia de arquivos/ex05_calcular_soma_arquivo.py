file = open('numeros.txt', 'r')

dados = file.readlines()
file.close()

soma = 0
for num in dados:
    soma += int(num)
print(soma)
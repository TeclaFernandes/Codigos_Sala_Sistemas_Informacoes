file = open('dados.txt', 'r', encoding='utf8')

dados = file.readlines()
file.close()

for i in range(len(dados), 0, -1):
    print(dados[i-1])

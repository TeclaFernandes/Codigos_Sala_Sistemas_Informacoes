file = open('dados.txt', 'r', encoding='utf8')

dados = file.read()

file.close()
print(dados)
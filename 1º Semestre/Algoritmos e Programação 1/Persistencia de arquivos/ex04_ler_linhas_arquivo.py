file = open('dados.txt', 'r', encoding='utf8')

dados = file.readlines()
file.close()
print(f'{len(dados)} linhas.' )
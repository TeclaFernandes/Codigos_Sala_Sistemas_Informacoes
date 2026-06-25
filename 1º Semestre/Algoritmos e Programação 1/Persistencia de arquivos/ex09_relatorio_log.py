file = open('log.txt', 'r', encoding='utf8')

dados = file.readlines()

file.close()
dadosTratados = []
valores = []

for valor in dados:
    dadosTratados.append(valor.replace('\n', ' '))


for dado in dadosTratados:
    if dado not in valores:
        valores.append(dado)

for valor in valores:
    repetido = dadosTratados.count(valor)
    print(f'{valor}: {repetido}')
    





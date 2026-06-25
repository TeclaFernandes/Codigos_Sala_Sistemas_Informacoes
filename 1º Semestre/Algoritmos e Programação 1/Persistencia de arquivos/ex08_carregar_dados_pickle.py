import pickle

file = open('estudante.pkl', 'rb')
dados = pickle.load(file)

file.close()

for valor in dados:
    print(valor)

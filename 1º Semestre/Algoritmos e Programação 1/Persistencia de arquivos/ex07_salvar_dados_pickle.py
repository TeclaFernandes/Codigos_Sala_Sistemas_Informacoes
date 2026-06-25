import pickle

dados = ['Maria', '20', 'Sistemas de Informação para web']
file = open('estudante.pkl', 'wb')

pickle.dump(dados, file)

file.close()
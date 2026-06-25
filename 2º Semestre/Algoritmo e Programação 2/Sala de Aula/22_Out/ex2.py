import pickle

arquivo = open("dados.dat", "rb")
lista = pickle.load(arquivo)
arquivo.close()

for e in lista:
    print(e)
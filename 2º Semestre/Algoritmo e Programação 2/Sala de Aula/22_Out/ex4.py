import pickle

arquivo = open("clientes.dat", "rb")
clientes = pickle.load(arquivo)
arquivo.close()

for c in clientes:
    print("Nome:",c[0])
    print("Idade:",c[1])
    print("Cidade:",c[2])
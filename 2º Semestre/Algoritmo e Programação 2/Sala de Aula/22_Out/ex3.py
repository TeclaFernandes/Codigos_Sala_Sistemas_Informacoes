import pickle
import os

def salvar_arquivo(nome_arquivo, lista):
    arquivo = open(nome_arquivo, "wb")
    pickle.dump(lista, arquivo)
    arquivo.close()

def carrega_dados(nome_arquivo):
    if (not os.path.exists(nome_arquivo)):
        return []
    arquivo = open(nome_arquivo, "rb")
    lista = pickle.load(arquivo)
    arquivo.close()
    return lista    

def cadastrar_clientes(clientes):
    n = int(input("N:"))
    for e in range(n):
        nome = input("Nome:")
        idade = int(input("Idade:"))
        cidade = input("Cidade:")
        cliente = [nome, idade, cidade]
        clientes.append(cliente)
    salvar_arquivo("clientes.dat", clientes)



def imprime_lista(lista):
    for c in lista:
        print("Nome:",c[0])
        print("Idade:",c[1])
        print("Cidade:",c[2])

def imprime_menu():
    print(" 1. Cadastrar Novos Clientes")
    print(" 2. Listar Clientes")
    print(" 9. Sair ")

# Programa Principal
clientes = carrega_dados("clientes.dat")
opcao = 1
while (opcao!=9):
    imprime_menu()
    opcao = int(input("Opção:"))
    if opcao==1:
        cadastrar_clientes(clientes)
    elif (opcao==2):
        imprime_lista(clientes)
    elif (opcao==9):
        print("Tchau!")
    else:
        print("Opcao invalida")   
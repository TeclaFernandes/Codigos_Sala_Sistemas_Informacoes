import sqlite3
from produto import *

def imprime_menu():
    print(" MENU ")
    print(" 1. Inserir Produto ")
    print(" 2. Remover Produto ")
    print(" 3. Atualiza Produto ")
    print(" 4. Listar Produtos ")
    print(" 5. Pesquisar Produto")
    print(" 6. Inserir Cliente ")
    print(" 7. Atualizar Cliente ")
    print(" 8. Remover Cliente ")
    print("---------------------")
    print(" 9. Sair ")

def inserir_produto():
    codigo = int(input("Codigo:"))
    descricao = input("Descricao:")
    valor = float(input("Valor:"))
    insere_produto(codigo, descricao, valor)

def listar_produtos():
    print("PRODUTOS CADASTRADOS:")
    print("--------------------")
    resultado = lista_produtos()
    imprime_resultado(resultado)

def remover_produto():
    listar_produtos()
    codigo = int(input("Digite o codigo do produto a ser removido:"))
    remover(codigo)
    print("Produto removido com sucesso!")

def atualizar_produto():
    listar_produtos()
    codigo = int(input("Digite o codigo do produto a ser atualizado:"))
    descricao = input("Nova Descricao:")
    valor = float(input("Novo Valor:"))
    atualiza_produto(codigo, descricao, valor)
    print("Produto atualizado com sucesso!")    

def pesquisa():
    termo = input("Digite o nome do produto que deseja buscar:")
    resultado = pesquisa_produtos(termo)
    print("Resultado da Busca:")
    imprime_resultado(resultado)
    print("##############################")


# Programa Principal
opcao = 1
while (opcao!=9):
    imprime_menu()
    opcao = int(input("Opcao:"))
    if (opcao==1):
        inserir_produto()
    elif (opcao==2):
        remover_produto()
    elif (opcao==3):
        atualizar_produto()
    elif (opcao==4):
        listar_produtos()
    elif (opcao==5):
        pesquisa()

# Cabeçalho
def imprime_cabecalho():
    print(" ###############################")
    print("   REGISTRA PESOS v0.0.1")
    print(" ###############################")

# Menu
def imprime_menu():
    print("# MENU:") 
    print("#  1. Registra Nome e Peso")
    print("#  2. Lista Nome e Peso")
    print("#  3. Remove Pessoa")
    print("#  4. Atualizar Dado")
    print("#  9. Sair")

# Registro de pesos
def registra_peso(lista1, lista2):
    nome = input("Nome:")
    peso = float(input("Peso (kg):"))
    lista1.append(nome)
    lista2.append(peso)

# Impressão da lista
def imprime_listas(lista1, lista2):
    n = len(lista1)
    if (n == len(lista2)):
        for i in range(n):
            print(i+1,")",lista1[i], lista2[i])

# Remove itens
def remove_item(indice, lista1, lista2):
    lista1.pop(indice)
    lista2.pop(indice)

# Atualiza itens
def atualizar_item(indice, lista1, lista2, novo_dado1, novo_dado2):
    lista1[indice] = novo_dado1
    lista2[indice] = novo_dado2

# Programa Principal
nomes = []
pesos = []

opcao = 0
while (opcao != 9):
    imprime_cabecalho()
    imprime_menu()
    opcao = int(input("Informe a opcao desejada:"))
    if (opcao == 1):
        registra_peso(nomes, pesos)
    elif (opcao ==2):
        imprime_listas(nomes, pesos)
    elif (opcao ==3):
        n = len(nomes)
        if (n>0):
            imprime_listas(nomes, pesos)
            codigo = int(input("Qual o numero da pessoa que deseja remover?"))
            if (codigo>0 and codigo <n+1):
                remove_item(codigo-1, nomes, pesos)
            else:
                print("Numero invalido.")
        else:
            print("Nao ha nenhum peso cadastrado.")
    elif (opcao==4):
        n = len(nomes)
        if (n>0):
            imprime_listas(nomes, pesos)
            codigo = int(input("Qual o numero da pessoa que deseja atualizar?"))
            if (codigo>0 and codigo <n+1):
                novo_nome = input("Informe um novo nome:")
                novo_peso = float(input("Informe um novo peso:"))
                atualizar_item(codigo-1, nomes, pesos, novo_nome, novo_peso)
            else:
                print("Numero invalido.")
        else:
            print("Nao ha nenhum peso cadastrado.")
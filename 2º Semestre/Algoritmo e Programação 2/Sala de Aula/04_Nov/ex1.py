import sqlite3

def lista_produtos():
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produto;")
    resultado = cursor.fetchall()
    #conexao.commit()
    conexao.close()

    for linha in resultado:
        print("Codigo:",linha[0])
        print("Descrição:",linha[1])
        print("Valor:",linha[2])
    
def insere_produto(codigo, descricao, valor):
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO produto (codigo, descricao, valor) VALUES (?,?,?)", (codigo, descricao, valor))
    conexao.commit()
    conexao.close() 

# Programa Principal
insere_produto(10, 'Mouse XYZ', 200);
lista_produtos()
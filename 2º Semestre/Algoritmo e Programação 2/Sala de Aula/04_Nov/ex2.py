import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()
cursor.execute("SELECT * FROM cliente;")
resultado = cursor.fetchall()
#conexao.commit()
conexao.close()

for linha in resultado:
    print("ID:",linha[0])
    print("Nome:",linha[1])
    

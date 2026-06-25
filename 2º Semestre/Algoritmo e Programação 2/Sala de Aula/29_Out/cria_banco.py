
import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()
cursor.execute("""CREATE TABLE cliente (
        id INT, 
        nome VARCHAR(100) NOT NULL, 
        cidade VARCHAR(30),
        uf VARCHAR(2),
        PRIMARY KEY(id)
    )""")
conexao.commit()
conexao.close()

import sqlite3

id = int(input("id:"))
nome = input("nome:")
cidade = input("cidade:")
uf = input("uf:")


conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()
cursor.execute("INSERT INTO cliente (id, nome, cidade, uf) VALUES (?, ?, ?, ?);", (id, nome, cidade, uf))
conexao.commit()
conexao.close()
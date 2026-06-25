palavra = input("Digite uma palavra: (click ENTER para encerrar)")
nova_palavra = palavra.strip().capitalize()
lista = []

while nova_palavra != '':
    lista.append(nova_palavra)
    palavra = input("Digite uma palavra: (click ENTER para encerrar)")
    nova_palavra = palavra.strip().capitalize()

print("lista original: ", lista)

nova_lista = []
for palavra in lista:
    if len(palavra) >= 3:
        nova_lista.append(palavra) 
print("nova lista: ", nova_lista)
soma_nota = 0
for i in range(1, 6):
    nota = float(input("Informe a nota: "))
    soma_nota += nota
    media = soma_nota/5
print(f"A media das notas é {media}")
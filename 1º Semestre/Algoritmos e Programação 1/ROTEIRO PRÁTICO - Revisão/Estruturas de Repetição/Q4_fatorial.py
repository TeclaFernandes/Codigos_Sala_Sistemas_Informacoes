num = int(input("Informe um numero: "))
fat = 1 
for i in range(1, num + 1):
    fat *= i
print(f'Fatorial de {num} é {fat}')
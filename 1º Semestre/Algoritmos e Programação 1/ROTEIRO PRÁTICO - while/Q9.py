numero = int(input('digite um número: '))
fator = 1 
print(f'calculando {numero}! = ', end=' ')
while numero > 0: 
  print(f'{numero}', end=' ')
  print(' x ' if numero > 1 else ' = ', end=' ')
  fator = fator * numero
  numero -= 1
print(f'{fator}')
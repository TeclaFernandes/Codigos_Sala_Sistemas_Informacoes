numero_decimal = int(input('Digite um número decimal: '))
if numero_decimal == 0:
    print('O número 0 em binário é 0')
else:
    binario = ''
    while numero_decimal > 0:
        resto = numero_decimal % 2 
        binario = str(resto) + binario 
        numero_decimal = numero_decimal // 2 
    print(f'O número em binário é {binario}')
ano = int(input("Informe o ano: "))

if ano % 400 == 0:
    print(f'{ano} é um ano bissexto.')
elif ano % 100 == 0:
    print(f'{ano} NÃO é um ano bissexto.')
elif ano % 4 == 0:
    print(f'{ano} é um ano bissexto.')
else:
    print(f'{ano} NÃO é um ano bissexto.')
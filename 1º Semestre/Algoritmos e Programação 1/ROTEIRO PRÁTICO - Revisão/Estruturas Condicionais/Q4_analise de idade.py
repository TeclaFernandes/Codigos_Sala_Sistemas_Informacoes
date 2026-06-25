idade = int(input("Informe a idade para analise: "))

if idade > 0 and idade <= 12:
    print('Criança')
elif idade > 12 and idade <= 18:
    print('Adolescente')
elif idade > 18 and idade <= 65: 
    print('Adulto')
elif idade > 65:
    print('Idoso')
else:
    print('Idade inválida...')
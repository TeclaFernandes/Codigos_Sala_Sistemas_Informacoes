lado1 = float(input("Informe o lado do triangulo: "))
lado2 = float(input("Informe o lado do triangulo: "))
lado3 = float(input("Informe o lado do triangulo: "))

if lado1 == lado2 and lado2 == lado3 and lado3 == lado1:
    print('O trinangulo é EQUILATERO.')
elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
    print('O triangulo é ISÓCELES.')
elif lado1 + lado2 > lado3 or lado2 + lado3 > lado1 or lado1 + lado3 > lado2:
    print('O triangulo é ESCALENO ')
else: 
    print('As medidas informadas não formam um triângulo')
real = float(input("Informe a quantia em real: "))
taxa_cambio_dolar = float(input("Informe a taxa de câmbio do dolar: "))
taxa_cambio_euro = float(input("Informe a taxa de câmbio do euro: "))

dolar = real*taxa_cambio_dolar
euro = real*taxa_cambio_euro

print(f"R$ {real} em dolar é USD $ {dolar:.2f} e em euro é EUR {euro:.2f}")
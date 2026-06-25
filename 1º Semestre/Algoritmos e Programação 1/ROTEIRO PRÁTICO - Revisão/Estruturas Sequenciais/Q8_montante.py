capital_inicial = float(input("Informe o capital inicial: "))
taxa_juros = float(input("Informe a taxa de juro: "))
tempo = int(input("Informe o tempo em anos: "))

montante = capital_inicial*(1+taxa_juros/100)**tempo

print(f"Montante = {montante:.2f}")
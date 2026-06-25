principal = float(input("Informe o valor principal (inicial): "))
taxa_juros = float(input("Informe a taxa de juros anual (em %): ")) / 100
compostos_por_ano = int(input("Informe o número de vezes que os juros são compostos por ano: "))
anos = int(input("Informe o número de anos: "))
montante = principal
periodos_totais = compostos_por_ano * anos
contador = 0
while contador < periodos_totais:
    montante *= (1 + taxa_juros / compostos_por_ano)
    contador += 1
print(f"O montante acumulado após {anos} anos é: R$ {montante:.2f}")

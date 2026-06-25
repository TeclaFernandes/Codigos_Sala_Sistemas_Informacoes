preco_inicial = float(input("Digite o preço inicial do produto (em R$): "))
num_meses = int(input("Digite o número de meses com desconto: "))

preco_final = preco_inicial

for mes in range(1, num_meses + 1):
    desconto = float(input(f"Digite o desconto para o mês {mes} (em %): "))
    preco_final -= preco_final * (desconto / 100)

print(f"O preço final do produto é: R${preco_final:.2f}")

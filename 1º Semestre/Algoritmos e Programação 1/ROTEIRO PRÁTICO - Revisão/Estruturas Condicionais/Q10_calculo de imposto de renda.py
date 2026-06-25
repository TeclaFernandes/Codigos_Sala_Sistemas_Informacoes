def calcular_imposto_de_renda(renda_bruta, deducoes):
    renda_tributavel = renda_bruta - deducoes
    
    if renda_tributavel <= 2640:
        imposto = 0
    elif renda_tributavel <= 3520:
        imposto = (renda_tributavel - 2640) * 0.075 - 66.75
    elif renda_tributavel <= 4540:
        imposto = (renda_tributavel - 3520) * 0.15 + 138.45
    elif renda_tributavel <= 5660:
        imposto = (renda_tributavel - 4540) * 0.225 + 244.80
    else:
        imposto = (renda_tributavel - 5660) * 0.275 + 446.75
    
    imposto = max(imposto, 0)
    
    return imposto

renda_bruta = float(input("Digite a sua renda mensal bruta: R$ "))
deducoes = float(input("Digite o total de deduções permitidas: R$ "))

imposto = calcular_imposto_de_renda(renda_bruta, deducoes)

print(f"O valor do imposto de renda a ser pago é: R$ {imposto:.2f}")

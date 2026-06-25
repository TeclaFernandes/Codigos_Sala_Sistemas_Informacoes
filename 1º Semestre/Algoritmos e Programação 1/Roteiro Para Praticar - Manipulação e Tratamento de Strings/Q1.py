def vogal(palavra):
    vogais = "aeiouAEIOU"
    qntd_vogal = 0
    for letra in palavra:
        if letra in vogais:
            qntd_vogal += 1
    return qntd_vogal

print(vogal("Tecla"))
print(vogal("Tecla Fernandes Oliveira"))
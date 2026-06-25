def palindromo(palavra):
    palavra_invertida = palavra[::-1]
    if palavra == palavra_invertida:
        return "É um palindromo!"
    else:
        return "Não é um palindromo!"

print(palindromo("tecla"))
print(palindromo("arara"))
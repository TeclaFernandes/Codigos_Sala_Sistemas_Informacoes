def inserir_pontuacao(top10, nova_pontuacao):

    top10.append(nova_pontuacao)

    i = len(top10) - 1

    while i > 0 and top10[i] > top10[i-1]:
        top10[i], top10[i-1] = top10[i-1], top10[i]
        i -= 1

    if len(top10) > 10:
        top10.pop()

    return top10

top10 = [1000, 900, 850, 800, 700, 600, 500, 400, 300, 200]
top10 = inserir_pontuacao(top10, 750)
print(top10)
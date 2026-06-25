class Produto:
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco

    def __repr__(self):
        return f"{self.id} - {self.nome} - {self.preco}"


def ordenar_produtos(produtos):
    n = len(produtos)

    for i in range(n):
        trocou = False

        for j in range(0, n - i - 1):

            if (produtos[j].preco > produtos[j+1].preco) or \
               (produtos[j].preco == produtos[j+1].preco and 
                produtos[j].nome > produtos[j+1].nome):

                produtos[j], produtos[j+1] = produtos[j+1], produtos[j]
                trocou = True

        if not trocou:
            break

produtos = [
    Produto(1, "Arroz", 20),
    Produto(2, "Feijão", 10),
    Produto(3, "Feijoada", 10),
    Produto(4, "Picanha", 10),
    Produto(5, "Macarrão", 10),
    Produto(6, "Açúcar", 15)
]

ordenar_produtos(produtos)

for p in produtos:
    print(p)
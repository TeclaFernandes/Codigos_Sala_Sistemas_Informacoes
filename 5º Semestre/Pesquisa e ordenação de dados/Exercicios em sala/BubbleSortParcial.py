listDic = [
    {'Nome': 'Ana', 'Nota': 8.5},
    {'Nome': 'Andre', 'Nota': 6.0},
    {'Nome': 'Carlos', 'Nota': 7.0},
    {'Nome': 'Bruno', 'Nota': 8.5}
]

def bubble_sort(lista, key=None, reverse=False):
    n = len(lista)

    for i in range(n - 1):
        trocou = False
        for j in range(n - i - 1):
            a = lista[j]
            b = lista[j + 1]

            if key:
                a = key(a)
                b = key(b)

            if (not reverse and a > b) or (reverse and a < b):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True

        if not trocou:
            break

    return lista

bubble_sort(listDic, key=lambda item: item['Nome'])
bubble_sort(listDic, key=lambda item: item['Nota'], reverse=True)
print(listDic[0], listDic[1], listDic[2])
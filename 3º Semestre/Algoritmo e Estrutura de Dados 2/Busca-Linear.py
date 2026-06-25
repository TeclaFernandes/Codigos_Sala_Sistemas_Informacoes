cod = [12, 345, 182, 342, 2025, 2645, 266, 1651, 166, 548]

desejo = 2025

for i in range(len(cod)):
    if cod[i] == desejo:
        busca = i+1
        print('posição: ', busca)
        break

if desejo not in cod:
    print('NOT-FOUND') 
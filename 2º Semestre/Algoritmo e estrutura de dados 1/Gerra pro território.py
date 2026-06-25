import numpy as np

n = int(input())
entrada = list(map(int, input().split()))

soma = 0

for i in range(len(entrada)):
    soma += entrada[i]
metade = soma/2

soma_metade = 0

for c in range(len(entrada)):
    soma_metade += entrada[c]

    if soma_metade == metade:
        print(c+1)
        exit()
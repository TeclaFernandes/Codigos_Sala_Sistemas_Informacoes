l = list(map(int, input().split()))

maior = 0
n = 0

while l[n] > 0:
    if maior < l[n]:
        maior = l[n]
    n += 1

print(maior)

# Otimização de Caixas em Supermercado

def encontrar_par(nums, alvo):
    vistos = {}

    for i, num in enumerate(nums):
        complemento = alvo - num

        if complemento in vistos:
            return (vistos[complemento], i)

        vistos[num] = i

    return (-1, -1)

nums = [2, 7, 11, 15]
alvo1 = 9
alvo2 = 10

print(encontrar_par(nums, alvo1)) 
print(encontrar_par(nums, alvo2)) 
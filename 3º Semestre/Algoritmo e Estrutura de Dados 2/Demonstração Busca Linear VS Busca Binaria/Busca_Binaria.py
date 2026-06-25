# import numpy as np
# np.random.seed(123456)
# arr = np.sort(np.random.randint(low=0, high=10000000000, size=100000000))

# def Ordena(x, vetor):
#     n = len(vetor)
#     p = 1
#     r = n

#     while p <= r: 
#         print("|", end="")

#         q = (p+r)//2
#         if vetor [q] == x:
#             return q
        
#         elif x < vetor[q]:
#             r = q - 1
        
#         elif x > vetor[q]:
#             p = q + 1

#     return 'NOT-FOUND'

# print(Ordena(arr[-1], arr))
        
arr = [4, 7, 20, 23, 53, 67, 165, 181, 469, 546]

def Ordena(x, vetor):
    n = len(vetor)
    p = 1
    r = n

    while p <= r: 
        print("|", end="")

        q = (p+r)//2
        if vetor [q] == x:
            return q
        
        elif x < vetor[q]:
            r = q - 1
        
        elif x > vetor[q]:
            p = q + 1

    return 'NOT-FOUND'

print(Ordena(arr[-1], arr))
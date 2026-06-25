def busca_otimizada(A, x):
    n = len(A)  
    ultimo = A[-1]  
    A[-1] = x  

    i = 0  
    while A[i] != x:
        i += 1  

    A[-1] = ultimo  

    if i < n - 1 or A[-1] == x:
        return i 
    else:
        return "NOT-FOUND"

A = [165, 181, 23, 546, 469, 20, 4, 7, 53, 67]
x = 20
resultado = busca_otimizada(A, x)
print(resultado)

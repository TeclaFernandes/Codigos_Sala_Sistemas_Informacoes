import numpy as np
np.random.seed(123456)
arr = np.sort(np.random.randint(low=0, high=10000000000, size=100000000))

def Linear(arr, x):

    for i in range(len(arr)):
        print("|", end="")
        if arr[i] == x:
            return i
        return 'NOT-FOUND'

x = arr[-1]
resultado = Linear(arr, x)
print(resultado)
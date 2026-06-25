num = 1  
while num <= 50:  
    t = 0  
    c = 1  
    while c <= num:  
        if num % c == 0:  
            t += 1  
        c += 1  
    if t == 2:  
        print(f'{num} é primo!')  
    num += 1  
n = int(input())
for _ in range(n):
    numero = int(input())
    
    if numero <= 1:
        print("Not Prime")
    elif numero <= 3:
        print("Prime")
    elif numero % 2 == 0 or numero % 3 == 0:
        print("Not Prime")
    else:
        i = 5
        is_prime = True
        while i * i <= numero:
            if numero % i == 0 or numero % (i + 2) == 0:
                is_prime = False
                break
            i += 6
        
        if is_prime:
            print("Prime")
        else:
            print("Not Prime")
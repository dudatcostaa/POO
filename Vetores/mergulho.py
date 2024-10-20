while True:
    try:
        n, r = input().split()
        n = int(n)
        r = int(r)
        
        retornaram = input().split()

        if r == n:
            print("*")
        else:
            retornaram = [int(x) for x in retornaram]
            
            for i in range(1, n + 1):
                if i not in retornaram:
                    print("%d " %i, end="")
            print()        
        
    except EOFError:
        break
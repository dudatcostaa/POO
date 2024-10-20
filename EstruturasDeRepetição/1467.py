while True :
    try:
        a, b, c = input().split()
        a = int (a)
        b = int (b)
        c = int (c)
        
        if a == b == c:
            print('*')
        elif a != b and a != c:
            print('A')
        elif b != c and b != a:
            print('B')
        else:
            print('C')
            
    except EOFError:
        break
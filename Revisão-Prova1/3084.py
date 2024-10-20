while True:
    try:
        h, m = input().split()
        h = int(h)
        m = int(m)
        
        horas = h // 30
        minutos = m // 6
        
        print("%02d:%02d" % (horas, minutos))
    except EOFError:
        break
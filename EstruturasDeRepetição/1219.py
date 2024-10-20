import math
while True:
    try:
        l1, l2, l3 = input().split()
        l1 = float(l1)
        l2 = float(l2)
        l3 = float(l3)
        if not (l1, l2, l3):
            break
        
        perimetro = l1 + l2 + l3
        p = (l1 + l2 + l3) / 2
        areatriangular = math.sqrt(p * (p - l1)*(p - l2)*(p - l3))
        r = areatriangular / p
        R = (l1 * l2 * l3) / (4.0 * areatriangular)
        areacmaior = math.pi * (R ** 2)
        areacmenor = math.pi * (r ** 2)
        
        sunflowers = areacmaior - areatriangular
        violetas = areatriangular - areacmenor
        #rosas = areacmenor
        
        print("%.4f %.4f %.4f" % (sunflowers, violetas, areacmenor))
    
    except EOFError:
        break
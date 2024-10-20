n = int(input())

for _ in range(0, n):
    j1, d1 = input().split()
    j1 = int(j1)
    d1 = int(d1)
    j2, d2 = input().split()
    j2 = int(j2)
    d2 = int(d2)
    j3, d3 = input().split()
    j3 = int(j3)
    d3 = int(d3)
    m1, b1 = input().split()
    m1 = int(m1)
    b1 = int(b1)
    m2, b2 = input().split()
    m2 = int(m2)
    b2 = int(b2)
    m3, b3 = input().split()
    m3 = int(m3)
    b3 = int(b3)
    
    if(j1 * d1) + (j2 * d2) + (j3 * d3) < (m1 * b1) + (m2 * b2) + (m3 * b3):
        print("MARIA")
    else:
        print("JOAO")
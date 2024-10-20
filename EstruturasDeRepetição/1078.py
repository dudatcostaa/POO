n = int(input())

if 2 < n < 1000:
    for i in range (1,11):
        print("%d x %d = %d" % (i, n, n * i))
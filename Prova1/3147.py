h, e, a, o, w, x = input().split()
h = int(h)
e = int(e)
a = int(a)
o = int (o)
w = int(w)
x = int(x)

if h + e + a + x >= o + w:
    print("Middle-earth is safe.")
else:
    print("Sauron has returned.")
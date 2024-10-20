n = int(input())

anos = n // 365
restodiasano = (n % 365) 
meses = (restodiasano // 30)
dias = (restodiasano % 30)

print("%d ano(s)" % anos)
print("%d mes(es)" % meses)
print("%d dia(s)" % dias)
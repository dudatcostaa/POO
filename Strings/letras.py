l = input().strip()
t = input().strip()

palavras = t.split()

repeticoes = 0

for i in palavras:
    if l in i:
        repeticoes += 1

total_palavras = len(palavras)

if total_palavras > 0:
    porcentagem = (repeticoes / total_palavras) * 100
else:
    porcentagem = 0 

print("%.1f" % porcentagem)
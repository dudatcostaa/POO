valor = float(input())

notas = int(valor)
moedas = int((valor - notas) * 100)

print("NOTAS:")
cem = notas // 100
notas %= 100
print("%d nota(s) de R$ 100.00" % cem)

cinquenta = notas // 50
notas %= 50
print("%d nota(s) de R$ 50.00" % cinquenta)

vinte = notas // 20
notas %= 20
print("%d nota(s) de R$ 20.00" % vinte)

dez = notas // 10
notas %= 10
print("%d nota(s) de R$ 10.00" % dez)

cinco = notas // 5
notas %= 5
print("%d nota(s) de R$ 5.00" % cinco)

dois = notas // 2
notas %= 2
print("%d nota(s) de R$ 2.00" % dois)

print("MOEDAS:")
um = notas // 1
print("%d moeda(s) de R$ 1.00" % um)

cinquenta_centavos = moedas // 50
moedas %= 50
print("%d moeda(s) de R$ 0.50" % cinquenta_centavos)

vinte_e_cinco_centavos = moedas // 25
moedas %= 25
print("%d moeda(s) de R$ 0.25" % vinte_e_cinco_centavos)

dez_centavos = moedas // 10
moedas %= 10
print("%d moeda(s) de R$ 0.10" % dez_centavos)

cinco_centavos = moedas // 5
moedas %= 5
print("%d moeda(s) de R$ 0.05" % cinco_centavos)

um_centavo = moedas // 1
moedas %= 1
print("%d moeda(s) de R$ 0.01" % um_centavo)
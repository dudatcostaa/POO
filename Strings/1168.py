n = int(input())

for i in range(n):
    numero = input().strip()
    
    leds = 0

    for i in numero:
        if i == '1':
            leds += 2
        elif i == '2':
            leds += 5
        elif i == '3':
            leds += 5
        elif i == '4':
            leds += 4
        elif i == '5':
            leds += 5
        elif i == '6':
            leds += 6
        elif i == '7':
            leds += 3
        elif i == '8':
            leds += 7
        elif i == '9':
            leds += 6
        else:
            leds += 6
    
    print("%d leds" % leds)
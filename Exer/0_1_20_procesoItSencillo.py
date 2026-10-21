numero = int(input())

while numero < 100:
    if numero % 2 == 0:
        numero += 3
    else:
        numero *= 2

print(numero)

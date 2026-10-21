numero = int(input())
digits = 0

if numero < 0:
    numero *= -1

if numero == 0 or numero < 10:
    print(1)
else:
    while numero > 0:
        numero //= 10
        digits += 1
    print(digits)

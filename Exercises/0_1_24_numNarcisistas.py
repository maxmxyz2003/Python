numero = int(input())
res = 0
digits = 0

copianum = numero
img = numero

if numero < 0:
    numero *= -1

if numero == 0 or numero < 10:
    digits = 1
else:
    while numero > 0:
        numero //= 10
        digits += 1
    copia = digits
    numero = copianum  # Restauramos el valor original de 'numero' para el siguiente bucle
    while copianum > 0:
        base = copianum % 10
        potencia = 1
        for i in range(copia):
            potencia *= base
        res += potencia
        copianum //= 10

if img == res:
    print("Es Narcisista")
else:
    print("No es Narcisista")

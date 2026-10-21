casos = int(input())

for i in range(casos):
    tomacorr = int(input())
    espacios = 0
    for i in range(tomacorr):
        temp = int(input())
        espacios += temp
    espacios = espacios - tomacorr + 1
    print(espacios)

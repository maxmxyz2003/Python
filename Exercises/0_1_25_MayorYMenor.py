import sys
numeros = int(input())
elmayor = -sys.maxsize
elmenor = sys.maxsize

if numeros <= 1:
    temp = int(input())
    print(temp, temp)
else:
    for i in range(numeros):
        temp = int(input())
        if temp > elmayor:
            elmayor = temp
        if temp < elmenor:
            elmenor = temp
    print(elmayor, elmenor)

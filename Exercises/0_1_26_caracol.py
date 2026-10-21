profund = int(input())
avance = int(input())
retroceso = int(input())
inicio = 0
dias = 0

prog = avance - retroceso

while inicio < profund:
    inicio += prog
    dias += 1

print(dias - 1)

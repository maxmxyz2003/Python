vaca=False
Descandsito=False
vasyir=vaca or Descandsito
if vasyir:
    print("Si si voy yir")
else:
    print("No no voy yir")


Descandsito=True
vasyir=vaca or Descandsito
if vasyir:
    print("Si si voy yir")
else:
    print("No no voy yir")

#Si funciona en repl

#otra forma sería
vaca=False
Descandsito=False
vasyir=not(vaca or Descandsito)
if vasyir:
    print("Non")
else:
    print("Sis")

Descandsito=True
vasyir=not(vaca or Descandsito)
if vasyir:
    print("Non")
else:
    print("Sis")
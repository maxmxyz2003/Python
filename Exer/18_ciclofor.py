

from tracemalloc import stop


a=""
filas=int(input("num filas "))
columnas=int(input("Num columns "))
symbolo=input("Introduce el simbolo ")
for i in range(filas):
    for n in range(columnas):
        print(symbolo, end="")
    print()



cadena_de_teshto="Bien seco el cerdo"
for caracter in cadena_de_teshto:
    print(caracter)
else:
    print("Fin xd")


#Ejemplo 2
pais="Mexico"
for letra in pais:
    if letra =="i":
        break #romper la ejecucion del codigo
    else:
        print(letra)



for letra in "pais":
    if letra =="i":
        break
    else:
        print(letra)

frutas=["uva", "sandía"]
for fruta in frutas:
    print(fruta)



print("AVG")
hs=input("Escribe La estatura ',' sin escpacio: ").split(",")
for n in range(0, len(hs)):
    hs[n]=int(hs[n])
print (hs)

tot=0
for h in hs:
    tot+=h
print(tot)

students=0
for i in hs:
    students+=1
print(students)

print(f"El promedio es {tot/students}")

#maximos y minimos
print(max(hs))
print(min(hs))


print("AVG")
hs=input("Escribe La estatura ',' sin escpacio: ").split(",")
for n in range(0, len(hs)):
    hs[n]=int(hs[n])
print (hs)

tot=0
for h in hs:
    tot+=h
print(tot)

students=0
for i in hs:
    students+=1
print(students)

print(f"El promedio es {tot/students}")



print("Puntajes Max y min")
sc=input("Escribe los puntajes ',' sin escpacio: ").split(",")
for n in range(0, len(sc)):
    sc[n]=int(sc[n])
print (sc)

Max=0
for dat in sc:
    if dat>Max:
        Max=dat
print(Max)



#----------------------------GAUSS
number=0
for n in range(1,101):
    number+=n
print(number)


#ASI NO
r=1
for n in range(1,100):
    r+=n
print(r)

#----------Sumar todos los pares del 2 al 100
n=0
for r in range(2,101):
    if r%2==0:
        n+=r
print(n)
#---------------Papa keshu
n=0
for r in range(1,101):
    if r%3==0:
        print("PAPA")
    elif r%5==0:
        print("Keshu")
    else:
        print(f"numero {r}")
            
print(n)

xd=9
#inicia en 0
for position in range(xd):
    print(position)
    
print(xd)



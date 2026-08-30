#listas sintax
nombres=["Juan Leonidas","Chuek", "Shaggy", "canija", "Chelin", "Gokuk"]
print(nombres)
#acceder al elemento con +
print(nombres[0])
#acceder al elemento con -
print(nombres[-4])

#acceder a un rango de elementos
print(nombres[0:4])
#Desde el incio sin incluir el final
print(nombres[:2])
print(nombres[:5])

#Desde el indice haste el final sin el inicio
print(nombres[2:])
print(nombres[4:])


#cambiar un valor
nombres[4]="ZEZ"
print(nombres)


for name in nombres:
    print(f"{name}\n") # \n = salto de linea
else:
    print("Ya no hay gfe solo tengo 5 pesitos xd")

print(len(nombres)) #cantidad de elementos de la lista

#agregar a la lista al final
nombres.append("Negro")
print(nombres)

#agregar a la lista donde sea
nombres.insert(0,"Seco")
print(nombres)

#quitar a la lista donde sea
nombres.remove("Seco")
print(nombres)

#quitar a la lista al final
nombres.pop()
print(nombres)


#quitar a la lista donde sea
del nombres [5]
print(nombres)
#limpiar lista de todo
nombres.clear()



bebidas=["cafe", "soda", "te"]
cenas=["pizza", "burg", "Chickn"]
postres=["kek", "ice", "carlota"]
comida=[bebidas,cenas,postres]
comida[0][2]="MUCHA KK"

print(comida[0][2])
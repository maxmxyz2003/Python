#tupla sintax
frutas=("coko", "Fresa", "Gayuaba", "platano", "Youoo")
#saber la cant de elementos
print(len(frutas))
#acceder a un elemento +
print(frutas[0])
#acceder a un elemento -
print(frutas[-1])

#acceder a un rango de elementos
print(frutas[0:4])
#Desde el incio sin incluir el final
print(frutas[:2])
#Desde el indice haste el final sin el inicio
print(frutas[2:])

for fruta in frutas:
    print(f"{fruta}")

#cambiar de elemento
frutalista=list(frutas)
frutalista[0]="UVA"
frutas=tuple(frutalista)
print(frutas)

del frutas #eliminamos la tupla
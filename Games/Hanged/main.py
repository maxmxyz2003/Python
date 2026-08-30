lista_personajes=["shaggy", "shrek", "oscar", "cubo", "dante", "facundo", "juan"]
import random
#elegimos un personaje al azar
nombre_personaje=random.choice(lista_personajes)
#Creamos una lista de caracteres que forman el nombre
Espacios=[]
#creamos variable para contar las letras que ocupa
num_letras=len(nombre_personaje)
#print(num_letras)
#numero de vidas total
vidas=6
#variavle "esp" para contar los 
# espacios que ocupa la palabra y anotarlos en la lista de espacios
for esp in range(num_letras):
    Espacios+="-"
#lista con los espacios necesarios creada
print(Espacios)
#respuesta
#print(f"La respuesta es {nombre_personaje}")

#Definimos el fin 
fin=False
#Hasta que ganemos o perdamso se ejecuta el while

while fin!=True:
    #intentos
    intento=input("Escoge una letra: ")
    #la varaible position empieza en 0,
    #  la letra la definimos en base a la posicion 

    for position in range(num_letras):
        letra=nombre_personaje[position] #tomamos la palabra  
        #como lista letra por letra
        #donde coincida la letra en el indice position se cambia el valor
        if letra==intento:
            Espacios[position]=letra
    #nuestra nueva palabra con espacios actualizado
    print(Espacios)
    #Declaramos que se vayan perdiendo vidas si fallan el intento
    if intento not in nombre_personaje:
        vidas-=1
        if vidas==0:
            print("perdiste")
            break
    #Ya cuando no halla - se acaba porque ganamos
    if "-" not in Espacios:
        fin=True
        print("Ganaste")

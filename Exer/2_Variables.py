import xdrlib


Variable_xd = 3
print(Variable_xd)
Variable_xd = "Cico pseo"
print(Variable_xd)

x=5
y=1
print(x)
print(y)

print(x+y)
#Lugar de la variable en la mem ram 
print(id(x))
print(id(y))
print(id(x+y))

#Comentario
# Indicador para el programador 
sr: int =1

type(Variable_xd)
type(x)
#cadenas---------------
Texto="Mucha compu"
equisde="XD"
#concatenar
#opcion 1
print("Yo antes era:" +Texto+equisde)
#opcion 2
print("Yo antes era:", Texto, equisde)

equix="5"
yo= "1000"
y_1="1"
print(equix+y_1)
print(x+y)
print(int(yo))

#Boleano
Nosabo=True
print(Nosabo)
if Nosabo:
    print("No sabo")


#valor por consola----------
yo=input("Escribe tu nombre: ")
print(yo)
#cambiar tipo de variable

resultado = int(input('Cómo estuvo tu día (1 al 10)?: '))
print('Mi día estuvo de:', resultado)

mipito = input("Escribe un mensaje: ")
print("Valor proporcionado:"+ mipito)
print("Fin del programa")

#Hayvariables locales y globales
#ejemplo
def funcion():
    a=5
    print(a+6)
#print(a+6) No se puede porque no esta definida afuera e la funcion
#PAra definir una variable global dentro de una funcion hacemos lo siguiente
xd=0
def funcion_2():
    global xd
    xd=5
    print(xd+6)
print(xd)

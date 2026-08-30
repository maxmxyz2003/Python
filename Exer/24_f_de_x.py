def SaludarYa(nombre, apodo):
    print(f"SALUDOS \/ {nombre} el {apodo}" )
    print("      ( ! )")

SaludarYa("Juan", "Leonidas Toreto")

def que_Onda(podo):
    print(f"Que onda mi {podo}" )

que_Onda("Chuek")

#REturn
def sumar(a, b):
    return a+b
result=sumar(5, 9)
print(result)

#valores default

def sumar(a=0, b=0):
    return a+b

result=sumar()
print(f"Resultado sin nada {result}")
print(f"Resultado de sumar 2 y 5: {sumar(2,5)}")

#----------------

def lista_names(*nombres): #(*argumentos) como tupla   
    for nombre in nombres:
        print(nombre)
lista_names("Chuek", "lanzaguisantes", "Sos")

#ahora como dicc
def lista_dicc(**terminos):
    for llave, valor in terminos.items():
        print(f"{llave} : {valor}")

lista_dicc(Cherk="Shrek", Aaron="Feo")

#-------
def decirnombre(nombres):
    for nombre in nombres:
        print(f"Hola {nombre} \n")

nombres=["Cherk", "Chaggy", "Giovanni leoni di"]
decirnombre(nombres)
decirnombre("Chek")

decirnombre((10,12, 10800)) #tupla

decirnombre([10,12, 10800]) #Lista



#---------------
print("imprimir en Tilulo")
def titulo(frase):
    if frase=="" or frase==" ":
        print("No ingresaste argumentos validos")
    print(frase.title())

titulo("Que onda mi chuek")

titulo(" ")
titulo(input("ingresa la frase: "))





#----------Funcion en funcion

def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)#15
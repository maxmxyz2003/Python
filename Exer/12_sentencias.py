print ("Ejemplo 1")
codicion=True
#La condicion con texto se va a tomar comono valida
if codicion==True:
    print("Condicion verdadera")
elif codicion==False:
    print("Condicion falsa")
else:
    print("Condicion no reconocida")


print("Ejemplo 2")
print("wilkommen je suis the montaña rusa")
h=int(input("Introduce tu estarua (cm): "))
if h<0:
    print("eso no es posbile")
elif h<120:
    print("Eres muy bajo")
elif h<=120:
    print("Aceptado")
else:
    print("Condicion no reconocida")


print("Ejemplo 3 ifs anidados")
print("wilkommen je suis the montaña rusa")
alt=int(input("Introduce tu estarua (cm): "))
age=int(input("Introduce tu edad: "))

if alt>120:
    print("Aceptado")
    if age<12:
        print("El cosrto es de $5")
    elif 12<age<18:
        print("Pagar $7")
    else:
        print("El costo es de $500")
else:
    print("Eres muy bajo")

#--------------
print("calcular año bisiesto")
anion=int(input("Escribe el año: "))
if anion%4==0:
    if anion%100==0:
        if anion%400==0:
            print("Año bisiesto perfecto")
        else: 
            print("No año bisiesto perfecto")
    else:
        print("No año bisiesto perfecto")
else:
    print("No año bisiesto")

#-----------------------
print("Ejemplo 4 con varias condiciones")
print("wilkommen je suis the montaña rusa")
al=int(input("Introduce tu estarua (cm): "))
ag=int(input("Introduce tu edad: "))
cuenta=0
if al>120:
    print("Aceptado")
    if ag<12:
        cuenta=5
        print(f"El cosrto es de {cuenta}")
    elif 12<ag<18:
        cuenta=7
        print("Pagar $7")
    else:
        cuenta=500
        print("El costo es de $500")
    foto=input("Quieres foto (S/N)?: ")
    if foto=="S":
        print("Serían $3 extra ")
        cuenta=cuenta+3
        print(cuenta)
    else:
        print(f"LA cuenta final es de {cuenta}")
else:
    print("Eres muy bajo")
#-----------------


#--------------
print("calcular año bisiesto simplificado")
anion=int(input("Escribe el año: "))
if anion%4==0 & anion%100==0 & anion%400==0:
    print("No año bisiesto perfecto")
else:
    print("No año bisiesto perfecto")
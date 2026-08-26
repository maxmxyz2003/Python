#General
edad=int(input("Escribe un numero: "))
Valor_min=20
Valor_max=30
edadenrango = (edad>=Valor_min) and (edad<=Valor_max)
if edadenrango==True:
    print("Califica")
else:
    print("No Califica")


#preciso
edad=int(input("Escribe un numero: "))
Ventes=edad>=20 and edad<30
trentes=edad>=30 and edad<40
if Ventes or trentes:
    if Ventes:
        print("Esta en los veintes")
    elif trentes: #elif para no marcar otro 
        #if dentro de otro if sino en el mismo o "Si no esto entonces si aquello"
        print("Esta en los treintas")
    else:
        print("No esta en el rango")


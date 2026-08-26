valorenrango=int(input("Escribe un numero: "))

Valor_min=0
Valor_max=5
valorpermitido = (valorenrango>=Valor_min) and (valorenrango<=Valor_max)
if valorpermitido==True:
    print("Estamos en el mismo rango")
else:
    print("No estamos en el mismo rango")
##Si sirve en repl.it
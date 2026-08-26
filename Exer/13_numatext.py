#numero=int(input("Escribe un numero seco: "))

#numeroentexto=""
#if numero==1:
#    numeroentexto="número uno"
#elif numero==2:
#    numeroentexto="número dos"
#elif numero==3:
#    numeroentexto="número tre"
#else: 
#    numeroentexto="No valido"
#print(f"El numero proporcionado es {numero} - {numeroentexto}")





numero = int(input('Proporciona un valor entre 1 y 3: '))
numeroTexto = ''
if numero == 1:
    numeroTexto = 'Numero uno'
elif numero == 2:
    numeroTexto = 'Numero dos'
elif numero == 3:
    numeroTexto = 'Numero tres'
else:
    numeroTexto = 'Valor fuera de rango'
print(f'Numero proporcionado: {numero} - {numeroTexto}')
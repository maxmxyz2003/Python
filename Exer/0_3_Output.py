# Estructura: nombre=input("Mensaje")
print("Dame tu nombre")
nombre=input()# input es para guardar datos
print("Hola",nombre) # nombre es una variable, no le ponemos comillas
#input solo guarda texto por defecto, hay que decirle que tipo de dato es
numero=int(input("Dame un numero")) # int es para guardar numeros enteros
print("El numero es",numero)
print(type(numero)) # Corroborar que tengamos un numero entero y no un texto
print("Dame un numero decimal")
numeroDec=float(input()) # float es para guardar numeros decimales
print("El numero decimal es",numeroDec)
print(type(numeroDec)) # Corroborar que tengamos un numero entero y no

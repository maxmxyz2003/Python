continua=True
while continua:
    numero=int(input("Escribe un número: "))

    if numero%2==0:
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")
    
    seguir=input("continuar(S/N) ?: ")
    if seguir=="S":
        continue
    else:
        print("fin del programa")
        break
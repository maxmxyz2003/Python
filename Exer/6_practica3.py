
continuar=True
while continuar:
    edad=int(input("Escribe tu edad: "))
    if edad<0:
        print("Eso no es posible")
    elif edad<10:
        print("Eres un niño como Peter Pan")    
    elif edad<18:
        print("Eres un puberto/adolecente como las TMNT")
    elif edad<30:
        print("Eres un adulto joven como el kechu")
        
    elif edad<40: 
        print("Eres un adulto")
    elif edad<80: 
        print("Eres un adulto mayor")
        
    elif edad>120:
        print(f"{edad} Tampoco es posible, ni que fueras George arreola")
    continuar=input("Continue?(S/N): ")
    if continuar=="S":
        continuar=True
    else:
        print("Fin del programa")
        break
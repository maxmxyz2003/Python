edad=int(input("Escribe tu edad: "))
if edad<0:
    print("Eso no es posible")
elif edad<18:
    print("Eres menor de edad")
elif edad<120: 
    print("Eres mayor de edad")
else:
    print("Tampoco es posible")

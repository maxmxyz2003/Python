def Calificar(calif):
    if calif < 6:
        print("NA")
    elif 6 <= calif < 7.5:
        print("S")
    elif 7.5 <= calif < 9:
        print("B")
    elif 9 <= calif <= 10:
        print("MB")

calificacion = float(input())
Calificar(calificacion)

def mystery_funct(n):
    if n <= 1:
        return n
    else:
        return mystery_funct(n-1)+mystery_funct(n-2)

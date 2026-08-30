#Crear objeros
class Personaje:
    def __init__(self, name, apellido, edad):
        self.name=name
        self.apellido=apellido
        self.edad=edad
    #nuevo metodo de instancia
    def mostrar_detail(self):
        print(f"Nombre: {self.name} \n ")
        print(f"Apellido: {self.apellido} \n ")
        print(f"Edad: {self.edad} \n ")
personaje1=Personaje("The", "Wok", 100)
#print(personaje1.name)
#print(personaje1.apellido)
#print(personaje1.edad)
personaje1.mostrar_detail()
personaje2=Personaje("Jong", "Xina", 43)
personaje2.mostrar_detail()

#print(f"{personaje2.name} {personaje2.apellido} {personaje2.edad}")
#Modifi valores
personaje1.apellido="COCK"

personaje1.mostrar_detail()
#Podemps solo llamar al metodo de details y listo
personaje1.mostrar_detail()
personaje2.mostrar_detail()
# o tambien así
Personaje.mostrar_detail(personaje1)
# se pueden agregar características adicionales 
# pero solo se agregaran a uno solo

personaje1.pito=3
print(f"El pito le mide {personaje1.pito} cm")


class IG:
    def __init__(self, id, namenick):
        self.id=id
        self.namenick=namenick
        self.seguidos=0
        self.seguidores=0
        
    #nuevo metodo de instancia
    def Seguir(self, user):
        user.seguidores+=1
        self.seguidos+=1

        return f"Sigues a {self.seguidos}"
        #print(f"Te siguen  {user.seguidores}")
        
    def Mostrar_info(self):    
        print(f"Cuenta_ID: {self.name} \n ")
        print(f"Namenick: {self.namenick} \n ")
        print(f"Edad: {self.edad} \n ")
User1=IG(1, "The Wok")
User2=IG(2, "Jong Xina")

User1.Seguir(User2)
print(User1.seguidos)




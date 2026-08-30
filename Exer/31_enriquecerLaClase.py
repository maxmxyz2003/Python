#Crear objeros
class Personaje:
    def __init__(self, name, apellido, edad, *tupl, **dicc): #añadir tupla y un dicc
        self.name=name
        self.apellido=apellido
        self.edad=edad
        self.tupl=tupl
        self.dicc=dicc
    #nuevo metodo de instancia
    def mostrar_detail(self):
        print(f"Nombre: {self.name} \n ")
        print(f"Apellido: {self.apellido} \n ")
        print(f"Edad: {self.edad} \n ")
        print(f"Edad: {self.tupl} \n ")
        print(f"Edad: {self.dicc} \n ")
        
personaje1=Personaje("The", "Wok", 100, "Wock","Rock", "COCK", p="pito",)

personaje1.mostrar_detail()
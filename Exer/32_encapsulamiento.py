#Crear objeros
class Personaje:
    def __init__(self, name, apellido, edad): #añadir tupla y un dicc
        self._name=name #atributo encapsulado ya sea con "_" 
                        #o "__" este ultimo no es recomendable
        self._apellido=apellido
        self._edad=edad

    #nuevo metodo de instancia
    def mostrar_detail(self):
        print(f"Nombre: {self._name} \n ")
        print(f"Apellido: {self._apellido} \n ")
        print(f"Edad: {self._edad} \n ")
        
personaje1=Personaje("The", "Wok", 100, "Wock","Rock", "COCK", p="pito",)

personaje1.mostrar_detail()
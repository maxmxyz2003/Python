from prueba import Persona

if __name__=="__main__":
    print("Crear objetos".center(50,"_"))#Centrar con el guion bajo
    persona3=Persona("Youyo", "500", 23)


    persona3.mostrar_detalle()
    print("Eliminar objetos".center(30,"_"))
    del persona3
    print(__name__)#estamos trabajanod en este modiulo o sea solo este archivo
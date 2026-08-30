class Aritmetica:
    """
    suma resta mutiplicacion y division
    """
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def sumar(self):
        return self.a+self.b
    def restar(self):
        return self.a-self.b
    def multiplicar(self):
        return self.a*self.b
    def divi(self):
        return self.a/self.b
    

operacion1=Aritmetica(5,3)
print(f"Los valores son 5 y 3")
print(f"LA suma es {operacion1.sumar()}")
print(f"LA resta es {operacion1.restar()}")
print(f"LA mutiplicacion es {operacion1.multiplicar()}")

print(f"La division redondeada es {operacion1.divi():.2f}") #para solo mostrar 2 digitos decimales

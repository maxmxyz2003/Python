class rectangulo:
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura
    def area(self):
        return self.base*self.altura
    def perimetro(self):
        return 2*self.altura+2*self.base

rectan1=rectangulo(5,3)
print(f"Los valores son 5 y 3")
print(f"El area es {rectan1.area()}")
print(f"El perimetro es {rectan1.perimetro()}")
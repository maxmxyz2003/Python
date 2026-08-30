class cubo:
    def __init__(self, largo, alto, ancho):
        self.largo=largo
        self.alto=alto
        self.ancho=ancho
        
    def vol(self):
        return self.ancho*self.alto*self.largo

cubo1=cubo(5,5,5)
print(f"Los lados miden 5")
print(f"El volumen es {cubo1.vol()} cm^3")

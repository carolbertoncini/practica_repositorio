import math
class Figura:
    def __init(self):
        pass
    def get_area(self):
        return ("No se puede crear el área")
    def get_perimetro(self):
        return ("No se puede calcular el perímetro")

class Rectangulo(Figura):
    def __init__(self,base,altura):
        self.base = base
        self.altura= altura
        super().__init__()
    def get_area(self):
        area = self.base * self.altura
        return area
    def get_perimetro(self):
        perimetro = 2*self.base + 2*self.altura
        return perimetro

class Circulo (Figura):
    def __init__(self,radio):
        self.radio = radio
    def get_area(self):
        area = math.pi * self.radio**2
        return area
    def get_perimetro(self):
        perimetro = 2*math.pi*self.radio
        return perimetro
class Cuadrado (Figura):
    def __init__(self,lado):
        self.lado = lado
    def get_area(self):
        area = self.lado * self.lado
        return area
    def get_perimetro (self):
        perimetro = self.lado * 4
        return perimetro

rectangulo1 = Rectangulo(3,1)
print("El rectángulo tiene un área de: ",rectangulo1.get_area(), "y un perímetro de:", rectangulo1.get_perimetro())
circulo1 = Circulo(2)
print("El círculo tiene un área de", circulo1.get_area(), "y un perímetro de:", circulo1.get_perimetro())
cuadrado1 = Cuadrado(3)
print("El cuadrado tiene un área de:", cuadrado1.get_area(), "y un perímetro de:", cuadrado1.get_perimetro())

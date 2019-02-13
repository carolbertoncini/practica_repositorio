#Crear una clase Rectángulo, con atributos base y altura. Crear también el constructor de la clase
#y los métodos necesarios para calcular el área y el perímetro. Crear otra clase PruebaRectángulo
#que pruebe varios rectángulos y muestre por pantalla sus áreas y perímetros.

class Rectangulo:
    def __init__ (self, base, altura):
        self.base = base
        self.altura = altura
    def get_area(self):
        area = self.base * self.altura
        return area
    def get_perimetro(self):
        perimetro = self.base * 2 + self.altura * 2
        return perimetro

class PruebaRectangulo(Rectangulo):
    def __init__(self, base, altura):
        super().__init__(base, altura)

rectangulo = PruebaRectangulo(2,3)
rectangulo.get_area()
rectangulo.get_perimetro()

print ("El area del rectangulo es:", rectangulo.get_area(),"y el perímetro" ,rectangulo.get_perimetro())

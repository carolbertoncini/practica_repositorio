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


rectangulo1 = Rectangulo(3,1)
print("El rectángulo tiene un área de: ",rectangulo1.get_area(), "y un perímetro de:", rectangulo1.get_perimetro())

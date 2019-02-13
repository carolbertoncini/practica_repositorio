#Crear una clase Coche, a través de la cual se pueda conocer el color del coche, la marca, el
#modelo, el número de caballos, el número de puertas y la matrícula. Crear el constructor del
#coche, así como los métodos que considere necesarios. Crear una clase PruebaCoche que
#instancie varios coches, cambiándole el color a lo largo de la vida a algunos de ellos y
#mostrándolo por pantalla.

class Coche:
    def __init__(self,color,marca,modelo,caballos,puertas,matricula):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.caballos = caballos
        self.puertas = puertas
        self.matricula = matricula
    def get_info(self):
        return self.color, self.marca, self.modelo, self.caballos, self.puertas, self.matricula

class PruebaCoche(Coche):
    def __init__(self,color,marca,modelo,caballos,puertas,matricula,cambio_color = None):
        super().__init__(color,marca,modelo,caballos,puertas,matricula)
        self.cambio_color = cambio_color
    def cambio_color(self):
        if self.cambio_color is not None:
            self.cambio_color = cambio_color
        return self.cambio_color

coche1 = PruebaCoche("azul","Audi","A4","1200CV",4,"636463B", "rojo")
print("El coche de color", coche1.color, coche1.marca, "modelo", coche1.modelo, "tiene", coche1.caballos, coche1.puertas,"puertas", "y matrícula", coche1.matricula, "y ha cambiado al color", coche1.cambio_color())


            

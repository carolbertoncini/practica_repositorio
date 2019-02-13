class Producto():
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
class Medicamento(Producto):
    def __init__(self,nombre, cantidad, precio, composicion, porcentaje):
        super().__init__(nombre, cantidad, precio)
        self.composicion = composicion
        self.porcentaje = porcentaje
class Laboratorio():
    def __init__(self, laboratorio, Producto, Producto2):
        self.laboratorio = laboratorio
        self.producto = Producto
        self.producto2 = Producto2

pañales = Producto("pañales",2, 4)

dalsi = Medicamento("dalsi", 6, 3, "Acido", 0.3)

roche = Laboratorio("Roche", dalsi, pañales)

print(roche.producto.nombre)
print(roche.producto2.nombre)
print("El laboratorio", roche.laboratorio, "tiene", roche.producto.nombre ,", ", roche.producto2.nombre)
print("la composición de", roche.producto.nombre,"es", roche.producto.composicion)

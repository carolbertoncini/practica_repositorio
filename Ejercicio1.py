#Crea una clase cuenta con los métodos, ingreso, reintegro y transferencia.
#La clase contendrá un constructor por defecto,
#u con parámetros y los métodos para obtener info. (getters)
#o para almacenar info, (setters)

class Cuenta:
    def __init__(self, ingreso, reintegro, transferencia):
        self.ingreso = ingreso
        self.reintegro = reintegro
        self.transferencia = transferencia
    def dame_info(self):
        return self.ingreso, self.reintegro, self.transferencia
    def almacena_info(self):
        almacenar = []
        almacenar.append(self.ingreso)
        almacenar.append(self.reintegro)
        almacenar.append(self.transferencia)
        return almacenar

banco = Cuenta(2000,60,56)
print("Mi cuenta tiene un ingreso de:", banco.ingreso, "un reintegro de:", banco.reintegro, "y una transferencia de:", banco.transferencia)
print("Tengo", banco.almacena_info())

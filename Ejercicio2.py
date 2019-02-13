#Crea una clase Contador con los métodos par
#a incrementar y decrementar el contador. La clase
#contendrá un constructor por defecto, un constructor con parámetros
#y los métodos getters y setters

class Contador:
    def __init__ (self,x):
        self.x = x
    def mueve_arriba(self):
        return self.x + 1
    def mueve_abajo (self):
        return self.x - 1
coche = Contador(4)
print("El coche está en la posición:", coche.mueve_abajo())


class Contador:
    def __init__ (self, val = None):
        self.val = val
        if val is  None:
            self.val = 3
        else:
            self.val
    def mueve_arriba(self):
        return self.val + 1
    def mueve_abajo(self):
        return self.val -1
coche = Contador()
print("El coche está en la posición:", coche.mueve_abajo())

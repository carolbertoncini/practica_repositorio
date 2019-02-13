# Crea una clase Persona. La clase contendrá un atributo fecha Nacimiento que será un objeto de
#la clase Fecha creada en el ejercicio 6 anterior.

class Fecha:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    def get_info (self):
        return self.dia, self.mes, self.ano
    def comprobar(self):
        if self.dia > 31 or self.dia < 1:
            print("La fecha introducida no es válida")
        elif self.mes > 12 or self.mes < 1:
            print("La fecha introducida no es válida")
    def mover_arriba(self):
        self.dia = self.dia + 1
        return self.dia, self.mes, self.ano

class Persona(Fecha):
    def __init__ (self, dia, mes, ano, dia_nacimiento, mes_nacimiento):
        super().__init__(dia, mes, ano)
        self.dia_nacimiento = dia_nacimiento
        self.mes_nacimiento = mes_nacimiento
    def get_info(self):
        return self.dia_nacimiento, self.mes_nacimiento

cumpleanos = Persona(11,"febrero",2019,6,"marzo")
print("Hoy es:", cumpleanos.dia, "de", cumpleanos.mes, "de", cumpleanos.ano, "mi cumpleaños es el", cumpleanos.dia_nacimiento, "de", cumpleanos.mes_nacimiento)

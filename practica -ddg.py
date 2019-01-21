jugador = int(input("Introduzca un número: "))

def ddg(jugador):
    jugadores = ["Juan", "Jose", "Maria", "Pedro"]
    for i in range(len(jugadores)):
        if i == jugador:
            return (jugadores[i])
print(ddg(jugador))

print("hola")

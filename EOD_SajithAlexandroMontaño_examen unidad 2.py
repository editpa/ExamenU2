class Cola:
    def __init__(self):
        self.items = []

    def cola(self, x):
        self.items.append(x)

    def colaF(self):
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola está vacía")

    def print_cola(self):
        print(self.items)


class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def print_pila(self):
        print(self.items)

# Crear una lista de nombres
nombres = ["VANESSA, EMMANUEL, MELANY, ARATH, GAEL, JULIAN, SAJITH, ZULEYMA, AXEL, FERNANDA, JUAN, AYLIN, SANTIAGO, JONATHAN, XITLALI"]

#
class Cola:
    def __init__(self):
        self.items = []

    def cola(self, x):
        self.items.append(x)

    def colaF(self):
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola está vacía")

    def print_cola(self):
        print(self.items)


class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def print_pila(self):
        print(self.items)

def acomodar_nombres():
    nombres = []  # Creamos una lista vacía para almacenar los nombres

    # Pedimos al usuario que ingrese los nombres hasta que ingrese un nombre vacío
    while True:
        nombre = input("Ingresa un nombre (o presiona Enter para finalizar): ")
        if nombre == "":
            break
        nombres.append(nombre)

    # Ordenar la lista alfabéticamente
    nombres.sort()

    # Imprimir la lista ordenada
    print("Lista de nombres ordenada alfabéticamente:")
    for nombre in nombres:
        print(nombre)

# Llamamos a la función para acomodar los nombres
acomodar_nombres()



class Cola:
    def __init__(self):
        self.items = []

    def cola(self, x):
        self.items.append(x)

    def colaF(self):
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola esta vacia")

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

cola_nombres = Cola()
pila_nombres = Pila()

nombres = ["VANESSA", "EMMANUEL", "MELANY", "ARATH", "GAEL", "JULIAN", "SAJITH", "ZULEYMA", "AXEL", "FERNANDA", "JUAN", "AYLIN", "SANTIAGO", "JONATHAN", "XITLALI"]
for nombre in nombres:
    cola_nombres.cola(nombre)

while not len(cola_nombres.items) == 0:
    nombre = cola_nombres.colaF()
    while len(pila_nombres.items) > 0 and nombre > pila_nombres.items[0]:
        cola_nombres.cola(pila_nombres.pop())
    pila_nombres.push(nombre)

while len(pila_nombres.items) > 0:
    print(pila_nombres.pop())

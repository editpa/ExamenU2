class Cola:
    def __init__(self):
        self.items = []

    def cola(self, x):
        self.items.append(x)

    def colaF(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            raise ValueError("La cola está vacía")

    def esta_vacia(self):
        return len(self.items) == 0

    def print_cola(self):
        print(self.items)


class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            raise ValueError("La pila está vacía")

    def esta_vacia(self):
        return len(self.items) == 0

    def print_pila(self):
        print(self.items)

# Crear una cola y una pila
cola = Cola()
pila = Pila()

while True:
    print("\n1. Agregar nombre")
    print("2. Quitar nombre de la cola")
    print("3. Quitar nombre de la pila")
    print("4. Ordenar y mostrar nombres alfabéticamente")
    print("5. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Ingresa un nombre: ")
        cola.cola(nombre)
        pila.push(nombre)
    elif opcion == "2":
        try:
            nombre_cola = cola.colaF()
            print(f"Nombre eliminado de la cola: {nombre_cola}")
        except ValueError as e:
            print(e)
    elif opcion == "3":
        try:
            nombre_pila = pila.pop()
            print(f"Nombre eliminado de la pila: {nombre_pila}")
        except ValueError as e:
            print(e)
    elif opcion == "4":
        nombres = pila.items + cola.items
        nombres.sort()
        print("\nLista de nombres ordenada alfabéticamente:")
        for nombre in nombres:
            print(nombre)
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")

print("\nCola:")
cola.print_cola()
print("\nPila:")
pila.print_pila()

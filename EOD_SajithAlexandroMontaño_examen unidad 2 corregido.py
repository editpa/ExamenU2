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

def ordenar_nombres(nombres):
    n = len(nombres)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nombres[j] > nombres[j + 1]:
                nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]

cola = Cola()
pila = Pila()

while True:
    print("\nMenú:")
    print("1. Agregar nombre")
    print("2. Quitar nombre")
    print("3. Mostrar nombres ordenados alfabéticamente")
    print("4. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Ingresa un nombre: ")
        cola.cola(nombre)
        pila.push(nombre)
        print(f"'{nombre}' agregado a la cola y la pila.")
    elif opcion == "2":
        if not cola.esta_vacia():
            nombre_cola = cola.colaF()
            print(f"'{nombre_cola}' eliminado de la cola.")
        else:
            print("La cola está vacía.")
        if not pila.esta_vacia():
            nombre_pila = pila.pop()
            print(f"'{nombre_pila}' eliminado de la pila.")
        else:
            print("La pila está vacía.")
    elif opcion == "3":
        nombres = pila.items + cola.items
        ordenar_nombres(nombres)
        print("\nLista de nombres ordenada alfabéticamente:")
        for nombre in nombres:
            print(nombre)
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")

print("\nCola:")
cola.print_cola()
print("\nPila:")
pila.print_pila()

class RegistroNombres:
    def __init__(self):
        self.lista_nombres = []

    def agregar_nombre(self, nombre):
        if nombre not in self.lista_nombres:
            self.lista_nombres.append(nombre)
            print(f"Nombre {nombre} agregado correctamente.")
        else:
            print(f"El nombre {nombre} ya está en la lista, no se permite duplicados.")

    def ordenar_nombres(self):
        self.lista_nombres.sort()
        print("Lista de nombres ordenada alfabéticamente:")
        for nombre in self.lista_nombres:
            print(nombre)

# Ejemplo de uso
registro = RegistroNombres()
nombres = ["VANESSA", "EMMANUEL", "MELANY", "ARATH", "GAEL", "JULIAN", "SAJITH", "ZULEYMA", "AXEL", "FERNANDA", "JUAN", "AYLIN", "SANTIAGO", "JONATHAN", "XITLALI"]

# Agregar nombres a la estructura de datos
for nombre in nombres:
    registro.agregar_nombre(nombre)

# Ordenar y mostrar la lista de nombres
registro.ordenar_nombres()
from queue import SimpleQueue

nombres = ["VANESSA", "EMMANUEL", "MELANY", "ARATH", "GAEL", "JULIAN", "SAJITH", "ZULEYMA", "AXEL", "FERNANDA", "JUAN", "AYLIN", "SANTIAGO", "JONATHAN", "XITLALI"]

cola_nombres = SimpleQueue()
for nombre in nombres:
    cola_nombres.put(nombre)

pila_nombres_ordenados = []

while not cola_nombres.empty():
    nombre_actual = cola_nombres.get()

    while pila_nombres_ordenados and nombre_actual > pila_nombres_ordenados[-1]:
        cola_nombres.put(pila_nombres_ordenados.pop())

    pila_nombres_ordenados.append(nombre_actual)

print("Nombres ordenados:")
while pila_nombres_ordenados:
    print(pila_nombres_ordenados.pop())

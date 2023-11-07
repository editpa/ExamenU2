importimport queue

def ordenar_nombres(nombres):
    cola = queue.Queue()

    # Llenar la cola con los nombres
    for nombre in nombres:
        cola.put(nombre)

    # Crear una cola de prioridad para ordenar alfabéticamente
    cola_prioridad = queue.PriorityQueue()

    # Vaciar la cola en la cola de prioridad
    while not cola.empty():
        nombre = cola.get()
        cola_prioridad.put(nombre)

    # Extraer los nombres ordenados de la cola de prioridad y guardarlos en una lista
    nombres_ordenados = []
    while not cola_prioridad.empty():
        nombres_ordenados.append(cola_prioridad.get())

    return nombres_ordenados

# Ejemplo de uso
nombres = ["Vanessa", "Emanuel", "Melany", "Arath", "Gael" , "Julian" , "Sajith", "Zuleyma" , "Axel" , "Fernanda" , "Juan" , "Aylin" , "Santiago"]
nombres_ordenados = ordenar_nombres(nombres)
print(nombres_ordenados)





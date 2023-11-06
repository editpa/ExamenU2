#### MELANY MARLEN CHAVEZ ORTIZ
##ListaOrdenada = ["VANESSA","EMMANUEL","MELANY","ARATH","GAEL","JULIAN","SAJITH","ZULEYMA","AXEL","FERNANDA","JUAN","AYLIN","SANTIAGO", "JONATHAN","XITLALI"]
##pila = ITIC3()
##print(ITIC3)
##ITIC3.sort()
##print(ITIC3)

class Cola:
    def __init__(self):
        self.items = []

    def cola(self,x):
        self.items.append(x)
    
    def colaAS(self):
        try:
            return self.items.pop(0)
        except:
            raise ValueError("No hay ningun dato en la cola")
    def print_cola(self):
        print(self.items)


class   ITIC3:
    def __init__(self):
        self.items = []
    
     
    def push(self, item): 
        self.items.insert(0, item)
     
    def pop(self): 
        return self.items.pop(0)
     
    def print_pila(self):
        print(self.items)


ListaOrdenada = ["GAEL","JULIAN","SAJITH","ZULEYMA","VANESSA","EMMANUEL","MELANY","ARATH","AXEL","FERNANDA","JUAN","AYLIN","SANTIAGO", "JONATHAN","XITLALI"]
pila = ITIC3()
pila.push(ListaOrdenada[7])
pila.push(ListaOrdenada[14])
pila.push(ListaOrdenada[0])
pila.push(ListaOrdenada[12])
pila.push(ListaOrdenada[2])
pila.push(ListaOrdenada[10])
pila.push(ListaOrdenada[5])
pila.push(ListaOrdenada[4])
pila.push(ListaOrdenada[9])
pila.push(ListaOrdenada[1])
pila.push(ListaOrdenada[11])
pila.push(ListaOrdenada[8])
pila.push(ListaOrdenada[3])
pila.print_pila()

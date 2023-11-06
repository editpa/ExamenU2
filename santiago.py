class Cola:
    def __init__(self):
        self.items = []

    def cola(self,x):
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


lista = ["VANESSA","EMMANUEL","MELANY","ARATH","GAEL","JULIAN","SAJITH","ZULEYMA","AXEL","FERNANDA","JUAN","AYLIN","SANTIAGO", "JONATHAN","XITLALI"]

#Ejemplo de uso 
Mpila = Pila()
Mpila.push(lista[7])
Mpila.push(lista[14])
Mpila.push(lista[0])
Mpila.push(lista[12])
Mpila.push(lista[2])
Mpila.push(lista[10])
Mpila.push(lista[5])
Mpila.push(lista[4])
Mpila.push(lista[9])
Mpila.push(lista[1])
Mpila.push(lista[11])
Mpila.push(lista[8])
Mpila.push(lista[3])
Mpila.print_pila()





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

nombres = ["VANESSA", "EMMANUEL","MELANY","ARATH", "GAEL","JULIAN", "SAJITH", "ZULEYMA","AXEL","FERNANDA",  "JUAN", "AYLIN", "SANTIAGO", "JONATHAN", "XITLALI"]

#Ejemplo de uso 
Mpila = Pila()
Mpila.push(nombres[7])
Mpila.push(nombres[14])
Mpila.push(nombres[0])
Mpila.push(nombres[12])
Mpila.push(nombres[2])
Mpila.push(nombres[10])
Mpila.push(nombres[5])
Mpila.push(nombres[4])
Mpila.push(nombres[9])
Mpila.push(nombres[1])
Mpila.push(nombres[11])
Mpila.push(nombres[8])
Mpila.push(nombres[3])
Mpila.print_pila()

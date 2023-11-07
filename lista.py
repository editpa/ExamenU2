class Cola:
    def __init__(self):
        self.items = ["VANESSA", "EMMANUEL", "MELANY", "ARATH", "GAEL", "JULIAN", "SAJITH", "ZULEYMA", "AXEL", "FERNANADA", "JUAN", "AYLIN", "SANTIAGO", "JONATHAN", "XITLALI"]

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


#Ejemplo de uso 
Mpila = Pila()
Mpila.push("Zuleyma")
Mpila.push("Xitlali")
Mpila.push("Vanessa")
Mpila.push("Santiago")
Mpila.push("Sajith")
Mpila.push("Melany")
Mpila.push("Julian")
Mpila.push("Juan")
Mpila.push("Jonathan")
Mpila.push("Gael")
Mpila.push("Fernanda")
Mpila.push("Emmanuel")
Mpila.push("Aylin")
Mpila.push("Axel")
Mpila.push("Arath")
Mpila.print_pila()



#Examen de la unidad 2: Ordenar alfabeticamente la siguiente lista con el código de la actividad 23. La calificación se dará de la siguiente manera
#9:10 - 9:30 -> 10 9:30 - 9:40 -> 9 9:40 - 9:50 -> 8 (con internet) 9:50 - 10:00 -> 7 (con internet)
#VANESSA EMMANUEL MELANY ARATH GAEL JULIAN SAJITH ZULEYMA AXEL FERNANDA JUAN AYLIN SANTIAGO JONATHAN XITLALI

#Nidia Vanessa Chávez Rendón IT3

#names = ["Vanessa", "Emmanuel", "Melany", "Arath", "Gael", "Julian", "Sajith", "Zuleyma", "Axel", "Fernanda", "Juan", 
#      "Aylin", "Santiago", "Jonathan", "Xitlali"]
#print(names)
#names.sort()
#def sort_names(names):
#   return sorted(names)
#print (sort_names(names))

class cola:
    def _init_(self):
        self.items = []

    def cola(self,x):
        self.items.append(x)
    
    def colaF(self):
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola está vacía y no tiene información")
    def print_cola(self):
        print(self.items)


class pila:
    def _init_(self):
        self.items = []
    
     
    def push(self, item): 
        self.items.insert(0, item)
     
    def pop(self): 
        return self.items.pop(0)
     
    def print_pila(self):
        print(self.items)


names = ["Vanessa", "Emmanuel", "Melany", "Arath", "Gael", "Julian", "Sajith", "Zuleyma", "Axel", "Fernanda", "Juan", "Aylin", "Santiago", "Jonathan", "Xitlali"]
print(names)
Mpila = pila()
Mpila.push(names[7])
Mpila.push(names[14])
Mpila.push(names[0])
Mpila.push(names[12])
Mpila.push(names[2])
Mpila.push(names[10])
Mpila.push(names[5])
Mpila.push(names[4])
Mpila.push(names[9])
Mpila.push(names[1])
Mpila.push(names[11])
Mpila.push(names[8])
Mpila.push(names[3])
Mpila.print_pila()
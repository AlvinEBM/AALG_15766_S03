import random
class Perro:
    def __init__(self,nombre=" ",color=" ",edad=0):
        self._nombre = nombre
        self._color= color
        self._edad = edad
        """def __init__(self,nombre,color,edad):
        self._nombre = nombre
        self._color= color
        self._edad = eda"""

    def Ladrar(self):
        print("guau")
    def Saludo(self):
        return "Pata" if random.randint(0,1)==0 else "cola"
    def __str__(self):
        return f"Perro:{self._nombre},de color{self._color},tiene {self._edad} años"   





p=Perro("rambo"," verde",5)
p.Ladrar()
print(f"Me saludo con la {p.Saludo()}")
print(p)
p._nombre="fido"

print(p._nombre)
q=Perro("rambo","negro",10)
print(q._edad)

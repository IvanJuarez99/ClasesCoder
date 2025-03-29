class Canino(object):
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Color: {self.color}"
class Caniche(Canino):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)
caniche_1 = Caniche("Firulais", 3, "Blanco")
print(caniche_1)
class Dogo(Canino):
    def __init__(self, name, age, color, peso):
        super().__init__(name, age, color)
        self.peso = peso
    def __str__(self):
        # return f"{super().__str__()}, Peso: {self.peso}"
        return f"Name: {self.name}, Age: {self.age}, Color: {self.color}, Peso: {self.peso}"
dogo_1 = Dogo("Rex", 2, "Marron", 50)
print(dogo_1)
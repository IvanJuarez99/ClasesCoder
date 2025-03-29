class Perro():
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
    def ladrar(self):
        print("Guau, guau")
    def __str__(self):
        return "Perro: {}, Raza: {}".format(self.nombre, self.raza)
perro1 = Perro("Rex", "Pastor Alemán")
print(perro1)
perro1.ladrar()


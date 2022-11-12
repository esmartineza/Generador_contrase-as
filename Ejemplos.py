class Auto:
    Rojo = False
    def __init__(self):
        print("se creo un auto")
    def Fabricar(self):
        Rojo = True
a = Auto()

print(a.Fabricar)

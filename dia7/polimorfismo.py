class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice muu')


class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice beee')


vaca1 = Vaca('Lucrecia')
oveja1 = Oveja('Nube')

animales = [vaca1, oveja1]


# for i in animales:
#     i.hablar()

def animal_habla(animal):
    animal.hablar()


animal_habla(vaca1)

# ejercicio 1
palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

for dato in [palabra, lista, tupla]:
    print(len(dato))

# ejercicio 2
class Mago():
    def atacar(self):
        print("Ataque mágico")


class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")


class Samurai():
    def atacar(self):
        print("Ataque con katana")


m = Mago()
a = Arquero()
s = Samurai()

personajes = [m, a, s]

for i in personajes:
    i.atacar()



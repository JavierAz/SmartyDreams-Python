class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.cambio = especie


mi_pajaro = Pajaro('amarillo', 'Tucan')

# print(mi_pajaro.color, mi_pajaro.cambio)
print(f'Mi parajaro {mi_pajaro.color} es {mi_pajaro.cambio} y tiene alas? {mi_pajaro.alas}')


class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos


casa_blanca = Casa('blanco', 4)


class Cubo:
    caras = 6

    def __init__(self, color):
        self.color = color


cubo_rojo = Cubo('rojo')


class Personaje:
    real = False

    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad


harry_potter = Personaje('humano', True, 17)
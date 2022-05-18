class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.cambio = especie

    def piar(self):
        print(f'pio mi color es {self.color}')

    def volar(self, metros):
        print(f'el pajaro a voldado {metros} metros')


piolin = Pajaro('amarillo', 'canario')
piolin.piar()
piolin.volar(10)


class Perro:

    def ladrar(self):
        print('Guau!')


class Mago:
    def lanzar_hechizo(self):
        print('¡Abracadabra!')


merlin = Mago()
merlin.lanzar_hechizo()


class Alarma:
    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")

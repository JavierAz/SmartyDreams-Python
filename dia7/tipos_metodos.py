class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.cambio = especie

    def piar(self):
        print(f'pio mi color es {self.color}')

    def volar(self, metros):
        print(f'el pajaro a voldado {metros} metros')

    # los metodos de instancia pueden modificar atributos

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'puso {cantidad} de huevos')
        cls.alas = False
        print(Pajaro.alas)

    @staticmethod
    def mirar():
        print('solo puede mirar')


piolin = Pajaro('amarillo', 'canario')
Pajaro.poner_huevos(3)
Pajaro.mirar()


class Mascota:

    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")


class Jugador():
    vivo = False

    def revivir(self):
        self.vivo = True


class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas = self.cantidad_flechas - 1

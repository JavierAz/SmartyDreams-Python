"""
Aqui se generan los numeros para la consola de turnos y los decoradores
"""


def cosmeticos():
    turno = 0
    while True:
        turno += 1
        yield f'C - {turno}'


def perfumeria():
    turno = 0
    while True:
        turno += 1
        yield f'P - {turno}'


def farmacia():
    turno = 0
    while True:
        turno += 1
        yield f'F - {turno}'


c = cosmeticos()
p = perfumeria()
f = farmacia()


def decorador(destino):
    print('\nSu numero es:')
    if destino == 'c':
        print(next(c))
    elif destino == 'p':
        print(next(p))
    elif destino == 'f':
        print(f)

    print('Gracias por esperar!')
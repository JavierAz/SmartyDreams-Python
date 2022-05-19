def decorar(funcion):
    def otra(palabra):
        print('Hola')
        print(palabra)
        print('Adios')

    return otra


@decorar
def mayus(txt):
    print(txt.upper())


@decorar
def minus(txt):
    print(txt.lower())


mayus('Javier')

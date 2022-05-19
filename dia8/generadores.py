def funcion():
    lista = []

    for i in range(1, 5):
        lista.append(i * 10)
    return lista


def generador():
    for i in range(1, 5):
        yield i * 10


print(funcion())

g = generador()
print(next(g))
print(next(g))
print(next(g))


# ejercicio 1
def gen():
    n = 0
    while True:
        n += 1
        yield n


generador = gen()


# ejercicio 2
def gen2():
    n = 7
    m = 1
    while True:
        res = n * m
        m += 1
        yield res


generador = gen2()


# ejercicio 3
def gen3():
    x = "Te quedan 3 vidas"
    yield x

    x = "Te quedan 2 vidas"
    yield x

    x = "Te queda 1 vida"
    yield x

    x = "Game Over"
    yield x


perder_vida = gen3()

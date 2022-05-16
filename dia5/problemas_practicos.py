seleccion = int(input('Numero de solucion [1-25]'))


def devolverDistintos(x, y, z):
    sum = x + y + z
    lis = [x, y, z]

    if sum > 15:
        return max(lis)
    elif sum < 10:
        return min(lis)
    else:
        lis.sort()
        # print(lis)
        return lis[1]


def letrasUnicas(texto):
    miSet = set()

    for t in texto:
        miSet.add(t)

    lista = list(miSet)
    lista.sort()

    return lista


def sinVecinos(*args):
    cont = 0
    for i in args:
        if cont + 1 == len(args):
            return False
        elif args[cont] == 0 and args[cont + 1] == 0:
            return True
        else:
            cont += 1
    return False


def primos(numero):
    pri = [2]
    it = 3

    if numero < 2:
        return 0

    while it <= numero:
        for i in range(3, it, 2):
            if it % i == 0:
                it += 2
                break
        else:
            pri.append(it)
            it += 2

    print(pri)
    return len(pri)


if seleccion == 1:
    distintos = devolverDistintos(5, 2, 1)
    print(distintos)

elif seleccion == 2:
    letras = letrasUnicas('Azanza')
    print(letras)

elif seleccion == 3:
    vecinos = sinVecinos(1, 2, 4, 5, 6, 7, 0, 1)
    print(vecinos)

elif seleccion == 4:
    print(primos(50))

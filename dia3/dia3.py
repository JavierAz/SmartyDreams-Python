seleccion = int(input('Numero de practica [1-25]'))

if seleccion == 1:
    palabra = 'ordenador'
    print(palabra[5])

elif seleccion == 2:
    frase = 'En toria, la teoria y la practica son los mismos. En la practica, no lo son'
    print(frase.index('p'))

elif seleccion == 3:
    frase = 'En toria, la teoria y la practica son los mismos. En la practica, no lo son'
    print(frase.rindex('p'))

elif seleccion == 4:
    frase = 'Controlar la complejidad es la esencia de la programacion'
    print(frase[0:9])

elif seleccion == 5:
    frase = 'Nunca confies en un ordenador que no puedas lanzar por una ventana'
    print(frase[9:len(frase):3])

elif seleccion == 6:
    frase = 'es genial  trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza'
    res = list(frase)
    res.reverse()
    print(res)

elif seleccion == 7:
    frase = 'Especialmente en las comunicaciones electronicas, la escritura enteramente en mayusculas equivale a gritar'
    print(frase.upper())

elif seleccion == 8:
    lista = ['La', 'Legibilidad', 'Cuenta.']
    res = ' '.join(lista)
    print(res)

elif seleccion == 9:
    frase = 'Si la implementacion es dificil de explicar, puede que sea una mala idea'
    res1 = frase.replace('dificil', 'facil')
    res2 = res1.replace('mala', 'buena')
    print(res2)

elif seleccion == 10:
    print('repeticion \n' * 15)

elif seleccion == 11:
    texto = """Tierra mojada
    mis recuerdos de viaje,
    entre las  lluvias"""
    res = 'agua'
    print(res in texto)

elif seleccion == 12:
    palabra = 'electroencefalograma'
    print(len(palabra) + 1)

elif seleccion == 13:
    lista1 = ['avion', 'auto', 'barco', 'bicicleta']
    lista1.append('motocicleta')
    print(lista1)

elif seleccion == 14:
    frutas = ['manzana', 'banana', 'mango', 'cereza', 'sandia']
    frutas.pop(3)
    print(frutas)

elif seleccion == 15:
    mi_dic = {
        'nombre': 'Karen',
        'apellido': 'Jurgens',
        'edad': 35,
        'ocupacion': 'periodista'
    }

    print(mi_dic)

elif seleccion == 16:
    mi_dic = {
        "valores_1": {'v1': 3, 'v2': 6},
        "puntos": {'points1': 9, 'points2': [10, 300, 15]}
    }

    print(mi_dic['puntos']['points2'][1])

elif seleccion == 17:
    mi_dic = {
        'nombre': 'Karen',
        'apellido': 'Jurgens',
        'edad': 35,
        'ocupacion': 'periodista'
    }

    mi_dic['pais'] = 'Argentina'

    print(mi_dic)

elif seleccion == 18:
    s = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 1, 3, 2, 2, 1, 3, 2)
    print(s.count(2))

elif seleccion == 19:
    s = (1, 2, 3, 4)
    mi_lista = list(s)

    print(mi_lista)

elif seleccion == 20:
    set1 = {1, 2, 'tres', 'cuatro'}
    set2 = {'tres', 4, 5}

    set3 = set1.union(set2)
    print(set3)

elif seleccion == 21:
    sorteo = {'Camila', 'Margarita', 'Axel', 'Jorge', 'Miguel'}

    ganador = sorteo.pop()

    print(ganador)

elif seleccion == 22:
    sorteo = {'Camila', 'Margarita', 'Axel', 'Jorge', 'Miguel'}

    sorteo.add('Damian')
    print(sorteo)

elif seleccion == 23:
    prueba = 2 <= 5

    print(prueba)

elif seleccion == 24:
    print(17834 / 34 > 87 * 56)

elif seleccion == 25:
    print(25 ** 0.5 == 5)

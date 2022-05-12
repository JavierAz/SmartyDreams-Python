seleccion = int(input('Numero de practica [1-5]'))

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

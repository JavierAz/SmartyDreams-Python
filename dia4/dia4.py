from random import *

seleccion = int(input('Numero de practica [1-25]'))

if seleccion == 1:
    num1 = 36
    num2 = 17
    mi_bool = num1 >= num2
    if mi_bool:
        print(f'El numero {num1} es mayor o igual al {num2}')
    else:
        print(f'El numero {num1} no es mayor o igual al {num2}')

elif seleccion == 2:
    num1 = 25 ** 0.5
    num2 = 5
    mi_bool = num1 == num2
    if mi_bool:
        print(f'{num1} es igual al {num2}')
    else:
        print(f'{num1} no es igual al {num2}')

elif seleccion == 3:
    num1 = 64 * 3
    num2 = 24 * 8
    mi_bool = not num2 == num1
    if mi_bool:
        print(f'son diferentes')
    else:
        print(f'son diferentes')
elif seleccion == 4:
    num1 = 36
    num2 = 72 / 2
    num3 = 48
    mi_bool = (num1 > num2) and (num1 < num3)
    if mi_bool:
        print('No se cumple')

elif seleccion == 5:
    num1 = 36
    num2 = 72 / 2
    num3 = 48
    mi_bool = (num1 > num2) or (num1 <= num3)
    if mi_bool:
        print('No se cumple')

elif seleccion == 6:
    palabra1 = 'exito'
    palabra2 = 'tecnologia'
    texto = 'Cuando algo es suficiente importante, lo hacesincluso si las posibilidades de que salga bien no te ' \
            'acompañe '
    mi_bool = bool(palabra1 in texto and palabra2 in texto)
    print(mi_bool)

elif seleccion == 7:
    num1 = int(input('Numero1:'))
    num2 = int(input('Numero2:'))
    if num1 > num2:
        print(f'{num1} es mayor a {num2}')
    elif num2 > num1:
        print(f'{num1} es mayor a {num2}')
    else:
        print('Son iguales')
elif seleccion == 8:
    edad = 16
    licencia = False

    if edad >= 18 and licencia == True:
        print('Puedes conducir')
    elif edad >= 18 and licencia == False:
        print('Necesitas una licencia')
    else:
        print('Tienese que ser mayor de edad')

elif seleccion == 9:
    ingles = False
    py = True

    if ingles and py:
        print('Te puedes postular')
    elif ingles != True and py:
        print('Necesitas aprender ingles')
    elif ingles and py != True:
        print('Necesitas aprender python')
    else:
        print('No cumples con los requisitos')

elif seleccion == 10:
    alumnos = ['Juan', 'Maria', 'Ton']

    for i in alumnos:
        print(f'Hola {i}')

elif seleccion == 11:
    nums = [1, 54, 2, 4, 2, 4, 8, 4]
    suma = 0
    for i in nums:
        suma += i
    print(f'Total: {suma}')

elif seleccion == 12:
    lista = [12, 11, 4, 7, 8, 90, 10]
    sumaPar = 0
    sumaImpar = 0
    for i in lista:
        if i % 2 == 0:
            sumaPar += i
        elif i % 2 != 0:
            sumaImpar += i

    print(f'Los pares suman: {sumaPar} \nLos impares suman {sumaImpar}')

elif seleccion == 13:
    inicio = 10
    while inicio >= 0:
        print(inicio)
        inicio -= 1

elif seleccion == 14:
    inicio = 50
    while inicio >= 0:
        if inicio % 5 == 0:
            print(inicio)
        inicio -= 1

elif seleccion == 15:
    lista = [1, 4, 3, 54, -2, 1, 43, 5, -1]
    for i in lista:
        if i < 0:
            break
        print(i)

elif seleccion == 16:
    for i in range(2500, 2586):
        print(i)

elif seleccion == 17:
    res = [i for i in range(3, 301, 3)]
    print(res)

elif seleccion == 18:
    sumaCuadrados = 0
    for i in range(1, 16):
        sumaCuadrados += i ** 2
    print(sumaCuadrados)

elif seleccion == 19:
    nombres = ['Juan', 'Javier', 'Maria', 'Lupe']
    for i in enumerate(nombres):
        print(f'{i[1]} es en la posición {i[0]}')

elif seleccion == 20:
    capitales = ['Berlin', 'Tokio', 'Paris', 'Ottawa', 'Canberra']
    paises = ['Alemnia', 'Japon', 'Francia', 'Canada', 'Australia']

    combinados = list(zip(capitales, paises))
    print(f'{combinados[0]} es la capital de {combinados[1]}')

elif seleccion == 21:
    marcas = ['HP', 'Dell', 'Google', 'Apple']
    productos = ['Zen', 'XPS', 'Chomebook', 'iMac']

    mi_zip = list(zip(marcas, productos))

elif seleccion == 22:
    esp = ['uno', 'dos', 'tres']
    por = ['um', 'dois', 'tres']
    en = ['one', 'two', 'three']

    numeros = list(zip(esp, por, en))
    print(numeros)

elif seleccion == 23:
    numeros = [44542247 / 2, 21310 / 5, 2134747 * 33, 44556475, 121676, 6654067, 353254, 123134, 55 ** 12, 611 ** 5]

    maxi = max(numeros)
    print(maxi)

elif seleccion == 24:
    numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

    rango = max(numeros) - min(numeros)
    print(rango)

elif seleccion == 25:
    diccionario_edades = {"Carlos": 55, "María": 42, "Mabel": 78, "José": 44, "Lucas": 24, "Rocío": 35, "Sebastián": 19,
                          "Catalina": 2, "Darío": 49}

    edadMinima = min(diccionario_edades.values())
    ultimo = max(diccionario_edades.keys())
    print(f'el menor es {edadMinima} el ultimo es {ultimo}')

elif seleccion == 26:
    ran = randint(1, 10)
    print(ran)

elif seleccion == 27:
    ran = random()
    print(ran)

elif seleccion == 28:
    nombres = ["Javier", "Juan", "Alo", "Laura", "Lola"]

    sorteo = choice(nombres)
    print(sorteo)

elif seleccion == 29:
    val = [1, 4, 7, 9, 3, 5]
    cuadrados = [i ** 2 for i in val]
    print(cuadrados)

elif seleccion == 30:
    val = [1, 4, 7, 9, 3, 5]
    pares = [i for i in val if i % 2 == 0]
    print(pares)

elif seleccion == 31:
    far = [32, 275, 212]
    cel = [(tem - 32) * (5 / 9) for tem in far]

    print(f'{far}farenheit = {cel} celsius')

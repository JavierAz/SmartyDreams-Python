import random

seleccion = int(input('Numero de solucion [1-25]'))

if seleccion == 1:
    texto = 'Tienes# que_quitar, de todo : un po%co '
    print(texto.lstrip('#,:%_'))

elif seleccion == 2:
    frutas = ['mango', 'kiwi', 'platano', 'manzana']
    frutas.insert(3, 'naranja')
    print(frutas)

elif seleccion == 3:
    celulares = {'Apple', 'Samsung', 'Oppo', 'Xiaomi'}
    tv = {'Sony', 'LG', 'Samsung'}

    aislado = tv.isdisjoint(celulares)
    print(aislado)

elif seleccion == 4:
    def saludar():
        print('Hola')


    print(saludar())

elif seleccion == 5:
    nombre = 'Javier'


    def bienvenida(nombre):
        print(f'Hola {nombre}')


    print(bienvenida(nombre))

elif seleccion == 6:
    numero = 8


    def cuadrado(numero):
        return numero ** 2


    print(cuadrado(numero))

elif seleccion == 7:
    base = 5
    exponente = 2


    def exp(n1, n2):
        return n1 ** n2


    print(exp(base, exponente))

elif seleccion == 8:
    dol = 123


    def dol_peso(dolares):
        return dolares * 20.50


    print(dol_peso(dol))

elif seleccion == 9:
    texto = 'Hola Persona'


    def invertir(texto):
        texto = texto[::-1]
        texto = texto.upper()
        return texto


    print(invertir(texto))

elif seleccion == 10:
    numeros = [1, -5, 300, -987, 32]


    def positivos(lista):
        for i in lista:
            if i < 0:
                return False
            else:
                pass
        return True


    print(positivos(numeros))

elif seleccion == 11:
    numeros = [1, 5, 8, 2, 10]


    def sumaMenores(lista):
        sum = 0
        for i in lista:
            if i in range(1, 1000):
                sum += 1
            else:
                pass
        return sum


    print(sumaMenores(numeros))

elif seleccion == 12:
    numeros = [1, 50, 502, 5000, 755, 600, 33, 61]


    def cantidadPares(lista):
        cantidad = 0
        for numero in lista:
            if numero % 2 == 0:
                cantidad += 1
            else:
                pass
        return cantidad

elif seleccion == 13:
    def lanzar():
        return random.randint(1, 6)


    def jugar(v1, v2):
        sumar = v1 + v2
        if sumar <= 6:
            return print(f'La sumade tus dados fue {sumar}, no parece muy buena')
        elif 6 < sumar < 10:
            return print(f'La suma de tus dados es {sumar} parece buena')
        else:
            return print(f'La suma de tus dados es {sumar} parece una jugada ganadora')


    jugar(lanzar(), lanzar())

elif seleccion == 14:
    lista = [1, 67, 54, 32, 89]


    def lanzarMoneda():
        resultado = random.choice(["Cara", "Cruz"])
        return resultado


    def suerte(moneda, lista):
        if moneda == "Cara":
            print("La lista se autodestruirá")
            return []
        elif moneda == "Cruz":
            print("La lista fue salvada")
            return f'{lista}', lista


    suerte(lanzarMoneda(), lista)

elif seleccion == 15:
    def cuadrados(*args):
        res = 0
        for i in args:
            res += i ** 2

        return res


    print(cuadrados(1, 2, 6, 8, 9))

elif seleccion == 16:
    def absolutos(*args):
        res = 0
        for i in args:
            res += abs(i)

        return res

elif seleccion == 17:
    def numPersona(nombre, *args):
        suma = sum(args)
        return f'Hola {nombre} la suma es {suma}'

elif seleccion == 18:
    def total(**kwargs):
        res = 0
        for i in kwargs:
            res += 1
        return res

elif seleccion == 19:
    def listarArgumentos(**kwargs):
        lista = []
        for i in kwargs.values():
            lista.append(i)
        return lista

elif seleccion == 20:
    def describirPersona(nombre, **kwargs):
        print(f"Características de {nombre}:")
        for clave, valor in kwargs.items():
            print(f'{clave}: {valor}')
        return 0

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

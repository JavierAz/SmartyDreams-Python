# variables
# lista = [1,'hola',1]
#
# print(lista[1])

seleccion = int(input('Numero de practica [1-5]'))

if seleccion == 1:
    nombre = 'Tony'
    apellido = 'Soprano'
    edad = 51

    nombreCompleto = nombre + apellido
    print(nombreCompleto)

    nombre = 'Julia'
    apellido = 'Roberts'
    nombreCompleto = nombre + apellido
    print(nombreCompleto)

elif seleccion == 2:
    curso = 'python'
    print(f'Esrtas tomando el curso de {curso}')

    nom = input('Asociado: ')
    num = input('Numero del asociado: ')

    print(f'Estimado {nom}, su numero es: {num}')

    puntos = int(input('Cuantos puntos se le han asignado este mes: '))
    print(f'Has ganado {puntos}, nos da un total de {puntos + 25}')

elif seleccion == 3:
    num1 = int(input('Ingrese el primer numero: '))
    num2 = int(input('Ingrese el segundo numero: '))

    print(f'El redondeo de {num1} sobre {num2} es', round(num1 / num2, 2))

elif seleccion == 4:
    n1 = float(input('Ingrese un decimal: '))
    print(f'El redeonde de {n1} es ', str(round(n1)))

elif seleccion == 5:
    print(f'Raiz cuadrada de 5 es', round(5 ** 1 / 2, 4))

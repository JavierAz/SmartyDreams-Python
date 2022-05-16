# proyecto del dia 4
# pregunta su nombre
# un numero entre el numero y el 100
# validaciones en rangos
# si es que leatina

from random import randint

vidas = 10
intentos = 0
numero = randint(1, 100)
nombre = input('Ingresa tu nombre: ')

print(
    f'{nombre} Tienes que  adivinar un numero que pense entre 1 y 100, tienes {vidas} vidas.\nQue la suerte este contigo!')

while vidas >= 0:
    intentos = int(input('Prueba: '))
    vidas += 1

    if intentos < numero:
        print('Un numero mas grande')
    elif intentos > numero:
        print('Un numero mas chico')
    else:
        print(f'{nombre.capitalize()} en Horabuena felicidades!')
        break

if intentos != numero:
    print(f'Haz perdido, el numero era: {numero}')

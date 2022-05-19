from Paquete_Jav import suma_resta

print(suma_resta.suma([1, 2, 3, 4]))

try:
    suma_resta.resta(1, '2')

except TypeError:
    print('Algo salio mal')

except ValueError:
    print('No fue lo esperado')

finally:
    pass


# ejercicio 1

def suma(num1, num2):
    try:
        print(num1 + num2)

    except:
        print('Error inesperado')

# ejercicio 2
def cociente(num1, num2):
    try:
        print(num1 / num2)

    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")


# ejercicio 3
def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")
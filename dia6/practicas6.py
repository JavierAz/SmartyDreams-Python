import os
from pathlib import Path

archivo1 = open('texto.txt')

seleccion = int(input('Numero de solucion [1-25]'))

if seleccion == 1:
    for i in archivo1:
        print(i.rstrip())

elif seleccion == 2:
    linea = archivo1.readlines()
    print(linea)

elif seleccion == 3:
    linea2 = archivo1.readlines()[1]
    print(linea2)

elif seleccion == 4:
    archivo2 = open('mi_archivo.txt', 'w')
    archivo2.write('Esta es una prueba\nOk')

    archivo2.close()

elif seleccion == 5:
    archivo2 = open('mi_archivo.txt', 'a')

    archivo2.write('Esta debe ser la ultima linea')

    archivo2.close()

elif seleccion == 6:
    archivo2 = open('mi_archivo.txt', 'w')
    registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
    for l in registro_ultima_sesion:
        archivo2.writelines(l + '\t')

    archivo2.close()

elif seleccion == 7:
    # obtiene la ruta
    ruta_base = Path.home()
    # cambiar de ruta .chdir('/home/javier/Desktop/')
    # hace directorios .makedirs('/path/')
    print(ruta_base)
elif seleccion == 8:
    ruta = Path('Cuso Python', 'Dia 6', 'practicas.py')

elif seleccion == 9:
    home = Path.home()
    ruta = Path(home, 'Curso Python', 'Dia 6', 'practicas.py')

elif seleccion == 10:
    def abriArchivos(archivoNombre):
        archivo = open(archivoNombre, 'w')
        archivo.write('Contenido eliminado')
        archivo.close()

elif seleccion == 11:
    def mi_log(logError):
        archivo = open(logError, 'a')
        archivo.write('Se a registrado unaaccion')
        archivo.close()

archivo1.close()

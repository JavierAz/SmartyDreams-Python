import re
import shutil, time, os, datetime, math, os
from pathlib import Path

# shutil.unpack_archive('Proyecto+Dia+9.zip','/home/javier/PycharmProjects/SmartyDreams-Python/dia9')
inicio = time.time()
ruta = os.path.abspath(os.getcwd())
print(ruta)

patron = r'N\D{3}-\d{5}'
hoy = datetime.date.today()
nums_encontrados = []
arch_encontrado = []


def buscar(archivo, clave):
    arch = open(archivo, 'r')
    textp = arch.read()

    if re.search(clave, textp):
        return re.search(clave, textp)
    else:
        return ''


def crear():
    for carpeta, subs, arch in os.walk(ruta):
        for i in arch:
            res = buscar(Path(carpeta, i), patron)
            if res != '':
                nums_encontrados.append((res.group()))
                arch_encontrado.append(i.title())


def mostrar():
    index = 0
    print(f'Dia de la busqueda: {hoy.day}/{hoy.month}/{hoy.year}\n')
    print('Arch\t\t\tNum. Serie')
    print('-----\t\t\t---------')
    for i in arch_encontrado:
        print(f'{i}\t{nums_encontrados[index]}')
        index += 1
    print('\n')
    print(f'Num encontrados: {len(nums_encontrados)}')
    fin = time.time()
    duracion = fin - inicio
    print(f'Tardamos en encontrar: {math.ceil(duracion)}\n\n')


crear()
mostrar()

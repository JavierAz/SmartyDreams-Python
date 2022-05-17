import os
from pathlib import Path
from os import system

# ruta de las recetas
ruta_general = Path(Path.home(), 'Recetas')


def total_recetas(ruta):
    cont = 0
    for i in Path(ruta).glob('**/*'):
        cont += 1
    return cont


def inicio():
    system('clear')
    print('Bienvenido al recetario!')
    print(f'Contamos con {total_recetas(ruta_general)}')

    eleccion = 's'
    while not eleccion.isnumeric() or int(eleccion) not in range(1, 7):
        print("""Selecciona una de las operaciones:
        \t[1] leer receta
        \t[2] crear receta
        \t[3] crear categoria
        \t[4] eliminar receta
        \t[5] eliminar categoria
        \t[6] finalizar programa
        """)
        eleccion = input()

    return int(eleccion)


def categorias(ruta):
    print('Categorias:')
    ruta_categorias = Path(ruta)
    lista_categorias = []
    cont = 1

    for i in ruta_categorias.iterdir():
        carpeta = str(i.name)
        print(f'{cont} - {carpeta}')
        lista_categorias.append(i)
        cont += 1
    return lista_categorias


def categorias_id(lista):
    categoria_id = 'x'

    while not categoria_id.isnumeric() or int(categoria_id) not in range(1, len(lista) + 1):
        categoria_id = input('Elige la categoria: ')
    return lista[int(categoria_id)-1]


def mostrar_recetas(ruta):
    print('Recetas: ')
    ruta_recetas = Path(ruta)
    lista_recetas = []
    cont = 1

    for i in ruta_recetas.glob('*.txt'):
        receta_str = str(i.name)
        print(f'{cont} - {receta_str}')
        lista_recetas.append(i)
        cont += 1

    return lista_recetas


def receta_id(lista):
    receta_elec = 'x'

    while not receta_elec.isnumeric() or int(receta_elec) not in range(1, len(lista) + 1):
        receta_elec = input('Elige una receta: ')

    return lista[int(receta_elec) - 1]


def abrir_receta(id):
    print(Path.read_text(id))


def crear_receta(ruta):
    exist = False

    while not exist:
        print('Nombre de la receta: ')
        receta_nombre = input() + '.txt'
        print('Escribe la receta: ')
        cuerpo = input()
        ruta_creada = Path(ruta, receta_nombre)

        if not os.path.exists(ruta_creada):
            Path.write_text(ruta_creada, cuerpo)
            print(f'Se a dado de alta la receta {receta_nombre}!:)')
            exist = True
        else:
            print('Ya existe esa receta!:(')


def crear_categoria(ruta):
    exist = False

    while not exist:
        print('Nombre de la Categoria: ')
        categoria_nombre = input()

        ruta_creada = Path(ruta, categoria_nombre)

        if not os.path.exists(ruta_creada):
            Path.mkdir(ruta_creada)
            print(f'Se a dado de alta la Categoria {categoria_nombre}!:)')
            exist = True
        else:
            print('Ya existe esa categoria!:(')


def borrar_receta(id):
    Path(id).unlink()
    print(f'Se a eliminado la receta {id.name}')


def borrar_categoria(id):
    Path(id).rmdir()
    print(f'Se a eliminado la categoria {id.name}')


def volver():
    eleccion_regresar = 'x'

    while eleccion_regresar.lower() != 's':
        eleccion_regresar = input('Se desa continuar? (s/n) ')


# mostrar las operaciones
fin = False

while not fin:

    seleccion = inicio()

    if seleccion == 1:
        categorias_total = categorias(ruta_general)
        categoria_select = categorias_id(categorias_total)
        recetas_total = mostrar_recetas(categoria_select)
        receta_select = receta_id(recetas_total)
        abrir_receta(receta_select)
        volver()

    elif seleccion == 2:
        categorias_total = categorias(ruta_general)
        categoria_select = categorias_id(categorias_total)
        crear_receta(categoria_select)
        volver()

    elif seleccion == 3:
        crear_categoria(ruta_general)
        volver()

    elif seleccion == 4:
        categorias_total = categorias(ruta_general)
        categoria_select = categorias_id(categorias_total)
        recetas_total = mostrar_recetas(categoria_select)
        receta_select = receta_id(recetas_total)
        borrar_receta(receta_select)
        volver()

    elif seleccion == 5:
        categorias_total = categorias(ruta_general)
        categoria_select = categorias_id(categorias_total)
        borrar_categoria(categoria_select)
        volver()

    elif seleccion == 6:
        fin = True

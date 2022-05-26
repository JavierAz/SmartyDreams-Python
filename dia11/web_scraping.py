import bs4
import requests

# crea la URLque espera el numero de pagina
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# lista oara los titulos con 4 o 5 estrellas
titulos_buenos = []

# iterar paginas
for i in range(1, 52):
    # crear soppa en cada pagina
    url_pagina = url_base.format(i)
    res = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(res.text, 'lxml')

    # seleccion de los libros
    libros = sopa.select('.product_pod')

    # iterar los libros
    for libro in libros:
        # validar que tengan 4 o mas estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')):
            # guardar titulo
            titulo_libro = libro.select('a')[1]['title']

            # agregar libro a la lista
            titulos_buenos.append(titulo_libro)

# ver los libros
for t in titulos_buenos:
    print(t)

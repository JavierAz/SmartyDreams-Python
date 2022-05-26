import bs4, requests

res = requests.get('https://escueladirecta-blog.blogspot.com/')

sop = bs4.BeautifulSoup(res.text, 'lxml')
print(sop.select('h1')[0].getText())

columna_lateral = sop.select('.featured-post section')
# print(columna_lateral)

for p in columna_lateral:
    print(p.getText)

# extraes imagenes de una pagina
imagenes = sop.select('img')[0]['src']
print(imagenes)
imagen_1 = requests.get(imagenes)
f = open('mi_imagen.jpg', 'wb')
f.write(imagen_1.content)
f.close()

# for i in imagenes:
#    print(i)

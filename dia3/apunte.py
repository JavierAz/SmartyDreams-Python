text = 'Hola Mundo'
# muestra la posicion en la que se encuentra
print(text.index('Mundo'))
# muestra la posicion en la que esta
print(text[5])

# fragmentar strings
abec = 'ABCDEFGHIJKLM'
# indice 1 es donde inicia, el segundo indice es donde termina, el tercer indice es para ir saltando
fragmento = abec[2:5:2]
print(fragmento)

# metodos
# upper() cambia elstring a mayusculas
# lower() cambia el string a minusculas
# split()
prueba = 'Esto es un texTo'
res = prueba[3].upper()
print(res)
res = prueba.split('t')
print(res)

a = 'aprender'
b = 'Python'
c = 'es'
d = 'divertido'
e = " ".join([a, b, c, d])
print(e)

encontrar = e.find("P")
print(encontrar)
reemplazar = e.replace('aprender', 'entender')
print(reemplazar)

poema = """Mil pequeños peces blancos
comosi hirviera
el color del agua"""

print(poema)

# listas
lista1 = ['hola', 123, 0.99, ['1', 2]]
print(lista1[2:len(lista1)])

lista1.append('mundo')
print(lista1[2:len(lista1)])

eliminado = lista1.pop(1)
print(lista1)
print(eliminado)

lista1.reverse()
print(lista1)

# diccionarios
diccionario = {
    'nombre': 'Juan',
    'ap': 'Lopez'
}
diccionario['num'] = [1, 2, 3]
print(diccionario)

# tuplas
tupla = 1, 2, 3, 4, 'test'
print(tupla)
print(tupla[2])

# sets
miSet = {1, 2, 3, 4, 5}

print(type(miSet))
miSet.add(6)
print(miSet)

miSet.discard(3)
print(miSet)

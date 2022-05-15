miBool = not 5 > 4 and 4 < 6

if miBool:
    print('es correcto')

imprimir = ['Jav', 'Luz', 'Cris', 'pepe']
for e in imprimir:
    print(f'en la posiscion {imprimir.index(e)} es ' + e)

dic = {'cla1': 3, 'Clave2': {1, 2, 3}, 'clave3': 'Jav'}

for i in dic.values():
    print(i)

for i in dic.items():
    print(i)

monedas = 4
while monedas > 0:
    print(f'Tengo {monedas}')
    monedas -= 1

res = 's'
while res == 's':
    res = input('Quieres seguir? (s/n)')
else:
    print('gracias')

nom = input('Nombre: ')
for l in nom:
    if l == 'j':
        break
    print(l)

# rangos
# rango(indice 1 es inicio, indice en 2 es elfin, indice 3 son los altos
for numero in range(10, 21, 2):
    print(numero)

# enumerado
lista = ['a', 'b', 'c']
for item in enumerate(lista):
    print(item)

# zip
nombres = ['ana', 'lupe', 'maria']
edades = [12, 18, 29]

combinados = list(zip(nombres, edades))
print(combinados)

# min y max
print(min([1, 2, 8, 3, 4, 5]))

print(max([10, 43, 53, 10]))

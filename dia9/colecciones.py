from collections import Counter, defaultdict, namedtuple, deque

# Counter
nums = [1, 8, 2, 8, 6, 4, 1, 3]
frase = 'al pan pan y al vino vino'
seri = Counter(frase.split())
print(seri)
print(seri.most_common(2))

# defaultdict
mi_dic = defaultdict(lambda: 'nada')
mi_dic['a1'] = 'azul'
print(mi_dic['a1'])

# tuplas de nombres
Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
dante = (Persona('Dante', 1.50, 40))
print(dante.peso)
print(dante[0])

# ejercicio 1
lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]
contador = Counter(lista)

# ejercicio 2
mi_diccionario = defaultdict(lambda: "Valor no hallado")
mi_diccionario["edad"] = 44

# ejercicio 3
lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])

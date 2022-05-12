# analizador de texto
# que ingrese un texto
# que ingrese 3 letras
# devolver cuantas veces aparece la letra en el texto
# cuantas palabras hay
# cual es la primera letra del inicio y la ultima
# aparece python?

texto = input('Ingrese un texto: ').lower()
letra1 = input('Ingrese una letra: ').lower()
letra2 = input('Ingrese una letra: ').lower()
letra3 = input('Ingrese una letra: ').lower()

print(f'dentro del texto la `{letra1}` aparece {texto.count(letra1)}')
print(f'dentro del texto la `{letra2}` aparece {texto.count(letra2)}')
print(f'dentro del texto la `{letra3}` aparece {texto.count(letra3)}')

palabras = texto.split()
print(f'Tiene un total de palabras de {len(palabras)}')

last = palabras[len(palabras) - 1]
lastOne = len(last)

print(f'Inicia con la letra {palabras[0].__getitem__(0).upper()} y termina con la letra {last[lastOne - 1:]}')

if 'python' in texto:
    print('Si aparece')

else:
    print('No se encuetra')
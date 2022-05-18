lis1 = [1, 1, 1, 1, 1, 1]
print(len(lis1))


class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f'Album: {self.titulo} de {self.autor}'

    def __len__(self):
        return self.canciones

    def __del__(self):
        print('Se a eliminado')


mi_cd = CD('U2', 'Sound', 24)

print(mi_cd, len(mi_cd))
del mi_cd


# ejercicio 1
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'

    # ejercicio 2
    def __len__(self):
        return self.cantidad_paginas

    def __del__(self):
        print('Libro eliminado')
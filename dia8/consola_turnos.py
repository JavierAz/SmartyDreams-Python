"""
Un numero de turno a donde es que vas a presentarte
Cosmeticos
Enfermeria
Perfumeria
"""
from Paquete_Jav import numeros


def destino():
    print('Bienvenido!')

    while True:
        print("""
        A donde se dirige?
        \t(P) Perfumería
        \t(C) Cosmeticos
        \t(F) Farmacia
        """)

        try:
            des = input("Por favor ingrese su seleccion:").lower()
        except ValueError:
            print('Porfavor ingrese una opcion valida!')
        else:
            break

    numeros.decorador(des)


def Inicio():
    while True:
        destino()
        try:
            o_turno = input('Desea sacar otro turno? (y/n)').lower()
        except ValueError:
            print('Opcion invalida, ingrese de nuevo')
        else:
            if o_turno == 'n':
                print('Vuelva pronto!')
                break


Inicio()
# if __name__ == '__main__':
#     Inicio.main()

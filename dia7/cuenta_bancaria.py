class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f'Bienvenido {self.apellido} {self.nombre} tiene en su cuenta {self.numero_cuenta}: ${self.balance}'

    def depositar(self, cantidad):
        self.balance += cantidad
        print('Se a depositado')

    def retirar(self, cantidad):
        if self.balance >= cantidad:
            self.balance -= cantidad
            print('Tome su dinero')

        else:
            print('No tienes dinero suficiente')


def dar_alta():
    cl_nombre = input('Su nombre: ')
    cl_apellido = input('Su apellido: ')
    cl_numero = input('Su numero de cuenta: ')

    cl = Cliente(cl_nombre, cl_apellido, cl_numero)
    return cl


def init():
    cliente = dar_alta()
    print(cliente)

    seleccion = 0

    while seleccion != 's':
        print("""
        Que desea hacer:
        [r] retirar
        [d] depositar
        [s] salir
        """)
        seleccion = input()

        if seleccion == 'd':
            deposito = int(input('Cuanto desea depositar: '))
            cliente.depositar(deposito)

        elif seleccion == 'r':
            retiro = int(input('Cuanto desea retirar: '))
            cliente.retirar(retiro)

        print(cliente)

    print(f'El banco le desea un excelente dia {cliente.nombre} {cliente.apellido}')


# esto es para iniciar el programa
init()

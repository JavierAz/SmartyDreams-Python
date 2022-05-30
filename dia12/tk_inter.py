from tkinter import *

# iniciar tkinter
aplicacion = Tk()

# dimension de pantalla
aplicacion.geometry('1020x630+10+10')

# no se maximiza
aplicacion.resizable(0, 0)

# titulo de la ventana
aplicacion.title('Los Pinitos - Sistema de Facturacion')

# color del fondo de pantalla
aplicacion.config(bg='burlywood')

# evitar que la pantallase cierre
aplicacion.mainloop()

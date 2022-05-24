import datetime
from datetime import date

mi_hora = datetime.time(17, 35, 20)
print(mi_hora.second)

dia = datetime.date(1998, 11, 16)
print(dia.ctime())

# ejercicio 1
mi_fecha = datetime.date(1999, 2, 3)

# ejercicio 2
hoy = date.today()

# ejrcicio 3
from datetime import datetime

minutos = datetime.now().minute
